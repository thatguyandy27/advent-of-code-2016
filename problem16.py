
def get_grid(): 
  grid = []
  for y in range(6):

    row = []
    grid.append(row)
    
    for x in range(50):
      row.append(False)


  return grid

def execute_rect(rect, grid):
  split = rect.split('x')

  x_max = int(split[0])
  y_max = int(split[1])

  for y in range(y_max):
    for x in range(x_max):
      grid[y][x] = True


def rotate_row(row, length, grid):
  grid_row = grid[row]
  row_len = len(grid_row)
  count = 0

  while count < length:
    temp = grid_row[-1]

    for n in range(row_len - 1):
      grid_row[-1 - n] = grid_row[-2 - n]

    grid_row[0] = temp

    count +=1


def rotate_column(column, length, grid): 
  colum_len = len(grid)
  count = 0

  while count < length:
    temp = grid[-1][column]
    for n in range(colum_len - 1):
      grid[-1 - n][column] = grid[-2 - n][column]

    grid[0][column] = temp

    count += 1


def execute_command(command, grid):
  parse = command.split(' ')

  if parse[0] == 'rect':
    execute_rect(parse[1], grid)
  elif parse[1] == 'row':
    rotate_row(int(parse[2].split('=')[1]), int(parse[4]), grid)
  elif parse[1] == 'column':
    rotate_column(int(parse[2].split('=')[1]), int(parse[4]), grid)
  else:
    print 'You done messed up: ' + command

def print_grid(grid):

  print '----------------------------------------------------'
  for row in grid:
    l = []
    for x in row:
      if x:
        l.append('*')
      else:
        l.append(' ')

    print ' '.join(l)

  print '----------------------------------------------------'


def get_count():
  f = open('day8.dat', 'r')
  grid = get_grid()
  count = 0

  for command in f:
    execute_command(command, grid)
    print_grid(grid)


  for row in grid:
    for x in row:
      if x:
        count += 1 


  print count

if __name__ == "__main__":
  get_count()