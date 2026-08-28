_hex = hex
def hex(val: int) -> str:
    sign = "-" if val < 0 else ""
    return f"{sign}0x{abs(val):04X}"
