import random


class Node:
    name = ''
    connections = []
    weights = []

    def __init__(self, name, connections, weights):
        self.name = name
        self.connections = connections
        if weights:
            self.weights = [random.uniform(0, 1)]*len(connections)
        else:
            self.weights = weights

    def print_data(self):
        print('Name: {}\n'.format(self.name))
        for index in range(self.connections):
            print('Weight = {} to node: {}\n'.format(self.weights[index], self.connections[index]))
