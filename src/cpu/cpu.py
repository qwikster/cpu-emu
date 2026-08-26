from types import SimpleNamespace

from cpu.alu import ALU
from cpu.cu import CU


class CPU:
    def __init__(
        self,
        memsize: int = 512,
        romsize: int = 2048,
        binary: list[int] | None = None,
        flag_debug: bool = False

    ):
        if binary is None:
            binary = []

        self.rom_start = memsize
        self.memory = [0x00] * (memsize + romsize)

        for i, byte in enumerate(binary):
            if i < romsize:
                self.memory[self.rom_start + i] = byte

        registers_dict = {
            "PC": 0x0000, # next instruction,
            "IR": 0x00, # current opcode
            "flags": {
                "ZF": False, # Zero flag
                "CF": False, # Carry
                "SF": False, # Sign
                "OF": False, # Overflow
                "TF": flag_debug, # Trap / Debug
            },
            "registers": [0x00] * 12
        }

        self.registers = SimpleNamespace(**registers_dict)

        self.interrupt = 0x0000
        self.HALT = False

        self.CU = CU()   # Control (opcodes)
        self.ALU = ALU() # Arithmetic

    def cycle(self):
        pass
