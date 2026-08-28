from proq.hw.mu import MU
from proq.hw.register import Registers


class Instruction:
    def execute(self, mu: MU, registers: Registers, operands: list[int]):
        pass

    def length(self):
        pass
