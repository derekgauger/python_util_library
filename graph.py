import json


class Vertex:
    def __init__(self, value):
        self.data = value
        self.connections = []

    def __str__(self):
        return self.data


class Graph:
    def __init__(self):
        self.vertices = []

    def __str__(self):
        output = {}
        for vertex in self.vertices:
            connections = []
            for connection in vertex.connections:
                connections.append(connection.data)
            output[vertex.data] = connections

        return json.dumps(output)

    def insert_vertex(self, new_vertex):
        if type(new_vertex) is int:
            new_vertex = Vertex(new_vertex)
        self.vertices.append(new_vertex)
        return new_vertex

    def create_edge(self, vertex1, vertex2):

        if vertex1 == vertex2:
            raise ValueError("Cannot ")

        for vertex in self.vertices:
            if vertex1 == vertex.data:
                vertex1 = vertex
            elif vertex2 == vertex.data:
                vertex2 = vertex

        if type(vertex1) is int:
            vertex1 = self.insert_vertex(vertex1)

        if type(vertex2) is int:
            vertex2 = self.insert_vertex(vertex2)

        if type(vertex1) is Vertex and type(vertex2) is Vertex:
            vertex1.connections.append(vertex2)
            vertex2.connections.append(vertex1)


g = Graph()
g.insert_vertex(Vertex(1))
g.insert_vertex(Vertex(2))
g.create_edge(1, 2)
g.create_edge(2, 3)
g.create_edge(3, 4)
g.create_edge(6, 6)
print(g)



