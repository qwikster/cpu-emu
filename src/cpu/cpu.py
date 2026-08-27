from enum import Enum

from cpu.alu import ALU
from cpu.cu import CU
from cpu.logging import Logger
from cpu.mu import MU, StdoutOutput
from cpu.register import Register

import random


class CPUState(Enum):
    FETCH =     "fetch"
    DECODE =    "dec"
    EXECUTE =   "exec"
    WRITEBACK = "wb"

class CPU:
    def __init__(
        self,
        binary: bytes,
        logger: Logger,
        memsize: int = 512,
        romsize: int = 2048,
        flag_debug: bool = False,
    ):
        self.log = logger

        self.state = CPUState.FETCH
        self.processor_cycle = 0   # global count
        self.instruction_cycle = 0 # per instruction EXECUTE (long ones)

        self.interrupt = 0 # hardware interrupt line

        self.alu = ALU()  # Arithmetic
        self.mu = MU(self.log) # Memory
        self.register = Register(stack = memsize, debug = flag_debug)
        self.cu = CU(self.register, self.mu)   # Control (opcodes)

        self.mu.map_device(0xF000, 0xF000, StdoutOutput())

    def tick(self):
        self.mu.write(0xF000, random.randint(0, 255))
