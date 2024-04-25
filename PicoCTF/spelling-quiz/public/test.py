import itertools
alphabet = "abcdefghijklmnop"
print(alphabet)

for alphabet_combo in list(itertools.islice(itertools.permutations(alphabet), 5000)):
	print(alphabet_combo)