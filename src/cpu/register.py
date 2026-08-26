from types import SimpleNamespace


class Register:
    def __init__(self, stack: int, debug: bool = False):
        registers_dict = {
            "PC": 0x0000, # next instruction
            "IR": 0x00, # current opcode
            "SP": stack, # stack memory address
            "flags": {
                "ZF": False, # Zero flag
                "CF": False, # Carry
                "SF": False, # Sign
                "OF": False, # Overflow
                "IF": False, # enable interrupts
                "TF": debug, # Trap / Debug
            },
            "registers": [0x00] * 12
        }

        self.registers = SimpleNamespace(**registers_dict)
