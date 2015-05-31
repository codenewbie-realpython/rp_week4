from __future__ import division
from random import randint

number_of_trials = 10000
flips = 0

for trials in range(number_of_trials):
    tally_list = []
    while True:
        flips += 1
        tally_list.append(randint(0, 1))
        if 0 in tally_list and 1 in tally_list:
            break

print "The average number of flips to get both heads and tails is {}".format(flips/number_of_trials)
