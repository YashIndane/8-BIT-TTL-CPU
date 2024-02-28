# 8-BIT-TTL-CPU
Step by step documentation of building a `8 bit TTL CPU` from **74xx** logic chips.

## Generating Machine Code

Writing the machine code from assembly code manually is a tedious task. To make life easy, use the assembler.py script to do the same job quickly.

### Usage
```
python assembler.py --asmfile="<ASSEMBLY-FILE>"
```

Sample programs can be found here -> [asm-files](https://github.com/YashIndane/8-BIT-TTL-CPU/tree/main/asm-files)

## List of alterations from the Ben Eater design-

1. For manual clock pulse increase the value of timing capacitor. If the push button switch is switching more than once in the pulse duration, it will trigger the clock pulse more than once, for a single step. So increase the value of timing capacitor. I used ```0.44 uF``` capacitor.

2. I connected a ```1k``` resistor between select input of the ```74157s``` on the data selectors, in the RAM module.

3. Ben used ```74273``` (Octal D-Type Flip Flop) along with a ```AND``` gate as his output register. This has some issues & it will generally latch in any value that's coming on the bus even if ```OI``` signal is not active. To solve this just simply use two ```74173s``` to make a 8 bit register (Same as A & B register).
