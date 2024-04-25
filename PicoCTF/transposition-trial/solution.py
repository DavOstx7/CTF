import itertools
from typing import List


def get_scrambled_flag():
	with open("./message.txt") as f:
		return f.read()

def get_three_piece_flag(scrambled_flag: str) -> List[str]:
	three_piece_flag = []
	for i in range(0, len(scrambled_flag), 3):
		three_piece_flag.append(scrambled_flag[i:i+3])
	return three_piece_flag

def check_for_correct_flag(flag: str) -> bool:
	return 'picoCTF{' in flag and len(flag.split[0]) == 3

def main():
	scrambled_flag = get_scrambled_flag()
	three_piece_flag = get_three_piece_flag(scrambled_flag)
	# print(three_piece_flag) - from this wee see that it's the same pattern on each piece of 3 chars
	flag = ''.join([piece[-1] + piece[:-1] for piece in three_piece_flag])
	print(flag)

if __name__ == "__main__":
	main()