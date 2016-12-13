paths = ['R3', 'L2', 'L2', 'R4', 'L1', 'R2', 'R3', 'R4', 'L2', 'R4', 'L2', 'L5', 'L1', 'R5', 
  'R2', 'R2', 'L1', 'R4', 'R1', 'L5', 'L3', 'R4', 'R3', 'R1', 'L1', 'L5', 'L4', 'L2', 'R5', 
  'L3', 'L4', 'R3', 'R1', 'L3', 'R1', 'L3', 'R3', 'L4', 'R2', 'R5', 'L190', 'R2', 'L3', 'R47', 
  'R4', 'L3', 'R78', 'L1', 'R3', 'R190', 'R4', 'L3', 'R4', 'R2', 'R5', 'R3', 'R4', 'R3', 'L1', 
  'L4', 'R3', 'L4', 'R1', 'L4', 'L5', 'R3', 'L3', 'L4', 'R1', 'R2', 'L4', 'L3', 'R3', 'R3', 'L2',
  'L5', 'R1', 'L4', 'L1', 'R5', 'L5', 'R1', 'R5', 'L4', 'R2', 'L2', 'R1', 'L5', 'L4', 'R4', 'R4', 
  'R3', 'R2', 'R3', 'L1', 'R4', 'R5', 'L2', 'L5', 'L4', 'L1', 'R4', 'L4', 'R4', 'L4', 'R1', 'R5', 
  'L1', 'R1', 'L5', 'R5', 'R1', 'R1', 'L3', 'L1', 'R4', 'L1', 'L4', 'L4', 'L3', 'R1', 'R4', 'R1', 
  'R1', 'R2', 'L5', 'L2', 'R4', 'L1', 'R3', 'L5', 'L2', 'R5', 'L4', 'R5', 'L5', 'R3', 'R4', 'L3', 
  'L3', 'L2', 'R2', 'L5', 'L5', 'R3', 'R4', 'R3', 'R4', 'R3', 'R1']


def next_direction(current_direction, path):
  if current_direction == 'N':
    return 'W' if path[0] == 'L' else 'E'
  elif current_direction == 'S':
    return 'E' if path[0] == 'L' else 'W'
  elif current_direction == 'E':
    return 'N' if path[0] == 'L' else 'S'
  elif current_direction == 'W':
    return 'S' if path[0] == 'L' else 'N'

def add_y(current_direction, amount):
  if current_direction == 'W' or current_direction == 'E':
    return 0
  else:
    return amount if current_direction == 'N' else amount * -1

def add_x(current_direction, amount):
  if current_direction == 'N' or current_direction == 'S':
    return 0
  else:
    return amount if current_direction == 'E' else amount * -1

def find_path():
  current_direction = 'N'
  x = 0
  y = 0

  for path in paths:
    current_direction = next_direction(current_direction, path)
    amount = int(path[1:])
    x += add_x(current_direction, amount)
    y += add_y(current_direction, amount)


  print 'x: ' + str(x) + ', y: ' + str(y) + '\n'

  print 'total: ' + str(x + y) + '\n'


if __name__ == "__main__":
  find_path()
