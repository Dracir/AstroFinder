import tkinter as tk
from os import walk
import random
import matplotlib.pyplot as plt
import numpy as np

########################

dataFolder = "Data/Horoscopedotcom/"
filenames = next(walk(dataFolder), (None, None, []))[2]  # [] if no file
statements = []
signScores = {}
signStatementsCount = {}
for signFile in filenames:
    signName = signFile.replace(".txt", "")

    signStatementsCount[signName] = 0
    signScores[signName] = 0
    with open(dataFolder + signFile) as f:
        for line in f.readlines():
            if len(line) < 5:
                continue
            signStatementsCount[signName] += 1
            prettyLine = line.strip()
            statements.append((signName, prettyLine))

signStatementTotalCount = 0
for statementCount in signStatementsCount:
    signStatementTotalCount += signStatementsCount[statementCount]

random.shuffle(statements)

########################
currentStatementIndex = -1


def scoreStatement(score):
    #print("Rate " + str(score) + " for " + statements[currentStatementIndex][0])
    signScores[statements[currentStatementIndex][0]] += score - 2
    moveNextState()


def skipStatement():
    # print("skip")
    signStatementTotalCount[statements[currentStatementIndex][0]] -= 1
    moveNextState()


def moveNextState():
    global currentStatementIndex
    currentStatementIndex += 1
    if currentStatementIndex >= signStatementTotalCount:
        showResults()
    else:
        progressLabel.config(text=str(currentStatementIndex+1) + "/" + str(signStatementTotalCount))
        currentStateLabel.config(text=statements[currentStatementIndex][1])


def showResults():
    print(signScores)
    values = list(map(lambda x: signScores[x], signScores))
    print(values)
    langs = list(map(lambda x: x, signScores))
    students = list(map(lambda x: signScores[x], signScores))

    fig, ax = plt.subplots()

    p1 = ax.bar(langs, students, label='')

    ax.axhline(0, color='grey', linewidth=0.8)
    ax.set_ylabel('Scores')
    ax.set_title('Scores for each signs')
    ind = np.arange(12)
    ax.set_xticks(ind, labels=langs)
    ax.legend()

    # Label with label_type 'center' instead of the default 'edge'
    ax.bar_label(p1, label_type='center')

    plt.show()


window = tk.Tk()

##
frameTop = tk.Frame(window)
statementTitleLabel = tk.Label(frameTop, text="Statement")
statementTitleLabel.pack(padx=10, pady=10, side=tk.LEFT)

progressLabel = tk.Label(frameTop, text="1/" + str(signStatementTotalCount))
progressLabel.pack(padx=10, pady=10, side=tk.RIGHT)

frameTop.pack(fill=tk.X, padx=10, pady=10)


##
currentStateLabel = tk.Label(window, text="I'm a person that is someone!")
currentStateLabel.pack(fill=tk.X, padx=10, pady=10)


# Score buttons
frameScore = tk.Frame(window)

scoreButton = tk.Button(master=frameScore, text=1, command=lambda: scoreStatement(1))
scoreButton.pack(padx=5, pady=10, side=tk.LEFT)
window.bind(1, lambda event: scoreStatement(1))

scoreButton = tk.Button(master=frameScore, text=2, command=lambda: scoreStatement(2))
scoreButton.pack(padx=5, pady=10, side=tk.LEFT)
window.bind(2, lambda event: scoreStatement(2))

scoreButton = tk.Button(master=frameScore, text=3, command=lambda: scoreStatement(3))
scoreButton.pack(padx=5, pady=10, side=tk.LEFT)
window.bind(3, lambda event: scoreStatement(3))

skipButton = tk.Button(master=frameScore, text='X', command=lambda: skipStatement())
skipButton.pack(padx=5, pady=10, side=tk.LEFT)
window.bind('x', lambda event: skipStatement())

frameScore.pack(fill=tk.X, padx=10, pady=10)
#

#currentStatementIndex = 11
#signScores = {'Aries': 1, 'Taurus': 1, 'Scorpio': 1, 'Virgo': 3, 'Capricorn': 3, 'Aquarius': 2, 'Cancer': 2, 'Leo': 1, 'Pisces': 2, 'Sagittarius': 2, 'Libra': 3, 'Gemini': 1}

moveNextState()
window.mainloop()
