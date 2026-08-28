from enum import Enum

from proq.hw.alu import ALU
from proq.hw.cu import CU
from proq.hw.mu import MU, RAM, ROM, StdoutOutput
from proq.hw.register import Registers
from proq.util.exceptions import EmulatorMemoryError
from proq.util.logging import Logger

MAX_MEMORY = 61440

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
        memsize: int = 4096,  # 4K
        romsize: int = 57344, # 56K
        flag_debug: bool = False,
    ):
        self.log = logger

        self.state = CPUState.FETCH # part of instruction
        self.processor_cycle = 0    # global count
        self.instruction_cycle = 0  # per instruction EXECUTE (long ones)

        self.interrupt = 0 # hardware interrupt line

        # Memory
        self.mu = MU(self.log)
        if memsize + romsize > MAX_MEMORY:
            raise EmulatorMemoryError(f"Assigning more RAM/ROM than is available (max: {hex(MAX_MEMORY)}, used: {hex(memsize + romsize)}")

        self.mu.map_device(0x0000, romsize - 1, ROM(size = romsize, binary = binary))
        self.mu.map_device(romsize, romsize + memsize - 1, RAM(size = memsize))
        self.mu.map_device(0xF000, 0xF000, StdoutOutput())

        # Registers
        self.reg = Registers(self.log, stack_addr = romsize + memsize - 1, debug = flag_debug)

        # Instructions
        self.alu = ALU()
        self.cu = CU(self.reg, self.mu)

    def tick(self):
        self.cu.tick()
        self.processor_cycle += 1
        if self.reg[0] >= 0x0E:
            self.log.interrupt("HALT")
            input()
        self.mu.write(0xF000, self.mu.read(self.reg[0]))
        self.reg[0] += 1
