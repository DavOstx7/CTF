from rail_fence import RailFence

def get_message() -> str:
	with open("./message.txt") as f:
		return f.read()

def extract_flag(decoded_message: str) -> str:
	_, flag = decoded_message.split("is: ")
	return flag
rail_fence = RailFence(4)
decoded_message = rail_fence.decrypt(get_message())
print(f"The decoded message is: '{decoded_message}'")
flag = "picoCTF" + '{' + extract_flag(decoded_message) + '}'
print(flag)
