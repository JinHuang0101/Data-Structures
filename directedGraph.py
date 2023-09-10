# Author: Jin Huang
# Description: Implement the DirectedGraph class.

import heapq
from collections import deque

class DirectedGraph:
    """
    Class to implement directed weighted graph
    - duplicate edges not allowed
    - loops not allowed
    - only positive edge weights
    - vertex names are integers
    """

    def __init__(self, start_edges=None):
        """
        Store graph info as adjacency matrix
        """
        self.v_count = 0
        self.adj_matrix = []

        # populate graph with initial vertices and edges (if provided)
        # before using, implement add_vertex() and add_edge() methods
        if start_edges is not None:
            v_count = 0
            for u, v, _ in start_edges:
                v_count = max(v_count, u, v)
            for _ in range(v_count + 1):
                self.add_vertex()
            for u, v, weight in start_edges:
                self.add_edge(u, v, weight)

    def __str__(self):
        """
        Return content of the graph in human-readable form
        """
        if self.v_count == 0:
            return 'EMPTY GRAPH\n'
        out = '   |'
        out += ' '.join(['{:2}'.format(i) for i in range(self.v_count)]) + '\n'
        out += '-' * (self.v_count * 3 + 3) + '\n'
        for i in range(self.v_count):
            row = self.adj_matrix[i]
            out += '{:2} |'.format(i)
            out += ' '.join(['{:2}'.format(w) for w in row]) + '\n'
        out = f"GRAPH ({self.v_count} vertices):\n{out}"
        return out

    # ------------------------------------------------------------------ #

    def add_vertex(self) -> int:
        """
        Add a new vertex to the graph, assign the vertex a reference index(integer),
        returns the number of vertices in the graph after the addition
        """
        matrix = self.adj_matrix
        vertices = self.v_count

        if vertices == 0:
            matrix.append([0])
        else:
            for i in range(0,vertices):
                matrix[i].append(0)

            list = [0 for j in range(vertices+1)]
            matrix.append(list)

        self.v_count += 1

        return self.v_count



    def add_edge(self, src: int, dst: int, weight=1) -> None:
        """
        Add a new edge the graph, connecting the two vertices with the provided indices.
        Do nothing if: vertex do not exist, weight is not positive, or src and dst refer to
        the same vertex.
        Update the weight it it already exists.
        """
        matrix = self.adj_matrix
        vertices = self.v_count

        # vertex do not exist
        if src not in range(vertices) or dst not in range(vertices):
            return
        # weight not positive
        if weight <= 0:
            return
        # src and dst the same
        if src == dst:
            return

        matrix[src][dst] = weight

        return


    def remove_edge(self, src: int, dst: int) -> None:
        """
        Remove an edge bewteen the two vertices with provided indices.
        Do nothing if: vertex do not exist or no edge between them.
        """
        matrix = self.adj_matrix
        vertices = self.v_count

        # vertex do not exist
        if src not in range(vertices) or dst not in range(vertices):
            return
        # no edge
        if matrix[src][dst] == 0:
            return

        matrix[src][dst] = 0

        return

    def get_vertices(self) -> []:
        """
        Return a list of the vertices of the graph.
        """
        vertices = self.v_count
        result = []
        for i in range(vertices):
            result.append(i)
        return result


    def get_edges(self) -> []:
        """
        Return a list of edges in the graph,
        Each list is a tuple: (src,dst,weight)
        """
        matrix = self.adj_matrix
        vertices = self.v_count
        result = []

        for row in range(vertices):
            for col in range(vertices):
                if matrix[row][col] != 0:
                    edge = (row,col,matrix[row][col])
                    result.append(edge)

        return result


    def is_valid_path(self, path: []) -> bool:
        """
        Takes a list of vertex indices and return True if they represent a valid path in the graph.
        Empty path is valid.
        """
        matrix = self.adj_matrix
        vertices = self.v_count

        if len(path) == 1:
            if path[0] not in range(vertices):
                return False
        else:
            for i in range(len(path)-1):
                src = path[i]
                dst = path[i+1]
                if matrix[src][dst] == 0:
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
        Perform a dfs in the graph and return a list of vertices visited.
        Pick the vertices by vertex index in ascending order.
        """
        matrix = self.adj_matrix
        visited = set()
        result = []
        vertices = self.v_count
        global terminateFlag
        terminateFlag = False

        def rec_dfs(v_start, v_end, visited):
            """
            Performs dfs recursively on a directed graph
            """
            global terminateFlag

            if v_start in visited:
                return

            # terminate if v_end reached
            if v_start == v_end:
                terminateFlag = True
                result.append(v_start)
                visited.append(v_start)
                return


            # mark the current vertex as visited
            # append it to output list
            visited.add(v_start)
            result.append(v_start)

            # recur for all its neighbours
            neighbours = []
            for i in range(vertices):
                if matrix[v_start][i] != 0:
                    neighbours.append(i)

            neighboursCopy = self.clone(neighbours)

            while neighboursCopy:
                for nextPick in neighboursCopy:
                    nextPick = min(neighboursCopy)
                    if nextPick not in visited:
                        rec_dfs(nextPick, v_end, visited)

                    if nextPick in visited and terminateFlag is True:
                        return

                    neighboursCopy.remove(nextPick)


        rec_dfs(v_start, v_end, visited)
        return result



    def bfs(self, v_start, v_end=None) -> []:
        """
        Perform a bfs in the graph and return a list of vertices visited.
        Pick the vertices by vertex index in ascending order.
        """
        matrix = self.adj_matrix
        vertices = self.v_count
        result = []
        visited = []
        queue = []

        # mark the current vertex as visited
        visited.append(v_start)

        # enqueue the current vertex
        queue.append(v_start)

        while queue:
            # dequeue a vertex and append it to result
            current = queue.pop(0)
            result.append(current)

            # terminate if v_end reached
            if current == v_end:
                return result

            # get all neighbours of the current vertex,
            # enqueue unvisited vertices
            neighbours = []
            for i in range(vertices):
                if matrix[current][i] != 0:
                    neighbours.append(i)

            neighboursCopy = self.clone(neighbours)

            while neighboursCopy:
                for nextPick in neighboursCopy:
                    nextPick = min(neighboursCopy)

                    if nextPick not in visited:
                        queue.append(nextPick)
                        visited.append(nextPick)

                    neighboursCopy.remove(nextPick)

        return result


    def has_cycle(self):
        """
        Check if a directed graph has cycle. Return True if there is at least one,
        Return False otherwise.
        """
        matrix = self.adj_matrix
        vertices = self.v_count
        verticesDict = {}
        for key in range(vertices):
            verticesDict[key] = -1  # each vertex has a flag, -1:unvisited, 0: stack, 1: visited
        visited = []
        stack = []
        global terminateFlag
        terminateFlag = False

        def rec_dfs(v_start, visited, stack):
            """
            Recursively performs dfs on the given vertex
            """
            global terminateFlag
            checkFlag = True

            if v_start in visited:
                return


            #push the current node to stack
            stack.append(v_start)
            verticesDict[v_start] = 0

            # visit all vertices adjacent to current vertex
            neighbours = []
            for i in range(vertices):
                if matrix[v_start][i] != 0:
                    neighbours.append(i)

            # dead end: remove from the stack, mark as visited
            if len(neighbours) == 0:
                verticesDict[v_start] = 1
                visited.append(v_start)
                stack.pop()
                return

            for nextPick in neighbours:
                checkFlag = True
                # a neighbour is on stack: cycle
                if verticesDict[nextPick] == 0:
                    terminateFlag = True
                    return

                if nextPick not in visited:
                    # recur
                    rec_dfs(nextPick, visited, stack)

                if terminateFlag is True:
                    return True

                # visited if all neighbours are visited
                for i in range(len(neighbours)):
                    if verticesDict[neighbours[i]] != 1:
                        checkFlag = False

                # all neighbours are visited
                #dead end: remove, from the stack, mark as visited
                if checkFlag is True:
                    verticesDict[v_start] = 1
                    visited.append(v_start)
                    stack.pop()
                    return

            return


        # perform dfs on every vertex
        for i in range(vertices):
            if i not in visited:
                result = rec_dfs(i,visited,stack)
                if result is True:
                    return True
        return False



    def dijkstra(self, src: int) -> []:
        """
        Implement the Dijkstra algorithm to compute the length of the shortest
        path from a given vertex to all other vertices in the graph.
        Return a list with one value per each vertex in the graph.
        If a certain vertex is not reachable from SRC, returned value is 'inf'.
        """
        matrix = self.adj_matrix
        vertices = self.v_count

        distance = [float('inf') for i in range(vertices)]
        distance[src] = 0
        visited = set()
        v_start = src
        breakFlag1 = False
        breakFlag = False

        # loop until all vertices are visited
        while len(visited) < vertices:

            # find all vertices adjacent to current vertex
            neighbours = {}
            for i in range(vertices):
                if matrix[v_start][i] != 0:
                    neighbours[i] = matrix[v_start][i]

            neighboursWeight = []
            heapq.heapify(neighboursWeight)

            for value in neighbours.values():
                heapq.heappush(neighboursWeight, value)

            neighboursCopy = self.clone(neighbours.keys())
            while neighboursWeight:
                minWeight = heapq.heappop(neighboursWeight)

                for nextPick in neighboursCopy:
                    if neighbours[nextPick] == minWeight and nextPick in visited:
                        breakFlag1 = True
                        break
                    if neighbours[nextPick] != minWeight:
                        continue
                    else:
                        break

                if breakFlag1 is True:
                    breakFlag1 = False
                    neighboursCopy.remove(nextPick)             # in case equal weight
                    continue


                nextPickDist = distance[v_start] + neighbours[nextPick]
                neighboursCopy.remove(nextPick)                 # in case equal weight

                if distance[nextPick] == float('inf'):
                    distance[nextPick] = nextPickDist
                elif nextPickDist < distance[nextPick]:
                    distance[nextPick] = nextPickDist

            visited.add(v_start)

            # pick a new v_start
            restMinDist = {}
            for i in range(vertices):
                if distance[i] != float('inf'):
                    restMinDist[i] = distance[i]

            restMinDisHeap = []
            heapq.heapify(restMinDisHeap)

            for vertex in restMinDist.keys():
                dist = restMinDist[vertex]
                heapq.heappush(restMinDisHeap, dist)

            while restMinDisHeap:
                minDist = heapq.heappop(restMinDisHeap)
                for vertex in restMinDist.keys():
                    if restMinDist[vertex] == minDist and vertex not in visited:
                        v_start = vertex
                        breakFlag = True
                        break
                if breakFlag is True:
                    breakFlag = False
                    break

            # if cannot update distance, stop.
            if v_start in visited:
                break

        return distance
