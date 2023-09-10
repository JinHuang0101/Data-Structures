# Author: Jin Huang
# Description: Implement the UndirectedGraph class

import heapq
from collections import deque

class UndirectedGraph:
    """
    Class to implement undirected graph
    - duplicate edges not allowed
    - loops not allowed
    - no edge weights
    - vertex names are strings
    """

    def __init__(self, start_edges=None):
        """
        Store graph info as adjacency list
        """
        self.adj_list = dict()

        # populate graph with initial vertices and edges (if provided)
        # before using, implement add_vertex() and add_edge() methods
        if start_edges is not None:
            for u, v in start_edges:
                self.add_edge(u, v)

    def __str__(self):
        """
        Return content of the graph in human-readable form
        """
        out = [f'{v}: {self.adj_list[v]}' for v in self.adj_list]
        out = '\n  '.join(out)
        if len(out) < 70:
            out = out.replace('\n  ', ', ')
            return f'GRAPH: {{{out}}}'
        return f'GRAPH: {{\n  {out}}}'

    # ------------------------------------------------------------------ #

    def add_vertex(self, v: str) -> None:
        """
        Add new vertex to the graph,
        Do nothing if the same vertex exists.
        """
        if v not in self.adj_list.keys():
            self.adj_list[v] = []
        return


        
    def add_edge(self, u: str, v: str) -> None:
        """
        Add edge to the graph,
        If either (or both) vertex do not exist, create the vertex and then create an edge between them.
        If an edge already exists or if u and v refer to the same vertex, do nothing.
        """
        # check if u and v are the same
        if u == v:
            return

        dict = self.adj_list

        # if either or both vertex do not exist, create the vertex
        if u not in dict.keys():
            self.add_vertex(u)
        if v not in dict.keys():
            self.add_vertex(v)

        # check if the edge already exist, if not: create an edge
        if v not in dict[u]:
            dict[u].append(v)

        if u not in dict[v]:
            dict[v].append(u)

        return



    def remove_edge(self, v: str, u: str) -> None:
        """
        Remove edge from the graph,
        If either or both vertex do not exist, or if there is no such edge, do nothing
        """
        dict = self.adj_list

        # vertex or edge do not exist
        if v not in dict.keys() or u not in dict.keys():
            return
        if v not in dict[u] or u not in dict[v]:
            return

        # remove edge
        dict[u].remove(v)
        dict[v].remove(u)

        return
        

    def remove_vertex(self, v: str) -> None:
        """
        Remove vertex and all connected edges,
        If vertex does not exist, do nothing
        """
        dict = self.adj_list

        if v not in dict.keys():
            return

        # delete the key/value pair
        del dict[v]

        # delete the value in other keys
        for key in dict.keys():
            if v in dict[key]:
                dict[key].remove(v)

        return



    def get_vertices(self) -> []:
        """
        Return list of vertices in the graph (any order)
        """
        dict = self.adj_list
        vertcies = []
        for i in dict.keys():
            vertcies.append(i)
        return vertcies


    def get_edges(self) -> []:
        """
        Return list of edges in the graph (any order)
        """
        dict = self.adj_list
        edges = []

        # append all edges
        for key, value in dict.items():
            for eachValue in value:
                edge = (key, eachValue)
                edges.append(edge)
                # check for duplicates
                for eachEdge in edges:
                    if eachEdge == (eachValue, key):
                        edges.remove(eachEdge)

        return edges
        

    def is_valid_path(self, path: []) -> bool:
        """
        Return true if provided path is valid, False otherwise
        Valid path if one can travel from the first vertex in the list to the last vertex in the list,
        at each step traversing over an edge in the graph.
        Empty path is valid.
        """
        # empty path is valid
        if not path:
            return True

        dict = self.adj_list
        edges = self.get_edges()
        vertices = self.get_vertices()

        # if only one vertex
        if len(path) == 1:
            if path[0] in vertices:
                return True
            else:
                return False

        # else, check if edge exists
        for i in range(len(path)-1):
            vertex1 = path[i]
            vertex2 = path[i+1]
            if (vertex1,vertex2) not in edges and (vertex2, vertex1) not in edges:
                return False
        return True
       
    def clone(self,l):
        """
        Takes an original list and clones the list, such that
        changes made to the cloned list won't affect the original list.
        """
        cloneList = list(l)
        return cloneList


    def dfs(self, v_start, v_end=None) -> []:
        """
        Return list of vertices visited during DFS search
        Vertices are picked in alphabetical order
        If starting vertex not in the graph, return an empty list
        If end vertex not in the graph, search as if there was no end vertex
        """
        dict = self.adj_list
        edges = self.get_edges()
        vertices = self.get_vertices()
        result = []
        visited = []
        global terminateFlag
        terminateFlag = False

        # starting vertex not in the graph
        if v_start not in vertices:
            return result

        # end vertex not in the graph
        if v_end is not None and v_end not in vertices:
            v_end = None

        # recursive dfs helper
        def rec_dfs(v_start, v_end, visited):
            """
            Takes a starting vertex, ending vertex, and visited list,
            recursively performs dfs.
            """
            global terminateFlag

            if v_start in visited:
                return

            if v_start == v_end:
                terminateFlag = True
                result.append(v_start)
                visited.append(v_start)
                return

            # append this vertex to result
            result.append(v_start)

            # mark the current vertex as visited
            visited.append(v_start)

            # visit all vertices adjacent to current vertex
            neighbours = dict[v_start]
            neighboursCopy = self.clone(neighbours)

            while len(neighboursCopy) != 0:
                for nextPick in neighboursCopy:
                    nextPick = min(neighboursCopy)

                    if nextPick not in visited:
                        rec_dfs(nextPick, v_end, visited)

                    if nextPick in visited and terminateFlag is True:
                            return
                    neighboursCopy.remove(nextPick)



        # call the recursive dfs helper function
        rec_dfs(v_start, v_end, visited)

        return result


    def bfs(self, v_start, v_end=None) -> []:
        """
        Return list of vertices visited during BFS search
        Vertices are picked in alphabetical order
        If starting vertex not in the graph, return an empty list
        If end vertex not in the graph, search as if there was no end vertex
        """
        dict = self.adj_list
        edges = self.get_edges()
        vertices = self.get_vertices()
        result = []
        visited = []
        queue = []

        # starting vertex not in the graph
        if v_start not in vertices:
            return result

        # end vertex not in the graph
        if v_end is not None and v_end not in vertices:
            v_end = None

        if v_start in visited:
            return

        # mark the current vertex as visited
        visited.append(v_start)

        # enqueue the current vertex
        queue.append(v_start)

        while queue:

            # dequeue a vertex and append it to result
            current = queue.pop(0)
            result.append(current)

            if current == v_end:
                return result

            # get all neighbours of the current vertex,
            # enqueue unvisited vertices
            neighbours = dict[current]
            neighboursCopy = self.clone(neighbours)

            while neighboursCopy:
                for nextPick in neighboursCopy:
                    nextPick = min(neighboursCopy)

                    if nextPick not in visited:
                        queue.append(nextPick)
                        visited.append(nextPick)

                    neighboursCopy.remove(nextPick)


        return result



    def count_connected_components(self):
        """
        Return number of connected componets in the graph
        """
        dict = self.adj_list
        vertices = self.get_vertices()
        count = 0
        visited = []

        def rec_dfs(v_start, visited):
            """
            Recursively performs dfs on the given vertex
            """
            if v_start in visited:
                return
            # mark the current vertex as visited
            visited.append(v_start)

            # visit all vertices adjacent to current vertex
            neighbours = dict[v_start]
            for vertex in neighbours:
                if vertex not in visited:
                    rec_dfs(vertex, visited)
            return


            # perform dfs on every vertex
        for vertex in vertices:
            if vertex not in visited:
                rec_dfs(vertex, visited)
                count += 1

        return count


      

    def has_cycle(self):
        """
        Return True if graph contains a cycle, False otherwise
        """
        dict = self.adj_list
        vertices = self.get_vertices()
        verticesDict = {}
        for key in vertices:
            verticesDict[key] = -1          # each vertex has a flag, -1:unvisited, 0: queue, 1: visited

        visited = []
        queue = []

        for i in range(len(vertices)):
            v_start = vertices[i]

            # enqueue the current vertex
            queue.append(v_start)
            verticesDict[v_start] = 0

            while queue:
                # dequeue a vertex
                current = queue.pop(0)

                # get all neighbours of the current vertex,
                # enqueue unvisited vertices
                neighbours = dict[current]
                for nextPick in neighbours:
                    if verticesDict[nextPick] == 0:         # a neighbour is in queue: cycle found
                        return True
                    if nextPick not in visited:
                        queue.append(nextPick)
                        verticesDict[nextPick] = 0
                        #visited.append(nextPick)
                # mark the current vertex as visited
                visited.append(current)
                verticesDict[current] = 1

        return False