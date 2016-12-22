
def get_instructions():
  return [line.rstrip('\n') for line in open('day12.dat')]

def copy_from(registers, r_to, r_from):
  copy_val(registers, r_to, registers[r_from])

def copy_val(registers, register,  value):
  registers[register] = int(value)

def get_jmp_dist(registers, reg_chk, jmp_dis):

  if registers[reg_chk] == 0:
    return 1
  else:
    return jmp_dis


def execute_instructions():
  registers = {
    'a': 0,
    'b': 0,
    'c': 1,
    'd': 0
  }  

  instructions = get_instructions()
  index = 0

  while index < len(instructions):
    instruction = instructions[index]
    sp = instruction.split(' ')

    if sp[0] == 'cpy':
      val = sp[1]
      reg_to = sp[2]

      if val.isdigit():
        copy_val(registers, reg_to, val)
      else:
        copy_from(registers, reg_to, val)

      index += 1

    elif sp[0] == 'inc':
      reg_to = sp[1]
      registers[reg_to] += 1

      index += 1

    elif sp[0] == 'dec':
      reg_to = sp[1]
      registers[reg_to] -= 1

      index += 1

    elif sp[0] == 'jnz':

      if sp[1].isdigit():
        if int(sp[1]) == 0:
          index += 1
        else:
          index += int(sp[2])

      else:
        reg_chk = sp[1]
        jmp_dis = int(sp[2])

        index += get_jmp_dist(registers, reg_chk, jmp_dis)  


    print registers

  print registers['a']

if __name__ == "__main__":
  execute_instructions()