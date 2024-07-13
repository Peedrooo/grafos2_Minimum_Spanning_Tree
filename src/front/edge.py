import math
from typing import Any

import pygame

from src.front.node import Node
from src.front.colors import WHITE


class Edge:
    def __init__(
            self, start_node: Node,
            end_node:Node, coust: int
            ):
        self.start_node = start_node
        self.end_node = end_node
        self.coust = coust

    def draw(self, screen):
        pygame.draw.line(screen, WHITE, self.start_node.pos, self.end_node.pos, 2)
