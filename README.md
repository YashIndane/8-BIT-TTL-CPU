# 8-BIT-TTL-CPU
Step by step documentation of building a `8 bit TTL CPU` from **74xx** logic chips.

![cpu8bit](https://github.com/YashIndane/8-BIT-TTL-CPU/assets/53041219/f67a7bfb-0adb-4b5d-b1a2-f94aeea5fe68)

## The architecture

The SAP-1 computer is a bus-organized computer and makes use of Von-Neumann architecture. It makes use of an 8-bit central bus and has ten main components. A pictorial representation of its architecture is shown below.

![sap1](https://github.com/YashIndane/8-BIT-TTL-CPU/assets/53041219/2bd9e97f-3501-4db6-a8cf-751ad2ebf2c7)


## The instruction set

This CPU supports 4 bit instructions, which are the following -

| INS       | OPCODE |  OPERATION |
|-----------|--------|------------|
| ***NOP*** | `0x0` | No operation |
| ***LDA*** | `0x1` | Copy content from RAM at the address to A reg. |
| ***ADD*** | `0x2` | Add content of RAM at the address to A reg and store in A reg |
| ***SUB*** | `0x3` | Subtract content of RAM at the address to A reg and store in A reg |
| ***STA*** | `0x4` | Store content of A reg in RAM at the address |
| ***LDI*** | `0x5` | Load A reg immediatly with the 4 bit value |
| ***JMP*** | `0x6` | Jump to the address |
| ***JC***  | `0x7` | Jump to the address if carry flag set |
| ***JZ***  | `0x8` | Jump to the address if zero flag set |
| --        | `0x9` | -- |
| --        | `0xa` | -- |
| --        | `0xb` | -- |
| --        | `0xc` | -- |
| --        | `0xd` | -- |
| ***OUT*** | `0xe` | Copy content from A reg to Output reg |
| ***HLT*** | `0xf` | Halt the CPU |

## Generating machine code

Writing the machine code from assembly code manually is a tedious task. To make life easy, use the assembler.py script to do the same job quickly.

### Usage
```
python assembler.py --asmfile="<ASSEMBLY-FILE>"
```

Sample programs can be found here -> [asm-files](https://github.com/YashIndane/8-BIT-TTL-CPU/tree/main/asm-files)

## Programming the microcode EEPROMs

You can find a seperate repository with code, schematics & instructions for programming the microcode EEPROMs [here](https://github.com/YashIndane/rpi-eeprom-programmer)

## List of alterations from Ben Eater's design

1. For manual clock pulse increase the value of timing capacitor. If the push button switch is switching more than once in the pulse duration, it will trigger the clock pulse more than once, for a single step. So increase the value of timing capacitor. I used ```0.44 uF``` capacitor.

2. I connected a ```1k``` resistor between select input of the ```74157s``` on the data selectors, in the RAM module.

3. Ben used ```74273``` (Octal D-Type Flip Flop) along with a ```AND``` gate as his output register. This has some issues & it will generally latch in any value that's coming on the bus even if ```OI``` signal is not active. To solve this just simply use two ```74173s``` to make a 8 bit register (Same as A & B register).
