"""CSC111 Tutorial 8: More with Graphs

Module Description
==================
This module contains a copy of the Graph and _Vertex classes that you'll adapt
for visualization purposes.

Note that in order to use networkx, you'll need to install the following Python libraries:
- networkx
- numpy
- scipy

Ask your TA or classmates for help if you aren't sure how to install a new library.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2022 Mario Badr, David Liu.
"""
from __future__ import annotations
import random
from typing import Any

import networkx
import pygame
from pygame.colordict import THECOLORS

# When you are ready to complete Question 2, install the libraries
# networkx, numpy, and scipy, and then uncomment the line below.
# import networkx


class _Vertex:
    """A vertex in a graph.

    Instance Attributes:
        - item: The data stored in this vertex.
        - neighbours: The vertices that are adjacent to this vertex.

    Representation Invariants:
        - self not in self.neighbours
        - all(self in u.neighbours for u in self.neighbours)
    """
    item: Any
    neighbours: set[_Vertex]

    def __init__(self, item: Any, neighbours: set[_Vertex]) -> None:
        """Initialize a new vertex with the given item and neighbours."""
        self.item = item
        self.neighbours = neighbours

    def check_connected(self, target_item: Any, visited: set[_Vertex]) -> bool:
        """Return whether this vertex is connected to a vertex corresponding to the target_item,
        WITHOUT using any of the vertices in visited.

        Preconditions:
            - self not in visited
        """
        if self.item == target_item:
            # Our base case: the target_item is the current vertex
            return True
        else:
            visited.add(self)         # Add self to the list of visited vertices
            for u in self.neighbours:
                if u not in visited:  # Only recurse on vertices that haven't been visited
                    if u.check_connected(target_item, visited):
                        return True

            return False


class Graph:
    """A graph.
    """
    # Private Instance Attributes:
    #     - _vertices:
    #         A collection of the vertices contained in this graph.
    #         Maps item to _Vertex object.
    _vertices: dict[Any, _Vertex]

    def __init__(self) -> None:
        """Initialize an empty graph (no vertices or edges)."""
        self._vertices = {}

    def add_vertex(self, item: Any) -> None:
        """Add a vertex with the given item to this graph.

        The new vertex is not adjacent to any other vertices.

        Preconditions:
            - item not in self._vertices
        """
        # Note: changed this self._vertices
        if item not in self._vertices:
            self._vertices[item] = _Vertex(item, set())

    def add_edge(self, item1: Any, item2: Any) -> None:
        """Add an edge between the two vertices with the given items in this graph.

        Raise a ValueError if item1 or item2 do not appear as vertices in this graph.

        Preconditions:
            - item1 != item2
        """
        if item1 in self._vertices and item2 in self._vertices:
            v1 = self._vertices[item1]
            v2 = self._vertices[item2]

            # Add the new edge
            v1.neighbours.add(v2)
            v2.neighbours.add(v1)
        else:
            # We didn't find an existing vertex for both items.
            raise ValueError

    def adjacent(self, item1: Any, item2: Any) -> bool:
        """Return whether item1 and item2 are adjacent vertices in this graph.

        Return False if item1 or item2 do not appear as vertices in this graph.
        """
        if item1 in self._vertices and item2 in self._vertices:
            v1 = self._vertices[item1]
            return any(v2.item == item2 for v2 in v1.neighbours)
        else:
            # We didn't find an existing vertex for both items.
            return False

    def connected(self, item1: Any, item2: Any) -> bool:
        """Return whether item1 and item2 are connected vertices in this graph.

        Return False if item1 or item2 do not appear as vertices in this graph.

        >>> g = Graph()
        >>> g.add_vertex(1)
        >>> g.add_vertex(2)
        >>> g.add_vertex(3)
        >>> g.add_vertex(4)
        >>> g.add_edge(1, 2)
        >>> g.add_edge(2, 3)
        >>> g.connected(1, 3)
        True
        >>> g.connected(1, 4)
        False
        """
        if item1 in self._vertices and item2 in self._vertices:
            v1 = self._vertices[item1]
            return v1.check_connected(item2, set())  # Pass in an empty "visited" set
        else:
            return False

    ############################################################################
    # Tutorial exercises
    ############################################################################
    def draw(self, screen: pygame.Surface) -> None:
        """Draw the vertices and edges of this graph onto the given screen.

        You can decide how you want to compute locations for each vertex.
        Some ideas are: choosing random coordinates for each vertex, and arranging
        the vertices in a circle.
        To keep things simple, draw each edge as a straight line between vertices.
        """
        start = [vertex for vertex in self._vertices.values()][0]
        pygame.draw.circle(screen, )

    def draw_nx(self, screen: pygame.Surface) -> None:
        """Draw the vertices and edges of this graph onto the given screen.

        Use the networkx library to determine graph layouts.
        In order to do this, you'll need to first convert self into a networkx.Graph object
        (this class has the same name as our Graph class, but it's different!).
        Luckily, our Graph interface is similar to the networkx.Graph class:

            - use networkx.Graph.add_node to add an ITEM to the graph
            - use networkx.Graph.add_edge to add an edge between two ITEMS in the graph

        After you've created the networkx.Graph object, we've provided the code to call
        a layout algorithm on it. Your task after that will be to extract the vertex
        coordinates and use them to draw the vertices and edges onto the pygame screen.
        """
        # 1. Convert self into a networkx.Graph object.
        graph_nx = networkx.Graph()
        ...

        # 2. Call a networkx graph layout algorithm. This returns a dictionary where each
        # key is a vertex ITEM, and each corresponding value is an (x, y) coordinate.
        center = (screen.get_width() // 2, screen.get_height() // 2)
        scale = screen.get_width() // 2 - 10
        vertex_pos = networkx.spring_layout(graph_nx, center=center, scale=scale)

        # 3. Use vertex_pos in the same way as Graph.draw to draw this graph to pygame!
        ...


################################################################################
# Graph visualization functions
################################################################################
SCREEN_SIZE = (800, 800)


def visualize_graph(graph: Graph) -> None:
    """Visualize a graph using pygame."""
    screen = initialize_screen(SCREEN_SIZE)
    graph.draw(screen)
    pygame.display.flip()
    while True:
        if any(event.type == pygame.QUIT for event in pygame.event.get()):
            break
    pygame.display.quit()
    pygame.quit()


def visualize_graph_nx(graph: Graph) -> None:
    """Visualize a graph using pygame."""
    screen = initialize_screen(SCREEN_SIZE)
    graph.draw_nx(screen)
    pygame.display.flip()
    while True:
        if any(event.type == pygame.QUIT for event in pygame.event.get()):
            break
    pygame.display.quit()
    pygame.quit()


def initialize_screen(screen_size: tuple[int, int]) -> pygame.Surface:
    """Initialize pygame and the display window.

    This is a helper function for the "visualize_graph" functions above.
    You can safely ignore this function.
    """
    pygame.display.init()
    pygame.font.init()
    screen = pygame.display.set_mode(screen_size)
    screen.fill(THECOLORS['white'])
    pygame.display.flip()

    pygame.event.clear()
    pygame.event.set_blocked(None)
    pygame.event.set_allowed([pygame.QUIT])

    return screen


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    # Try creating your own random graph here, and then calling visualize_graph on it.
    g = Graph()
    ...

    # visualize_graph(g)

    # import python_ta
    # python_ta.check_all(config={
    #     'max-line-length': 100,
    #     'disable': ['E1136']
    # }
