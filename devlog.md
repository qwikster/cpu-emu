okay soo I started this project without picking a place to ship it and this happens to be the only program that really fits right now SO! time to devlog 6 hours of work n probs 10h of research!! :x

### devlogs
are gonna have to be really technical :pf: there's not much to screenshot so ill do my best to explain all the concepts im researching!

### processor
this is a 16 bit computer emulator! the root of something this low level is the processor. It being 16 bit means that it works with 16 bit numbers, which are 2 bytes or 4 hex: something like `0x3A33`. All the addresses it can reference and values it can store use 16 bit numbers like this. Opcodes (numbers that represent instructions) are represented in 8 bit blocks, which gives 255 unique instructions, and addresses *contain* 8 bit numbers, or one byte each.

### memory
In the 16 bit space, there are 65,536 memory addresses, ranging from `0x0000` to `0xFFFF`. The `MU()` class (Memory Unit :sho:) lets me assign and access devices on the memory modularly. First, ROM: program memory that can be loaded before execution, but not written to. then, RAM- read-writable, slower than a register (on real hardware), but can hold much more information. The last bit, from the range `0xF000` to `0xFFFF` (4KiB) is reserved for:

### MMIO
or Memory-Mapped Input/Output. The processor is useless if it can't get information or display it to a user, and this is how we do that. The processor can read information from a special memory address, then write to another one to input and output data. This is also the space where some system things can be stored, like the reset bytes or the IVT (Interrupt Vector Table). I'll explain more about those things in a later devlog.

Thanks to Python being okay at OOP, the addresses on this emulated processor can be assigned really easily:
```python
self.keyboard_device = InterruptKeyboard(intp = 0x11) # so it can be used in main.py
self.mu.map_device(0x0000, romsize - 1, ROM(size = romsize, binary = binary))
self.mu.map_device(romsize, romsize + memsize - 1, RAM(size = memsize))
self.mu.map_device(0xF000, 0xF000, StdoutOutput())
self.mu.map_device(0xF001, 0xF001, keyboard_device)
# maybe a screen? or buttons? or GPIO pins? or a nuclear bomb? :3
```
and you might do something like this (i haven't built this part yet):
```python
# print the character in the keyboard's memory to stdout
#      instruction, memory to memory, destination, source 
self.cu.opcode(MOV, 0x08, 0xF000, 0xF001)
```

### Registers
Memory is great, but in real hardware it's slow, and it's weird to assign to and work with. Registers go inside of the processor itself for a place to really quickly keep and modify small amounts of information.

the General Purpose Registers (GPRs) R1 through R12 are used for storing small amounts of information between instructions. There's also the PC, or the Program Counter, which stores the memory address of the current instruction; the `IR`, instruction register, which stores the current opcode; and the SP, which points to a location in memory where the stack currently is, used for functions and interrupts.

Finally, a flags register, encoding single bits important for math instructions that I'll explain later.

### CU, ALU, and the rest of the stuff
Okay so I haven't mentioned a lot of stuff that I've worked on or that need to be considered- i'll explain them in the future. Right now, I'm working on how the processor actually performs instructions, and I'll write about that when the time comes :)

### Goog... :goog:
hopefully this is uh, somewhat educational and doesn't just read as a rant!! the devlogs that Don't take 6 hours are to be a lot more digestible but until then time to go back to OOP hell :droidtehe: also this is like full character limit lmao
