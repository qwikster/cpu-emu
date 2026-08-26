class MU:
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

        # todo: hardware memory addresses, proper stack, proper heap, safeties
