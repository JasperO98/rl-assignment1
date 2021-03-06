import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from hexgame import HexGame
from hexplayer import HexPlayerEnhanced

sns.set()


def simulate_game(sizes, timeout, TT_on, iter, player1, player2):
    combinations = [(s, t) for s in sizes for t in timeout]
    df = pd.DataFrame(columns=['Board size', 'Timeout', 'Depth'])
    for comb in combinations:
        print(comb)
        # sys.stdout = open(os.devnull, 'w')
        s = comb[0]
        t = comb[1]
        for i in range(iter):
            p1 = player1(t, TT_on)
            game = HexGame(s, p1, player2)
            game.step([])
            df.loc[len(df)] = (s, t, p1.reached)
        # sys.stdout = sys.__stdout__
    return df


if __name__ == '__main__':
    # Players to be tested:
    # HexPlayerRandom
    # HexPlayerDijkstra
    # HexPlayerID_TT Not available

    players = [HexPlayerEnhanced, HexPlayerEnhanced]
    TT_on = [True, False]
    task = ['3_on', '3_off']
    player2 = None

    iter = 10

    timeout = list(np.arange(5, 31, 5))
    timeout.insert(0, 1)
    board_size = range(3, 7)  # range(1, 6)

    for i in range(len(TT_on)):
        df = simulate_game(board_size, timeout, TT_on[i], iter, players[i], player2)

        df['Board size'] = df['Board size'].astype(int).astype('category')
        df['Depth'] = df['Depth'].astype(int)
        print(df.head())
        # plt.yscale('log')
        # plt.ylabel('Log10 of depth')

        ax = sns.lineplot(x="Timeout", y="Depth", hue="Board size", data=df)

        plt.xticks(timeout)
        plt.xlabel('ID time threshold (s)')
        plt.ylabel('Depth reached')

        plt.savefig('time_task' + task[i] + '.png')
        plt.clf()
