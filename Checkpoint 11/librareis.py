# import random

# cion = random.choice(["heads","tails"])
# print(cion)

# number = random.randint(1,10)
# print(number)

# cards = ["jack", "queen","king","Ace"]
# random.shuffle(cards)
# for card in cards:
#     print(card)

# import statistics
# print(statistics.mean([100,90]))

# import statistics
# import sys
# print(statistics.mean([int(sys.argv[1]),int(sys.argv[2])]))

import sys
import cowsay
try:
    print("Hello, my name is", sys.argv[1])
except IndexError:
    # print("Toofew arguments")
    sys.exit()

