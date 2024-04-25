import requests
import bs4
import hashlib
import webbrowser

CHALLENGE_URL = r"http://challenges.ringzer0team.com:10032/"
SOLUTION_URL = r"http://challenges.ringzer0team.com:10032/?r="
CHROME_PATH = r"/usr/bin/google-chrome %s"

def get_web_page_content(url: str) -> bytes:
	page: requests.models.Response = requests.get(url=url)
	return page.content

def get_web_page_soup(url: str) -> bs4.BeautifulSoup:
	return bs4.BeautifulSoup(get_web_page_content(url), "html.parser")

def get_message_to_hash(soup: bs4.BeautifulSoup) -> str:
	message_segment: str = soup.find('div', class_="message").get_text()
	return message_segment.splitlines()[2].strip()

def parse_numbers(string: str):
	first, rest = string.split("+")
	second, rest = rest.split("-")
	third, rest = rest.split("=")
	return first.strip(), second.strip(), third.strip()

if __name__ == "__main__":
	soup: bs4.BeautifulSoup = get_web_page_soup(CHALLENGE_URL)
	message: str = get_message_to_hash(soup)
	deci, hexa, bina = parse_numbers(message)
	deci, hexa, bina = int(deci), int(hexa[2:], 16), int(bina, 2)
	result = deci + hexa - bina

	''' Another option:
	message = message.replace(" 1", "0b1")
	expression = message.split("=")[0]
	result = eval(expression)
	print(f"{expression} = {result}")
	'''

	answer: str = f"{SOLUTION_URL}{result}"
	webbrowser.get(CHROME_PATH).open(answer)

