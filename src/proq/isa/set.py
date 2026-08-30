from enum import IntEnum


# centralized operation definitions
class Op(IntEnum):
    # NOP = 0x00

    ADD = 0x10
    SUB = 0x11

    # HALT = 0xF0
    # MKINTP = 0xF1
    # UNINTP = 0xF2
    # RMINTP = 0xF3
