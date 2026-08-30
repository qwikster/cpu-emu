import proq.isa.instructions  # noqa: F401 # Have to add this to force it to run proq.isa.instructions.__init__.py n do the stuff
from proq.hw.alu import ALU
from proq.hw.mu import MU
from proq.hw.register import Registers
from proq.isa.base import Instruction
from proq.isa.set import Op
from proq.util.exceptions import InstructionNotImplementedError
from proq.util.logging import Logger
from proq.util.util import hex


class CU:
    def __init__(self, alu: ALU, mu: MU, registers: Registers, logger: Logger):
        for skipped in Instruction.skipped:
            logger.setup(f"Skipped unregistered instruction: {skipped}")

        for op in Op:
            if op.value not in Instruction.registry:
                raise InstructionNotImplementedError(f"No matching Class(Instruction) definition for {op.name} ({hex(op.value)})")

        self.alu = alu
        self.mu = mu
        self.registers = registers

        self.logger = logger

    def tick(self):
        pass
        # instruction = Instruction.registry[self.mu.read(self.registers.PC)]
        # instance = instruction(self, self.mu, self.alu, self.registers)
        # self.instruction_cycle = instance.execute()
        # [ ... (on tick) ]
        # next(self.instruction_cycle)
