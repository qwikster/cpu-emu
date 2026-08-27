import argparse
from time import sleep

from cpu.cpu import CPU
from cpu.logging import Logger


def entry():
    parser = argparse.ArgumentParser(description="shitass cpu emulator")
    parser.add_argument("binary", type=str, help = "machine code to run")
    parser.add_argument("--memsize", "--mem", "-m", type=int, default = 512, help = "size of RAM in bytes")
    parser.add_argument("--romsize", "--rom", "-r", type=int, default = 4096, help = "size of ROM in bytes")

    args = parser.parse_args()

    if not args.binary:
        binary = bytes(0)
    else:
        with open(args.binary, 'rb') as f:
            binary = f.read()

    logger = Logger(default = True, setup = True)
    logger.setup("logger started")

    cpu = CPU(
        binary = binary,
        logger = logger,
        memsize = args.memsize,
        romsize = args.romsize,
    )

    logger.setup("starting CPU")

    while True:
        check_io(cpu)
        cpu.tick()
        sleep(0.1)

def check_io(cpu: CPU):
    pass # check keyboard and display to screen here
