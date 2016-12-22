import Queue as Q  

def print_grid(grid):
  f = open('output26.dat','w');

  for row in grid:
    for c in row:
      v = '# ' 
      if c:
        v = '. '
      f.write(v)

    f.write('\n')


def is_open(x, y):
  seed = 1362
  val = x*x + 3*x + 2*x*y + y + y*y
  val += seed
  ones = bin(val).count('1')

  return ones % 2 == 0

def create_grid():
  x_max = 50
  y_max = 50

  rows = []
  y = 0

  while  y < y_max:
    x = 0
    row = []
    while x < x_max:
      row.append(is_open(x, y))

      x += 1

    y += 1

    print row
    rows.append(row)


  return rows


class State:
  def __init__(self, moves, x, y):
    self.moves = moves
    self.x = x
    self.y = y
    self.dist = x + y 
    self.key = 'x:' + str(x) + ',y:' + str(y)

  def move(self, x_move, y_move):
    return State(self.moves + 1, self.x + x_move, self.y + y_move)

  def __cmp__(self, other):
    res = cmp(self.dist, other.dist)

    if res == 0:
      return cmp(self.moves, other.moves)

    return res


def add_state(state, q, used_paths):
  if used_paths.get(state.key, 1000000) > state.moves: 
    q.put(state)
    used_paths[state.key] = state.moves


def find_path(grid):
  min_moves = 100000000
  x_max = 49
  y_max = 49

  used_paths = {
    'x:31,y:39': 0
  }


  q = Q.PriorityQueue()

  q.put(State(0, 31, 39))

  while not q.empty():
    state = q.get()
    x = state.x
    y = state.y

    print 'x: ' + str(x) + ', y: ' + str(y)
    if state.moves < min_moves:

      if x == 1 and y == 1:
        min_moves = state.moves
        continue

      # try up 
      if y > 0 and grid[y - 1][x]:
        add_state(state.move(0, -1), q, used_paths)

      # try left
      if x > 0 and grid[y][x - 1]:
        add_state(state.move(-1, 0), q, used_paths)

      # try right
      if x < x_max and grid[y][ x + 1]:
        add_state(state.move(1, 0), q, used_paths)

      # try down
      if y < y_max and grid[y + 1][x]:
        add_state(state.move(0,1), q, used_paths)

  print min_moves


if __name__ == "__main__":
  grid = create_grid()
  print_grid(grid)

  find_path(grid)

