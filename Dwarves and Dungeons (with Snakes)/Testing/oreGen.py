"""
Generate and place ores
"""
import random as rng
rng.seed(rng.randint(0, 1000))
redFG = "\033[31m"
greenFG = "\033[32m"
yellowFG = "\033[33m"
blueFG = "\033[34m"
purpleFG = "\033[35m"
greyFG = "\033[37m"

stone = 5
ores = {"iron":[redFG,25], "gold":[yellowFG, 10], "silver":[greyFG, 15], "copper":[greenFG, 50], "lapis":[purpleFG, 15]}
def oreMap(maxX, maxY):
    try:
        oreAmount = round(maxX * maxY / 100 * (100-stone))
        oresPerc = 0
        map = [[''] * maxY for _ in range(maxX)]
        for values in ores:
            oresPerc += ores[values][1]

        for ore in ores.values():
            amount = round(oreAmount / (ore[1]*100 / oresPerc))
            x = rng.randint(0, maxX - 1)
            y = rng.randint(0, maxY - 1)
            while (amount > 0):
                """
                Place Bitboard for color checking
                here could also be your ad
                """
                if map[x][y] == '':
                    map[x][y] = ore[0]
                    amount -= 1

                stuff = rng.randint(-1, 1)
                x += stuff
                stuff = rng.randint(-1, 1)
                y += stuff

                if x < 0 or x > maxX - 1 or y < 0 or y > maxY - 1:
                    flag = 1
                else:
                    flag = rng.randint(ore[1] * - 1, 1)

                if flag < 0:
                    flag = 0

                if flag:
                    x = rng.randint(0,maxX - 1)
                    y = rng.randint(0,maxY - 1)
                    continue

    except:
        print("maxX: ", maxX)
        print("maxY: ", maxY)
        print("total area: ", maxX * maxY)
        print("stone: ", stone)
        print("oreAmount: ", oreAmount)
        print("oresPerc: ", oresPerc)
        print("ore perc: ", ore[1])
        print("percentage: ", (oresPerc/ ore[1]))
        print(amount)
        print(flag)
        print(stuff)
        print(ore)

    print("maxX: ", maxX)
    print("maxY: ", maxY)
    print("total area: ", maxX * maxY)
    print("stone: ", stone)
    print("oreAmount: ", oreAmount)
    print("oresPerc: ", oresPerc)
    print("ore perc: ", ore[1])
    print("percentage: ", (oresPerc/ ore[1]))
    print(amount)
    print(flag)
    print(stuff)
    print(ore)
    return map 