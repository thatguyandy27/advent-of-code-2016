import md5

puzzle_input = 'ffykfhsq'

def get_hash(index):
  return md5.new(puzzle_input + str(index)).hexdigest()

def get_code():
  index = 0
  current_code = ['0','0','0','0','0','0','0','0']
  codes = set()

  while len(codes) < 8:
    hash_code = get_hash(index)
    index += 1


    if hash_code[:5] == '00000':
      position = ord(hash_code[5]) - 48

      if position < 8 and position >= 0. and (not position in codes):
        print position
        print hash_code[6]
        current_code[position] = hash_code[6]
        codes.add(position)
        

  print ''.join(current_code)



if __name__ == "__main__":
  get_code()
