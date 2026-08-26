import argparse

from cpu.cpu import CPU


def entry():
    parser = argparse.ArgumentParser(description="shitass cpu emulator")
    parser.add_argument("binary", type=str, help = "machine code to run")
    parser.add_argument("--memsize", "--mem", "-m", type=int, default = 512, help = "size of RAM in bytes")
    parser.add_argument("--romsize", "--rom", "-r", type=int, default = 4096, help = "size of ROM in bytes")

    args = parser.parse_args()
    cpu = CPU(args.memsize, args.romsize)

    while not cpu.HALT:
        cpu.cycle()
