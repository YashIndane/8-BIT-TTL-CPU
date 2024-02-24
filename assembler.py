# Machine code generator for the 8 BIT Breadboard CPU
# Usage -
# python assembler.py --asmfile="<ASM-FILE>"
#
#
# Author - Yash Indane
# Email  - yashindane46@gmail.com
# License - Apache License 2.0


import argparse


def hex_to_bin(hex_data:str) -> str:
    scale = 16
    bit_length = 4*(len(hex_data) -2)
    bin_data = bin(int(hex_data, scale))[2:].zfill(bit_length)
    return bin_data


def addr_data_builder(a:list) -> tuple:

    length = len(a)
    addr = hex_to_bin(a[0])

    if length<3:
        if a[1] in ["nop", "out", "hlt"]:
            data = opcode_bin_map[a[1]] + "0000"
        else:
            data = hex_to_bin(a[1])
    else:
        data = opcode_bin_map[a[1]] + hex_to_bin(a[2])

    return (addr, data)


if __name__ == "__main__":
  
  #Parsing args
  parser = argparse.ArgumentParser()
  parser.add_argument("--asmfile", required=True, type=str, help="Assembly file")
  args = parser.parse_args()
  asm_file = args.asmfile

  opcode_bin_map = {
    "nop": "0000",
    "lda": "0001",
    "add": "0010",
    "sub": "0011",
    "sta": "0100",
    "ldi": "0101",
    "jmp": "0110",
    "jc" : "0111",
    "jz" : "1000",
    "out": "1110",
    "hlt": "1111"
  }
   
  assembly_file = open(asm_file)

  for line in assembly_file:
      splitted = line.replace("\n", "").split(" ")
      splitted_filtered = [term for term in splitted if term != ""]
      addr, data = addr_data_builder(splitted_filtered)
      print(addr, data)

  assembly_file.close()