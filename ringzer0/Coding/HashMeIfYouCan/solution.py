import requests
import bs4
import hashlib
import webbrowser

CHALLENGE_URL = r"http://challenges.ringzer0team.com:10013/"
SOLUTION_URL = r"http://challenges.ringzer0team.com:10013/?r="
CHROME_PATH = r"/usr/bin/google-chrome %s"

def get_web_page_content(url: str) -> bytes:
	page: requests.models.Response = requests.get(url=url)
	return page.content

def get_web_page_soup(url: str) -> bs4.BeautifulSoup:
	return bs4.BeautifulSoup(get_web_page_content(url), "html.parser")

def get_message_to_hash(soup: bs4.BeautifulSoup) -> str:
	message_segment: str = soup.find('div', class_="message").get_text()
	return message_segment.splitlines()[2].strip()

if __name__ == "__main__":
	soup: bs4.BeautifulSoup = get_web_page_soup(CHALLENGE_URL)
	message_to_hash: str = get_message_to_hash(soup)
	hashed_object = hashlib.sha512(message_to_hash.encode())
	hashed_message = hashed_object.hexdigest()

	option1 = f"{SOLUTION_URL}{hashed_message}"
	# option2 = f"{SOLUTION_URL}[{hashed_message}]"

	webbrowser.get(CHROME_PATH).open(option1)

