from __future__ import division
from random import randint

all_dice_rolls = 0
num_of_trials = 10000

for trials in range(0, num_of_trials):
	this_roll = randint(1, 6)
	all_dice_rolls += this_roll

print "average dice roll = {}".format(all_dice_rolls/num_of_trials)