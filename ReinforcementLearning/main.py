import os

def initial_state():
    my_reward = 0
    k = 0
    q_table = [[], [], [], []]
    for j in q_table:
        for i in range(0, 12):
            if k == 3:
                if i == 0:
                    j.append(1)
                elif i == 11:
                    j.append(2)
                else:
                    j.append(-1)
            else:
                j.append(0)
        k += 1

    return [3, 0], q_table, my_reward

def nextState(ijagent, table, reward, action):

    ijagent_next = list(ijagent)
    if action == 'U' and ijagent[0] != 0:
        ijagent_next[0] = ijagent[0] - 1
    if action == 'D' and ijagent[0] != 3:
        ijagent_next[0] = ijagent[0] + 1
    if action == 'L' and ijagent[1] != 0:
        ijagent_next[1] = ijagent[1] - 1
    if action == 'R' and ijagent[1] != 11:
        ijagent_next[1] = ijagent[1] + 1

    if table[ijagent_next[0]][ijagent_next[1]] == 0:
        next_reward = reward - 1
    else:
        next_reward = reward - 100
        ijagent_next[0] = 3
        ijagent_next[1] = 0

    table[ijagent[0]][ijagent[1]] = 0
    table[ijagent_next[0]][ijagent_next[1]] = 1

    f.write(action + " ")

    return ijagent_next, table, next_reward


def printTable(table, agent, reward):
    for i in table:
        print(i)
    print("The position of our agent is:", agent)
    print("The reward of our agent is:", reward)
    print()


if __name__ == '__main__':

    f = open("moves.txt", "w")

    ijAgent, qTable, myReward = initial_state()
    printTable(qTable, ijAgent, myReward)

    action = 'U'
    next_ijAgent, next_qTable, next_myReward = nextState(ijAgent, qTable, myReward, action)
    printTable(next_qTable, next_ijAgent,  next_myReward)

    action = 'R'
    next_ijAgent, next_qTable, next_myReward = nextState(next_ijAgent, next_qTable, next_myReward, action)
    printTable(next_qTable, next_ijAgent, next_myReward)

    action = 'L'
    next_ijAgent, next_qTable, next_myReward = nextState(next_ijAgent, next_qTable, next_myReward, action)
    printTable(next_qTable, next_ijAgent, next_myReward)

    action = 'D'
    next_ijAgent, next_qTable, next_myReward = nextState(next_ijAgent, next_qTable, next_myReward, action)
    printTable(next_qTable, next_ijAgent, next_myReward)

    action = 'R'
    next_ijAgent, next_qTable, next_myReward = nextState(next_ijAgent, next_qTable, next_myReward, action)
    printTable(next_qTable, next_ijAgent, next_myReward)



