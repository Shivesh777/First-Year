"""CSC111 W08 - Rough Solution (Graphs)

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.
"""
from __future__ import annotations
from typing import Any


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

    def print_all_connected(self, visited: set[_Vertex]) -> None:
        """Print all items that this vertex is connected to, WITHOUT using any of the vertices
        in visited.

        Preconditions:
            - self not in visited
        """
        print(self.item)

        visited.add(self)
        for u in self.neighbours:
            if u not in visited:  # Only recurse on vertices that haven't been visited
                u.print_all_connected(visited)

    def print_all_connected_indented(self, visited: set[_Vertex], d: int) -> None:
        """Print all items that this vertex is connected to, WITHOUT using any of the vertices
        in visited.

        Print out the items with indentation level d

        Preconditions:
            - self not in visited
        """
        print('  ' * d + str(self.item))
        visited.add(self)
        for u in self.neighbours:
            if u not in visited:  # Only recurse on vertices that haven't been visited
                u.print_all_connected_indented(visited, d + 1)

    def spanning_tree(self, visited: set[_Vertex]) -> list[set]:
        """Return a spanning tree for all items this vertex is connected to,
        WITHOUT using any of the vertices in visited.

        Preconditions:
            - self not in visited
        """
        edges_so_far = []

        visited.add(self)
        for u in self.neighbours:
            if u not in visited:  # Only recurse on vertices that haven't been visited
                edges_so_far.append({self.item, u.item})
                edges_so_far.extend(u.spanning_tree(visited))

        return edges_so_far


class Graph:
    """A graph.

    >>> graph = Graph()
    >>> graph.add_vertex(4)
    >>> graph.add_vertex(5)
    >>> graph.add_vertex(2)
    >>> graph.add_vertex(6)
    >>> graph.add_edge(4, 5)
    >>> graph.add_edge(4, 2)
    >>> graph.add_edge(2, 6)

    Representation Invariants: (COMPLETE AS HOMEWORK)
        - for each key in self._vertices, the corresponding vertex's item attribute
          equals that key
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
        new_vertex = _Vertex(item, set())
        self._vertices[item] = new_vertex

    def add_edge(self, item1: Any, item2: Any) -> None:
        """Add an edge between the two vertices with the given items in this graph.

        Raise a ValueError if item1 or item2 do not appear as vertices in this graph.

        Preconditions:
            - item1 != item2
        """
        if item1 in self._vertices and item2 in self._vertices:
            v1 = self._vertices[item1]
            v2 = self._vertices[item2]

            v1.neighbours.add(v2)
            v2.neighbours.add(v1)
        else:
            raise ValueError

    def spanning_tree(self) -> list[set]:
        """Return a subset of the edges of this graph that form a spanning tree.
        The edges are returned as a list of sets, where each set contains the two
        ITEMS corresponding to an edge. Each returned edge is in this graph
        (i.e., this function doesn't create new edges!).

        Preconditions:
            - this graph is connected
        """
        all_vertices = list(self._vertices.values())
        start_vertex = all_vertices[0]
        return start_vertex.spanning_tree(set())


if __name__ == '__main__':
    # Sample graph
    g = Graph()
    for i in range(0, 5):
        g.add_vertex(i)
    g.add_edge(0, 1)
    g.add_edge(0, 3)
    g.add_edge(1, 2)
    g.add_edge(1, 4)
    g.add_edge(2, 4)
