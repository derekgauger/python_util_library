"""
Author: Derek Gauger
Date: 07/11/2022

Purpose:
It would be good to learn more about graph implementations in code. This implementation will be one of two.
These graphs will not have weights added. One of my future projects will have weights added.

Description:
Unweighted graph with the following functions:
 - insert_vertex
 - create_edge
 - find_vertex
 - check_connection
"""
import json


# Class that represents vertices
class Vertex:

    # Constructor
    def __init__(self, value):
        self.data = value
        self.connections = []

    # To string method
    def __str__(self):
        return str(self.data)


# Class that represents a graph made up of vertices and edges
class Graph:

    # Constructor
    def __init__(self):
        self.vertices = []
        self.size = 0

    # To string method - prints out dictionary
    def __str__(self):
        output = {}
        for vertex in self.vertices:
            connections = []
            for connection in vertex.connections:
                connections.append(connection.data)
            output[vertex.data] = connections

        return json.dumps(output)

    # size of graph function when using len(graph)
    def __len__(self):
        return self.size

    # Function to find a vertex (input: int or Vertex)
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

    # Function for creating a vertex on the graph (input: int or Vertex)
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

    # Function for checking if there is an edge between vertices
    def check_connection(self, vertex1, vertex2):
        v1 = self.find_vertex(vertex1)
        v2 = self.find_vertex(vertex2)

        if not v1 or not v2:
            return False

        if str(v1) == str(v2):
            raise Exception("Vertices '{}' and '{}' are the same".format(v1, v2))

        for connection in v2.connections:
            if v1.data == connection.data:
                return True

        for connection in v1.connections:
            if v2.data == connection.data:
                return True

        return False

    # function for creating the edge between vertices
    def create_edge(self, vertex1, vertex2):
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

        v1.connections.append(v2)
        v2.connections.append(v1)
