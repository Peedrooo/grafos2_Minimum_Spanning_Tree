import sys
import pygame
from src.back.prim import Graph
from src.front.colors import *
from src.front.edge import Edge
from src.front.node import Node

pygame.init()

WIDTH, HEIGHT = 800, 600

font = pygame.font.Font(None, 32)

# Window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minimal Spanning Tree")

# Graph
nodes = []
edges = []

node_color = BLUE

# Main loop
class Interface:
    def __init__(self) -> None:
        self.running = True
        self.clock = pygame.time.Clock()
        self.dragging = False
        self.selected_node = None
        self.connecting = False
        self.start_node = None

    def draw_graph(self):
        screen.fill(BLACK)
        for edge in edges:
            edge.draw(screen)
        for node in nodes:
            node.draw(screen)

    def critical_node(self, color, ids):
        global nodes
        for id in ids:
            nodes[id-1].toggle_color(color)

    def find_clicked_node(self, pos):
        for node in nodes:
            dist = ((pos[0] - node.pos[0])**2 + (pos[1] - node.pos[1])**2)**0.5
            if dist < 20:
                return node
        return None

    def pop_up_cost(self):
        input_box = pygame.Rect(300, 250, 200, 32)
        active = True
        input_text = ''
        error_message = ''

        while active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        try:
                            cost = int(input_text)
                            return cost
                        except ValueError:
                            error_message = "Por favor, insira um número inteiro válido."
                    elif event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                    else:
                        input_text += event.unicode

            screen.fill(BLACK)
            
            question_surface = font.render("Insira o custo da aresta:", True, WHITE)
            screen.blit(question_surface, (input_box.x, input_box.y - 40))
            
            pygame.draw.rect(screen, WHITE, input_box, 2)
            text_surface = font.render(input_text, True, WHITE)
            screen.blit(text_surface, (input_box.x + 5, input_box.y + 5))
            input_box.w = max(200, text_surface.get_width() + 10)

            if error_message:
                error_surface = font.render(error_message, True, RED)
                screen.blit(error_surface, (input_box.x, input_box.y + 40))

            pygame.display.flip()
            self.clock.tick(30)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        pos = pygame.mouse.get_pos()
                        self.selected_node = self.find_clicked_node(pos)
                        if self.selected_node is None:
                            new_node = Node(len(nodes) + 1, pos)
                            nodes.append(new_node)
                        else:
                            self.dragging = True
                    elif event.button == 3:
                        if self.connecting:
                            pos = pygame.mouse.get_pos()
                            end_node = self.find_clicked_node(pos)
                            if end_node is not None and end_node != self.start_node:
                                cost = self.pop_up_cost()
                                edge = Edge(self.start_node, end_node, cost)
                                edges.append(edge)
                            self.connecting = False
                        else:
                            pos = pygame.mouse.get_pos()
                            self.start_node = self.find_clicked_node(pos)
                            if self.start_node:
                                self.connecting = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        self.dragging = False
                        self.selected_node = None
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        minimal_tree = Graph(len(nodes), edges).run()
                        for edge in edges:
                            for minimal_edge in minimal_tree:
                                if (
                                    edge.start_node.id == minimal_edge[0] and edge.end_node.id == minimal_edge[1]) or (
                                    edge.start_node.id == minimal_edge[1] and edge.end_node.id == minimal_edge[0]
                                    ):
                                    edge.toggle_color(GREEN)
                    if event.key == pygame.K_r:
                        for edge in edges:
                            edge.toggle_color(WHITE)
            if self.dragging and self.selected_node is not None:
                pos = pygame.mouse.get_pos()
                self.selected_node.pos = pos

            self.draw_graph()
            pygame.display.flip()
            self.clock.tick(30)

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    Interface().run()
