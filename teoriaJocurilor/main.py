class GameTeory:
    playerA = {}
    playerB = {}
    gains = []

    def __init__(self, path):
        self.read_file(path)

    def read_file(self, path):
        file = open(path, 'r')

        first_line = file.readline().split()
        self.playerA['player'] = first_line[0]
        moves_to_put_in_A = []
        for i in range(1, len(first_line)):
            moves_to_put_in_A.append(first_line[i])
        self.playerA['moves'] = moves_to_put_in_A

        second_line = file.readline().split()
        self.playerB['player'] = second_line[0]
        moves_to_put_in_B = []
        for i in range(1, len(second_line)):
            moves_to_put_in_B.append(second_line[i])
        self.playerB['moves'] = moves_to_put_in_B

        cost_line = file.readline()

        while cost_line != '':
            line_split = cost_line.split()
            for i in range(len(line_split)):
                parsed = line_split[i].split('/')
                self.gains.append((int(parsed[0]), int(parsed[1])))
            cost_line = file.readline()

    def A_dominantStrategy(self):
        nrMovesB = len(self.playerB['moves'])
        nrMovesA = len(self.playerA['moves'])
        nrComparations = nrMovesB

        solutions = []
        aSolution = ()
        """
        print("B poate face n mutari:", nrMovesB)
        print("gains=", len(self.gains), "nrMovesB=", nrMovesB)
        
        
        for i in range(len(self.gains)):
            print("i=", i,self.gains[i])"""


        A_moves = self.playerA.get('moves')
        B_moves = self.playerB.get('moves')
        #print(A_moves, B_moves)
        for j in range(0, nrComparations):
            i = j
            aSolutionGains = (0, 0)
            while i < len(self.gains):
                #print("j=", j, "i=", i)
                #print(self.gains[i])
                #print(A_moves[int(i/nrMovesA)])
                #print(B_moves[j % nrMovesB])
                if aSolutionGains[0] < self.gains[i][0]:
                    aSolutionGains = self.gains[i]
                    #aSolution = (aSolutionGains, A_moves[int(i/nrMovesA)], B_moves[j % nrMovesB])
                i += nrMovesB
            #solutions.append(aSolution)
            i = j
            while i < len(self.gains):
                #print("j=", j, "i=", i)
                #print(self.gains[i])
                #print(A_moves[int(i/nrMovesA)])
                #print(i, nrMovesA, int(i/nrMovesB))
                #print(B_moves[j % nrMovesB])
                if aSolutionGains[0] == self.gains[i][0]:
                    aSolution = (self.gains[i], A_moves[int(i/nrMovesB)], B_moves[j % nrMovesB])
                    solutions.append(aSolution)
                i += nrMovesB
            #solutions.append(aSolution)
        return solutions
    """
    def B_dominantStrategy(self):
        nrMovesB = len(self.playerB['moves'])
        nrMovesA = len(self.playerA['moves'])
        lenGains = len(self.gains)

        A_moves = self.playerA.get('moves')
        B_moves = self.playerB.get('moves')
        # print(A_moves, B_moves)

        solutions = []
        aSolution = ()
        i = 0
        while i < lenGains:
            aSolutionGains = (0, 0)
            for j in range(0, nrMovesA):
                #print(self.gains[i+j])
                #print(A_moves[int((i+j) / nrMovesA)], B_moves[(i+j) % nrMovesB])
                if aSolutionGains[1] < self.gains[i+j][1]:
                    aSolutionGains = self.gains[i]
                    aSolution = (aSolutionGains, A_moves[int((i+j) / nrMovesA)], B_moves[(i+j) % nrMovesB])
            solutions.append(aSolution)
            i += nrMovesA

        return solutions"""

    def B_dominantStrategy(self):
        nrMovesB = len(self.playerB['moves'])
        nrMovesA = len(self.playerA['moves'])
        lenGains = len(self.gains)

        A_moves = self.playerA.get('moves')
        B_moves = self.playerB.get('moves')
        #print(A_moves, B_moves)


        solutions = []
        aSolution = ()
        i = 0
        while i < lenGains:
            aSolutionGains = (0, 0)
            for j in range(0, nrMovesB):
                #print(self.gains[i+j])
                #print(A_moves[int((i+j) / nrMovesA)], B_moves[(i+j) % nrMovesB])
                if aSolutionGains[1] <= self.gains[i+j][1]:
                    aSolutionGains = self.gains[i+j]
                    #aSolution = (aSolutionGains, A_moves[int((i+j) / nrMovesA)], B_moves[(i+j) % nrMovesB])
            #print("Merge la urmatoarea linie")
            #print("deci, gainul ales pe linia asta e ", aSolution)
            #solutions.append(aSolution)
            for j in range(0, nrMovesB):
                #print(self.gains[i+j])
                #print(A_moves[int((i+j) / nrMovesA)], B_moves[(i+j) % nrMovesB])
                if aSolutionGains[1] == self.gains[i+j][1]:
                    aSolution = (self.gains[i+j], A_moves[ int((i+j) / nrMovesB)], B_moves[(i+j) % nrMovesB])
                    #print("se appendeaza", aSolution)
                    solutions.append(aSolution)
            i += nrMovesB

        return solutions


    def dominantStrategy(self):
        dominantStrategyforA = self.A_dominantStrategy()
        dominantStrategyforB = self.B_dominantStrategy()
        possibleSolution = (0, 0)
        for i in dominantStrategyforA:
            # print(i[0][0],i[0][1])
            #se va alege cea mai buna dintre strategiile dominante comune
            if i in dominantStrategyforB: # and i[0][0] > possibleSolution[0] and i[0][1] > possibleSolution[1]:
                possibleSolution = i
        return possibleSolution

    def nashEquilibria(self):
        dominantStrategyforA = self.A_dominantStrategy()
        dominantStrategyforB = self.B_dominantStrategy()
        solutions = []
        for i in dominantStrategyforA:
            # print(i[0][0],i[0][1])
            #se va alege cea mai buna dintre strategiile dominante comune
            if i in dominantStrategyforB:
                solutions.append(i)
        return solutions

    def realDominantStrategyPlayer1(self):
        A_strategy = self.A_dominantStrategy()
        nrMovesA = len(self.playerA['moves'])
        max = 0
        strategy = '0'
        for i in A_strategy:
            #print(i[1])
            aux =0
            for j in A_strategy:
                if j[1]==i[1]:
                    aux+=1
            #aux = A_strategy[1].count(i[1])
            #print(aux)
            if max < aux :
                max = aux
                strategy = i[1]
        if max-1 == nrMovesA:
            return(strategy)
        return False

        #print(A_strategy)

    def realDominantStrategyPlayer2(self):
        B_strategy = self.B_dominantStrategy()
        nrMovesB = len(self.playerB['moves'])
        max = 0
        strategy = '0'
        for i in B_strategy:
            # print(i[1])
            aux = 0
            for j in B_strategy:
                if j[2] == i[2]:
                    aux += 1
            # aux = A_strategy[1].count(i[1])
            # print(aux)
            if max < aux:
                max = aux
                strategy = i[2]
        if max-1 == nrMovesB:
            return(strategy)
        return False


