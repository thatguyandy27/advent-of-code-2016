
def is_aba(line):
  curr_index = 0
  next_index = 0
  external_strings = []
  internal_strings = []
  external_abas = []
  internal_abas = []

  while curr_index < len(line):
    next_index = line.find('[', curr_index)
    if next_index == -1: 
      next_index = len(line)
    
    # if it isnt at least 4 we don't care
    if next_index - curr_index > 3:
      external_strings.append(line[curr_index:next_index])

    # if we are at the end then we are done
    curr_index = next_index + 1
    if curr_index < len(line):
      next_index = line.find(']', curr_index)
      internal_strings.append(line[curr_index:next_index])
      curr_index = next_index + 1

  for internal in internal_strings:
    internal_abas.extend(find_aba(internal))

  for external in external_strings:
    external_abas.extend(find_aba(external))

  return match_abas(internal_abas, external_abas)

def match_abas(internals, externals):
  for internal in internals:
    swapped_int = internal[1] + internal[0] + internal[1]

    if swapped_int in externals:
      return True

  return False

def find_aba(s):
  index = 0
  max_index = len(s) - 3
  abas = []

  while index <= max_index:
    c1 = s[index]
    c2 = s[index + 1]
    c3 = s[index + 2]
    index += 1

    if c1 == c3 and c2 != c1:
      abas.append(c1 + c2 + c3)
   
  return abas

def get_count():
  f = open('problem13.dat', 'r')
  count = 0

  for line in f:
    if is_aba(line):
      print line

      count += 1


  print count


if __name__ == "__main__":
  get_count()
