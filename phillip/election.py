from __future__ import division
from random import random

def election_sim(p):
	return 'A' if random() < p else 'B'


def who_won(region_results_list):
	"""given a list of election results as a list
	of ['A', 'A', 'B'], this function returns the majority
	winner as 'A' or 'B'"""
	if region_results_list.count('A') > region_results_list.count('B'):
		return 'A'
	else:
		return 'B'

a_victories = 0
b_victories = 0
number_of_elections = 10000

for trials in range(number_of_elections):
	election_results = map(election_sim, [0.87, 0.65, 0.17])
	if who_won(election_results) == 'A':
		a_victories += 1
	else:
		b_victories += 1

print "probability of victory: A => {}; B => {}".format(a_victories/number_of_elections, b_victories/number_of_elections)