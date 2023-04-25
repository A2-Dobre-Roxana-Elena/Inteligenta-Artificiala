import random
from Neuron import Node


class NN:
    """
1. sepal length in cm
2. sepal width in cm
3. petal length in cm
4. petal width in cm
5. class:
-- Iris Setosa
-- Iris Versicolour
-- Iris Virginica
    """

    input = []
    hidden = []
    output = []
    size_input = 0
    size_hidden = 0
    size_output = 0

    train_data = []
    test_data = []

    max_epochs = 5

    def __init__(self, path_for_data):
        f = open(path_for_data, 'r')
        data_from_file = []
        read_one_line = f.readline()
        while read_one_line != '':
            data_from_file.append(read_one_line.replace('\n', '').split(','))
            read_one_line = f.readline()
        random.shuffle(data_from_file)

        size = len(data_from_file)
        """
        newList = originalList[0.05 * size - 1:0.95 * size + 1]
        """

        #middle_of_file = len(data_from_file)//2
        size = 0.70*size
        self.train_data = data_from_file[0:int(size)]
        self.test_data = data_from_file[int(size)+1:]

        self.output =\
            [Node('Setosa', [], []),
             Node('Versicolour', [], []),
             Node('Virginica', [], [])]

        self.hidden =\
            [Node('h1', self.output, []),
             Node('h2', self.output, []),
             Node('h3', self.output, []),
             Node('h4', self.output, [])]

        self.input =\
            [Node('sepal_length', self.hidden, []),
             Node('sepal_width', self.hidden, []),
             Node('petal_length', self.hidden, []),
             Node('petal_width', self.hidden, [])]

        self.size_input = len(self.input)
        self.size_hidden = len(self.hidden)
        self.size_output = len(self.output)

    def print_test_data_train_data(self):
        print('Train data:\n{}'.format(self.train_data))
        print('\nTest data:\n{}'.format(self.test_data))

    def print_parameters(self):
        print('Maximum number of epochs = {}\n---\nInput nodes (size = {})\n---\nHidden nodes (size = {})\n---\nOutput nodes (size = {})\n'.format(
                self.max_epochs, self.size_input, self.size_hidden, self.size_output))
        print(len(self.train_data))
        print(len(self.test_data))


if __name__ == '__main__':
    RN = NN('iris.data')
    RN.print_test_data_train_data()
    print('\n---\n')
    RN.print_parameters()


#3 variabile, nr neuroni intrare iesire ascuns, nr epoci, ponderi(matrici)
"""
dam instanta la retea, da output 3 probabilitati- pe exemplu
pe str de output: 3categorii
pe input 4 neuroni ca avem 4 valori(sepale petale cu lungime latime)
prin ponderi input legat de hidden
bias un nr real complementeaza ponderile-este ca o pondere(daca xi este 1 sau -1)
feed forward in functie de pondere si valoare de input (suma ponderata tuturor)-iesirile pt str output
functie de activare pe stratul ascuns si de output(functie signoida)-nu o sa mai avem o combinatie liniara
pe output -f. softmax-o sa avem probabilitati
pe output vrem sa obtinem 0 pe 2 din ele
mergem invers si update-up ponderile
midsquare error
gradientidupa str de output calculam o eroare dintre val asteptata si cea calculata

ponderile le putem face data viitoare

retropropagare:
calcum un gradient pt fiecare din output si ajustam ponderile
gradient pt stratul ascuns si ajustam ponderile
dupa prezentarea instatelor la retea facem corectiile

ultima tema grea-Q learning
"""