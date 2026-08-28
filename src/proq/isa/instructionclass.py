from proq.mu import MU
from proq.register import Registers


class Instruction:
    def execute(self, mu: MU, registers: Registers, operands: list[int]):
        pass

    def length(self):
        pass
