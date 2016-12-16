
def is_aba(line):
  curr_index = 0
  next_index = 0
  valid_strings = []
  invalid_strings = []

  while curr_index < len(line):
    next_index = line.find('[', curr_index)
    if next_index == -1: 
      next_index = len(line)
    
    # if it isnt at least 4 we don't care
    if next_index - curr_index > 4:
      valid_strings.append(line[curr_index:next_index])

    # if we are at the end then we are done
    curr_index = next_index + 1
    if curr_index < len(line):
      next_index = line.find(']', curr_index)
      invalid_strings.append(line[curr_index:next_index])
      curr_index = next_index + 1

  for invalid_str in invalid_strings:
    if check_string(invalid_str):
      return False

  for valid_str in valid_strings:
    if check_string(valid_str):
      return True

  return False
    

def check_string(s):
 
  index = 0
  max_index = len(s) - 4

  while index <= max_index:
    c1 = s[index]
    c2 = s[index + 1]
    c3 = s[index + 2]
    c4 = s[index + 3]
    index += 1

    if c1 == c4 and c2 == c3 and c1 != c2:
      return True

    
   
  return False

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
