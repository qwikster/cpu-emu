from dataclasses import dataclass, field

from cpu.logging import Logger

_hex = hex
def hex(int) -> str:
    goob = _hex(int).upper()
    if goob == "0X0":
        return "0x0000"
    return goob[0] + "x" + goob[2:]

@dataclass
class Flags:
    ZF: bool = False # Zero flag
    CF: bool = False # Carry
    SF: bool = False # Sign
    OF: bool = False # Overflow
    IF: bool = False # enable interrupts
    TF: bool = False # Trap / Debug

@dataclass
class Registers:
    log: Logger

    stack_addr: int
    debug: bool = False

    PC: int = 0x0000 # program counter
    IR: int = 0x00   # instruction register
    SP: int = 0x0000 # stack pointer
    flags: Flags = field(default_factory=Flags)
    GPR: list[int] = field(default_factory=lambda: [0x0000] * 12) # general purpose registers

    def __post_init__(self):
        self.SP = self.stack_addr
        self.flags.TF = self.debug
        self.log.setup(f"Set up registers: PC {hex(self.PC)} | SP {hex(self.SP)} | IR {hex(self.IR)}")
        self.log.setup(f"GPR 1 thru 12: {self.GPR}")
        self.log.setup(f"{self.flags}")

    # cpu.registers[3] = 0x1234
    def __getitem__(self, idx: int) -> int:
        self.log.register(f"Read {self.GPR[idx]} from R{idx + 1}")
        return self.GPR[idx]

    def __setitem__(self, idx: int, value: int):
        self.GPR[idx] = value & 0xFFFF
        self.log.register(f"Wrote {value} to R{idx + 1}")
