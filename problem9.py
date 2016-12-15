import md5

puzzle_input = 'ffykfhsq'

def get_hash(index):
  return md5.new(puzzle_input + str(index)).hexdigest()

def get_code():
  index = 0
  current_code = []

  while len(current_code) < 8:
    hash_code = get_hash(index)
    index += 1

    # print index
    # print current_code
    # print hash_code[:5]

    if hash_code[:5] == '00000':
      current_code.append(hash_code[5])

  print ''.join(current_code)



if __name__ == "__main__":
  get_code()
