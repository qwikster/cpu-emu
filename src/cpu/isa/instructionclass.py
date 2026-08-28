from cpu.mu import MU
from cpu.register import Registers


class Instruction:
    def execute(self, mu: MU, registers: Registers, operands: list[int]):
        pass

    def length(self):
        pass
