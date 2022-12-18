"""CSC111 Tutorial 8: More with Graphs

Module Description
==================
This module contains the Graph and _Vertex classes from lecture, and the functions
you'll complete for Part 2 of this tutorial.

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
            visited.add(self)  # Add self to the list of visited vertices
            for u in self.neighbours:
                if u not in visited:  # Only recurse on vertices that haven't been visited
                    if u.check_connected(target_item, visited):
                        return True

            return False

    #############################################################################
    # Tutorial exercises
    #############################################################################
    def compute_bipartition(self, partition1: set[_Vertex], partition2: set[_Vertex]) -> None:
        """Compute the bipartition for all vertices connected to self, without
        using any vertices in partition1 or partition2.

        The bipartition is computed by MUTATING partition1 and partition2 as follows:
            - self is added to partition1
            - all neighbours of self are added to partition2
            - all neighbours of neighbours of self are added to partition1
            - etc.

        If a vertex should be added to one partition but is already in the other partition,
        raise a ValueError. (In this case, the graph is not bipartite.)
        """
        if self not in partition2:
            partition1.add(self)
        for neighbor in self.neighbours:
            if neighbor not in partition1 and neighbor not in partition2:
                neighbor.compute_bipartition(partition2, partition1)



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
    def bipartition(self) -> tuple[set, set]:
        """Return a bipartition of this graph.

        The returned sets form a bipartition of the graph, and contain ITEMS
        (not _Vertex objects).

        Preconditions:
            - this graph is non-empty
            - this graph is bipartite
            - this graph is connected (this means you only need to call
              _Vertex.compute_bipartition once)

        >>> g = Graph()
        >>> for i in range(1, 7):
        ...     g.add_vertex(i)
        >>> g.add_edge(1, 2)
        >>> g.add_edge(1, 6)
        >>> g.add_edge(2, 3)
        >>> g.add_edge(3, 4)
        >>> g.add_edge(4, 5)
        >>> g.add_edge(5, 6)
        >>> partition1, partition2 = g.bipartition()
        >>> (partition1 == {1, 3, 5} and partition2 == {2, 4, 6}) or\
            (partition1 == {2, 4, 6} and partition2 == {1, 3, 5})
        True
        """
        v_1 = set()
        v_2 = set()

        v_first = [v for v in self._vertices.values()][0]

        v_first.compute_bipartition(v_1, v_2)

        v_1 = {v.item for v in v_1}
        v_2 = {v.item for v in v_2}

        return v_1, v_2


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    # import python_ta
    # python_ta.check_all(config={
    #     'max-line-length': 100,
    #     'disable': ['E1136']
    # }
