import argparse
from types import SimpleNamespace

from cpu.cpu import CPU
from cpu.debug import Debug

debug_settings_dict = {
    "setup": True,
    "memory": True,
}

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

    debug = Debug(SimpleNamespace(**debug_settings_dict))

    cpu = CPU(
        binary = binary,
        memsize = args.memsize,
        romsize = args.romsize,
        debug_settings = debug_settings
    )

    while True:
        check_io(cpu)
        cpu.tick()

def check_io(cpu: CPU):
    pass # check keyboard and display to screen here