if __name__ == "__main__":
    game = GameTeory("game.txt")
    #print(game.playerA)
    #print(game.playerB)
    #print(game.gains)

    #print(game.A_dominantStrategy())
    #print(game.B_dominantStrategy())

    #print(game.dominantStrategy())


    print(game.realDominantStrategyPlayer1())
    print(game.realDominantStrategyPlayer2())

    print(game.nashEquilibria())





"""

        for j in range(0, nrComparations):
            for i in range(j, len(self.gains), nrMovesB):      #foarte important aici
                print("se va compara asta yuhu", self.gains[i])
                if aSolutionGains[0] < self.gains[i][0]:
                    #print("se va alege ", self.gains[i])
                    aSolutionGains = self.gains[i]
                    A_moves = self.playerA.get('moves')
                    B_moves = self.playerB.get('moves')
                    aSolution = (aSolutionGains, A_moves[i-j], B_moves[j])          #ar fi fost i dar uneori portnesc cu j mai mare, deci asa trebuie calculat
                A_moves = self.playerA.get('moves')
                B_moves = self.playerB.get('moves')
                print(self.gains[i][0], B_moves[j])
            #solutions.append(aSolutionGains)
            solutions.append(aSolution)
            #print("abia dupa se mai compara, iar solution arata asa ", solutions)
            nrMovesB += 1


#pentru verificare itemi corecti, sunt corecti!!!
        A_moves = self.playerA.get('moves')
        B_moves = self.playerB.get('moves')
        print(A_moves, B_moves)
        for j in range(0, nrComparations):
            i = j
            while i < len(self.gains):
                print("j=", j, "i=", i)
                print(self.gains[i])
                print(A_moves[int(i/nrMovesA)])
                print(B_moves[j%nrMovesB])
                i += nrMovesB
                
PlayerA	A_HireLawyer A_NoLawyer
PlayerB B_HireLawyer B_NoLawyer
45/45 70/25
25/70 50/50

PlayerA	A B C D E
PlayerB V W X Y Z
9/9 7/1 5/6 3/4 1/1
7/8 5/2 3/6 1/4 3/3
5/6 3/3 1/8 9/7 1/5
3/9 1/9 9/4 7/9 5/9
1/2 9/8 7/7 5/6 3/7

PlayerA	A B
PlayerB X Y
3/3 1/1
2/4 3/3

PlayerA	A B C D E
PlayerB V W X Y Z
9/9 7/1 5/6 3/4 1/1
7/8 5/2 3/6 1/4 3/3
5/6 3/3 1/8 9/7 1/5
3/9 1/9 9/4 7/9 5/9
1/2 9/8 7/7 5/6 3/7



"""
