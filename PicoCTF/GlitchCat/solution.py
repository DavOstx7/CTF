import subprocess

GLITCHED_FLAG_COMMAND = "nc saturn.picoctf.net 53933"

# Need to run from shell and press enter
print("Press enter!")
output = subprocess.check_output(GLITCHED_FLAG_COMMAND, shell=True).decode()
print(f"Current flag: {output}")
evaled_output = eval(output)
print(f"Flag after eval: {evaled_output}")