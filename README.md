# 8-BIT-TTL-CPU
Step by step documentation of building a `8 bit TTL CPU` from **74xx** logic chips.

![cpu8bit](https://github.com/YashIndane/8-BIT-TTL-CPU/assets/53041219/f67a7bfb-0adb-4b5d-b1a2-f94aeea5fe68)

## Story

Usually for beginners or non-technical guys, its hard to understand how a CPU operates and executes the program. 

There should be a way to understand on how a basic how individual instructions are executed, which gives a fair bit of idea to us. So I decided to make a CPU on breadboards, using 74 series TTL logic chips which are easy to find.

I decided to make a 8 bit CPU that just runs on some Hz frequency (Not GHZ as we want to see what it does), which will help understanding fundamentals of CPU Operations.

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

# CPU Modules

![image](https://github.com/user-attachments/assets/59a3a1da-c59a-4629-928a-780586bfe753)

![image](https://github.com/user-attachments/assets/d96afba4-e87f-4277-bf62-599c0e1126d7)

![image](https://github.com/user-attachments/assets/73b313e4-c2ca-47e2-b384-e4c30146b22e)

![image](https://github.com/user-attachments/assets/b2cd7761-987c-4059-94c4-66c110ba98b1)

![image](https://github.com/user-attachments/assets/785bd5b5-84e3-4bc1-8edc-4ed7fac863c1)

![image](https://github.com/user-attachments/assets/6378d678-908b-4671-a33f-8a99f69fbdfb)

![image](https://github.com/user-attachments/assets/cf809aed-987d-4dc2-a588-3112bd978758)

![image](https://github.com/user-attachments/assets/0daf68ba-2966-4ad4-bc9a-2a99baeef4db)

![image](https://github.com/user-attachments/assets/b80576a2-68b5-4375-9f80-3dc473e3803a)

## Generating machine code

Writing the machine code from assembly code manually is a tedious task. To make life easy, use the assembler.py script to do the same job quickly.

### Usage
```
python assembler.py --asmfile="<ASSEMBLY-FILE>"
```

Sample programs can be found here -> [asm-files](https://github.com/YashIndane/8-BIT-TTL-CPU/tree/main/asm-files)

## Programming the microcode EEPROMs

You can find a seperate repository with code, schematics & instructions for programming the microcode EEPROMs [here](https://github.com/YashIndane/rpi-eeprom-programmer)

## List of alterations

1. For manual clock pulse increase the value of timing capacitor. If the push button switch is switching more than once in the pulse duration, it will trigger the clock pulse more than once, for a single step. So increase the value of timing capacitor. I used ```0.44 uF``` capacitor.

2. I connected a ```1k``` resistor between select input of the ```74157s``` on the data selectors, in the RAM module.

3. Originally I used ```74273``` (Octal D-Type Flip Flop) along with a ```AND``` gate as his output register. This has some issues & it will generally latch in any value that's coming on the bus even if ```OI``` signal is not active. To solve this just simply use two ```74173s``` to make a 8 bit register (Same as A & B register).
