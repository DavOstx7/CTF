import re

IMAGE_FILE_PATH = "drawing.flag.svg"
FLAG_REGEX = r'id="tspan\d+">([a-zA-Z0-9{}_ ]+)<'

def get_file_content(path: str) -> str:
	with open(path) as file:
		return file.read()

if __name__ == "__main__":
	file_content = get_file_content(IMAGE_FILE_PATH)
	parts = re.findall(FLAG_REGEX, file_content)
	flag = "".join(parts).replace(' ', '')
	print(flag)
