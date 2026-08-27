from enum import Enum
from types import SimpleNamespace

from cpu.alu import ALU
from cpu.cu import CU
from cpu.mu import MU
from cpu.register import Register


class CPUState(Enum):
    FETCH =     "fetch"
    DECODE =    "dec"
    EXECUTE =   "exec"
    WRITEBACK = "wb"

class CPU:
    def __init__(
        self,
        debug_settings: SimpleNamespace,
        binary: bytes,
        memsize: int = 512,
        romsize: int = 2048,
        flag_debug: bool = False,
    ):
        self.debug = debug_settings



        self.state = CPUState.FETCH
        self.processor_cycle = 0   # global count
        self.instruction_cycle = 0 # per instruction EXECUTE (long ones)

        self.interrupt = 0 # hardware interrupt line

        self.alu = ALU()  # Arithmetic
        self.mu = MU(self.debug) # Memory
        self.register = Register(stack = memsize, debug = flag_debug)
        self.cu = CU(self.register, self.mu)   # Control (opcodes)

    def tick(self):
        pass
