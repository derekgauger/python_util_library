"""
Author: Derek Gauger
Date: 07/12/2022

Purpose:
I wanted to learn a bit more about implementing a graph in code. I have now done weighted and unweighted graphs
so I will no longer have to implement them from scratch everytime in class.

Description:
Weighted graph with the following functions:
 - insert_vertex
 - create_edge
 - find_vertex
 - check_connection
 - Prim's Algorithm
"""
import json
import sys


# Class representing an edge
class Edge:

    # Constructor
    def __init__(self, weight, original_vertex, connected_vertex):
        self.weight = weight
        self.connected_vertex = connected_vertex
        self.original_vertex = original_vertex

    # To string method for edges
    def __str__(self):
        return "{} <--{}--> {}".format(self.original_vertex.data, self.weight, self.connected_vertex.data)


# Class representing a Vertex
class Vertex:

    # Constructor
    def __init__(self, value):
        self.data = value
        self.connections = []

    # To string method
    def __str__(self):
        return str(self.data)


# Class representing the weighted graph
class WeightedGraph:

    # Constructor
    def __init__(self):
        self.vertices = []
        self.size = 0

    # length method to return the size of the graph
    def __len__(self):
        return self.size

    # To string method
    def __str__(self):
        output = {}

        for vertex in self.vertices:
            connections = []
            for connection in vertex.connections:

                connections.append(str(connection))

            output[vertex.data] = connections

        return json.dumps(output, indent=4)

    # Method for finding a vertex
    def find_vertex(self, vertex):

        if type(vertex) is int:
            for v in self.vertices:
                if vertex == v.data:
                    return v
        elif type(vertex) is Vertex:
            for v in self.vertices:
                if vertex.data == v.data:
                    return v

        return None

    # Method for putting a vertex into a graph
    def insert_vertex(self, new_vertex):
        exists = self.find_vertex(new_vertex)
        if not exists:
            if type(new_vertex) is int:
                new_vertex = Vertex(new_vertex)
            self.vertices.append(new_vertex)
            self.size += 1
            return new_vertex
        else:
            raise Exception("This vertex already exists within this graph")

    # Method for checking if there is an edge between two vertices
    def check_connection(self, vertex1, vertex2):
        v1 = self.find_vertex(vertex1)
        v2 = self.find_vertex(vertex2)

        if not v1 or not v2:
            return False

        if str(v1) == str(v2):
            raise Exception("Vertices '{}' and '{}' are the same".format(v1, v2))

        for connection in v2.connections:
            if v1.data == connection.connected_vertex.data:
                return True

        for connection in v1.connections:
            if v2.data == connection.connected_vertex.data:
                return True

        return False

    # Function for creating an edge between two vertices
    def create_connection(self, vertex1, weight, vertex2):
        if str(vertex1) == str(vertex2):
            raise Exception("Cannot connect vertices '{}' and '{}'".format(vertex1, vertex2))

        v1 = self.find_vertex(vertex1)
        v2 = self.find_vertex(vertex2)

        if self.check_connection(v1, v2):
            raise Exception("Vertices '{}' and '{}' are already connected".format(v1, v2))

        if not v1:
            v1 = self.insert_vertex(vertex1)

        if not v2:
            v2 = self.insert_vertex(vertex2)

        connection = Edge(weight, v1, v2)

        v1.connections.append(connection)
        v2.connections.append(connection)

    # Prim's algorithm for a minimum spanning tree
    def prims_min_span_tree(self, start_vertex):
        start_vertex = self.find_vertex(start_vertex)
        if not start_vertex:
            raise Exception("'{}' vertex is not found".format(start_vertex))
        span_tree = [start_vertex]

        while len(span_tree) != len(self):
            min_weight = sys.maxsize
            min_weight_vertex = start_vertex
            for vertex in reversed(span_tree):
                for connection in vertex.connections:
                    to_vertex = connection.connected_vertex
                    weight = connection.weight
                    if min_weight >= weight and to_vertex not in span_tree:
                        min_weight = weight
                        min_weight_vertex = to_vertex

            span_tree.append(min_weight_vertex)
        return span_tree
