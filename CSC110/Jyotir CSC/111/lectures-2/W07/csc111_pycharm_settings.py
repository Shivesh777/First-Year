"""CSC111 W07 - Starter File

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

    ################################################################################################
    # Demo
    ################################################################################################
    def check_connected(self, target_item: Any, visited: set[_Vertex]) -> bool:
        """Return whether this vertex is connected to a vertex corresponding to target_item,
        by a path that DOES NOT use any vertex in visited.

        Preconditions:
            - self not in visited
        """
        if self.item == target_item:
            return True
        else:
            new_vis = set.union({self}, visited)
            for u in self.neighbours:
                val = u.check_connected(target_item, new_vis)
                if val:
                    return True
                else:
                    new_vis.add(u)
            return False


class Graph:
    """A graph."""
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

    ################################################################################################
    # Exercise 1
    ################################################################################################
    def adjacent(self, item1: Any, item2: Any) -> bool:
        """Return whether item1 and item2 are adjacent vertices in this graph.

        Return False if item1 or item2 do not appear as vertices in this graph.
        """
        for vertex in self._vertices:
            if vertex.item == item1:
                if item2 in [x.item for x in vertex.neighbours]:
                    return True
            if vertex.item == item2:
                if item1 in [x.item for x in vertex.neighbours]:
                    return True
        else:
            return False

    def num_edges(self) -> int:
        """Return the number of edges in this graph."""
        edge_so_far = 0
        for item1 in self._vertices:
            for item2 in self._vertices:
                if self.adjacent(item1, item2):
                    edge_so_far += 0.5
        return int(edge_so_far)
    ################################################################################################
    # Demo
    ################################################################################################

    def connected(self, item1: Any, item2: Any) -> bool:
        """Return whether item1 and item2 are connected vertices
        in this graph.

        Return False if item1 or item2 do not appear as vertices
        in this graph.
        """
        if item1 is self._vertices and item2 in self._vertices:
            for item in self._vertices[item1].neighbours:
                if item == item2:
                    return True
                else:
                    val = self.connected(item, item2)
                    if val:
                        return True
            return False
        else:
            return False




