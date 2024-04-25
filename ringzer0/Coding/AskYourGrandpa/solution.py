from typing import List
import binascii

FILE_PATH = r"8c80cb5cc7b85aee2ecc5c613af111c8.zip"

def is_line_binary(line: str) -> bool:
	possible_chars = ['0', '1', ' ']
	for char in line:
		if char not in possible_chars:
			return False
	return True

def get_binary_string_from_file(file_path: str) -> str:
	with open(file_path, "r") as file_handler:
		lines = file_handler.readlines()
		for line in lines:
			line = line.strip()
			if not line:
				continue
			if is_line_binary(line):
				return line

def get_list_of_binary_strings_from_file(file_path: str) -> List[str]:
	return get_binary_string_from_file(file_path).split()

def get_ascii_list_from_binary(binary_list: List[str]) -> List[str]:
	char_list: List[str] = list()
	for code_point in binary_list:
		integer_code_point: int = int(code_point, 2)
		char_list.append(chr(integer_code_point))
	return char_list

if __name__ == "__main__":
	binary_strings: List[str] = get_list_of_binary_strings_from_file(FILE_PATH)
	char_list: List[str] = get_ascii_list_from_binary(binary_strings)
	text: str = "".join(char_list)
	print(text)

	''' Another option:
	binary_number_no_spaces: str = "".join(get_binary_string_from_file(FILE_PATH).split())
	hex_number_no_spaces = hex(int(binary_number_no_spaces, 2))[2:]
	text = binascii.unhexlify(hex_number_no_spaces).decode()
	print(text)
	'''



