from collections import deque
import copy
import json


max_floor = 3
MIN_MOVES = 41
USED_STATES = {}
f = open('output.txt','w');

def add_to_queue(state, state_queue):
  global USED_STATES
  # global f

  key = state.get_key()
  if not key in USED_STATES:
    state_queue.append(state)
    USED_STATES[key] = state.moves
  elif USED_STATES[key] > state.moves:
    state_queue.append(state)
    USED_STATES[key] = state.moves


  # else:
    # print 'key added: ' + key

class State:
  def __init__(self, floors, moves, floor_num):
    self.floors = floors
    self.moves = moves
    self.floor_num = floor_num

  def is_valid(self):
    if len(self.current_floor().chips) == 0:
      return False

    for floor in self.floors:
      if not floor.is_valid():
        return False

    return True

  def toJSON(self):
    return json.dumps(self, default=lambda o: o.__dict__,sort_keys=True, indent=2)

  def current_floor(self):
    return self.floors[self.floor_num]

  def is_solution(self):
    all_generators = len(self.floors[3].generators) == 5
    # if all_generators:
      # print 'ALL GENERATORS!'
    all_chips = len(self.floors[3].chips) == 5 

    # if all_chips:
      # print 'ALL CHIPS!'

    return all_chips and all_generators
    

  def get_key(self):
    floor_keys = []

    for floor in self.floors:
      floor.generators.sort()
      floor.chips.sort()
      floor_keys.append('g:' + ','.join(floor.generators) + 'c:' + ','.join(floor.chips))

    return str(self.floor_num) + '.' + '|'.join(floor_keys)

class Floor:
  def __init__(self, num, chips, generators):
    self.num = num
    self.chips = chips
    self.generators = generators

  def is_valid(self):
    for chip in self.chips:
      safe_generator = False
      unsafe_generator = False
      for generator in self.generators:
        if generator == chip:
          safe_generator = True
          break

        if generator != chip:
          unsafe_generator = True

      if unsafe_generator and not safe_generator:
        return False

    return True


floors = [
  Floor(0, ['pr'], ['pr']),
  Floor(1, [], ['co', 'cu', 'ru', 'pl']),
  Floor(2, ['co', 'cu', 'ru', 'pl'], []),
  Floor(3, [], [])
]

initial_state = State(floors, 0, 0)

def copy_state(state):
  return copy.deepcopy(state)

def move_generator(old_state, id, up):

  state = copy_state(old_state)

  current_floor = state.current_floor()
  if up:
    state.floor_num += 1
  else:
    state.floor_num -= 1


  # print state.floor_num

  next_floor = state.floors[state.floor_num]

  for generator in current_floor.generators:
    if generator == id:
      next_floor.generators.append(generator)
      current_floor.generators.remove(generator)

      break;

  for chip in current_floor.chips:
    if chip == id:
      next_floor.chips.append(chip)
      current_floor.chips.remove(chip)
      break;  

  state.moves += 1

  return state


def move_chips(old_state, id1, id2, up):
  state = copy_state(old_state)

  current_floor = state.current_floor()
  if up:
    state.floor_num += 1
  else:
    state.floor_num -= 1

  next_floor = state.floors[state.floor_num]

  for chip in current_floor.chips:
    if chip == id1:
      next_floor.chips.append(chip)
      current_floor.chips.remove(chip)  
      break

  for chip in current_floor.chips:
    if chip == id2:
      next_floor.chips.append(chip)
      current_floor.chips.remove(chip)  
      break

  state.moves += 1

  return state

def move_generators(old_state, state_queue, g1, g2, is_up):
  state = copy_state(old_state)

  current_floor = state.current_floor()
  if is_up:
    state.floor_num += 1
  else:
    state.floor_num -= 1

  next_floor = state.floors[state.floor_num]

  for gen in current_floor.generators:
    if gen == g1:
      next_floor.generators.append(gen)
      current_floor.generators.remove(gen)  
      break

  for gen in current_floor.generators:
    if gen == g2:
      next_floor.generators.append(gen)
      current_floor.generators.remove(gen)  
      break

  state.moves += 1

  return state


def move_chip(old_state, id1, up):
  state = copy_state(old_state)

  current_floor = state.current_floor()
  if up:
    state.floor_num += 1
  else:
    state.floor_num -= 1

  next_floor = state.floors[state.floor_num]

  for chip in current_floor.chips:
    if chip == id1:
      next_floor.chips.append(chip)
      current_floor.chips.remove(chip)
      break;  

  state.moves += 1

  return state

def try_two_generator_move(state, state_queue, is_up):
  global MIN_MOVES

  is_complete = False
  current_floor = state.current_floor()

  for g1 in current_floor.generators:
    for g2 in current_floor.generators:

      if g1 == g2:
        break

      new_state = move_generators(state, state_queue, g1, g2, is_up)

      if new_state.moves >= MIN_MOVES:
        is_complete = True

      elif new_state.is_solution():
        print 'try_two_generator_move: SOLVED->' + new_state.toJSON()
        is_complete = True
        MIN_MOVES = new_state.moves

      elif new_state.is_valid():
        add_to_queue(new_state, state_queue)


def try_generator_move(state, state_queue, is_up):
  global MIN_MOVES

  is_complete = False
  current_floor = state.current_floor()


  for chip in current_floor.chips:
    for generator in current_floor.generators:
      if generator == chip:
          
        new_state = move_generator(state, generator, is_up)

        if new_state.moves >= MIN_MOVES:
          is_complete = True

        elif new_state.is_solution():
          print 'try_generator_move: SOLVED->' + new_state.toJSON()
          is_complete = True
          MIN_MOVES = new_state.moves

        elif new_state.is_valid():
          # print new_state.toJSON()
          # print 'try_generator_move: GEN_ID->' + str(generator) + ', FLOOR->' + str(current_floor.num)

          add_to_queue(new_state,state_queue)
        # else:
          # print 'try_generator_move: state not valid: ' + str(current_floor.num)

  return is_complete

def try_2chip_move(state, state_queue, is_up):
  global MIN_MOVES

  is_complete = False
  current_floor = state.current_floor()
  
  for i1 in current_floor.chips:
    for i2 in current_floor.chips:

      if i1 == i2:
        break

      new_state = move_chips(state, i1, i2, is_up)

      if new_state.moves >= MIN_MOVES:
        is_complete = True

      elif new_state.is_solution():
        print 'try_2chip_move: SOLVED->' + new_state.toJSON()
        is_complete = True
        MIN_MOVES = new_state.moves

      elif new_state.is_valid():
        # print 'f: ' + str(current_floor.num) + '=> ' + str(i1) + ':' + str(i2)
        # print new_state.toJSON()
        # print 'try_2chip_move: i1->' + str(current_floor.chips[i1]) + ', i2->' + current_floor.chips[i2] + ', FLOOR->' + str(current_floor.num)
        add_to_queue(new_state, state_queue)
      # else:
        # print 'try_2chip_move: state not valid: ' + str(current_floor.num)
      # else:
        # print new_state.toJSON()

  return is_complete

def try_chip_move(state, state_queue, is_up):
  global MIN_MOVES

  is_complete = False
  current_floor = state.current_floor()

  for chip in current_floor.chips:
    new_state = move_chip(state, chip, is_up)

    if new_state.moves >= MIN_MOVES:
      is_complete = True

    elif new_state.is_solution():
      print 'try_chip_move: SOLVED->' + new_state.toJSON()
      is_complete = True
      MIN_MOVES = new_state.moves

    elif new_state.is_valid():
      add_to_queue(new_state,state_queue)

  return is_complete

def find_answer():
  global MIN_MOVES
  global f
  
  state_queue = deque([])
  # state_queue = []

  add_to_queue(initial_state, state_queue)
 
  while len(state_queue) > 0:

    # state = state_queue.pop()
    state = state_queue.popleft()
    
    f.write(state.toJSON())

    # stop processing this 
    is_complete = False
    current_floor = state.current_floor()

    # try two moves up 
    if current_floor.num < max_floor: 
      is_complete = try_two_generator_move(state, state_queue, True)

      if not is_complete:
        is_complete = try_generator_move(state, state_queue, True)

      # try two chips up 
      if len(current_floor.chips) > 1 and not is_complete:
        is_complete = try_2chip_move(state, state_queue, True)

      # try single move up 
      if not is_complete:
        is_complete = try_chip_move(state, state_queue, True)

    # else:
    #   print state.toJSON()

    # try two moves down 
    if current_floor.num > 0:
      if not is_complete:
        is_complete = try_two_generator_move(state, state_queue, False)

      if len(current_floor.chips) > 1 and not is_complete:
        # print 'move down'
        is_complete = try_2chip_move(state, state_queue, False)

      # try single move down 
      if not is_complete:
        # print 'Try Down'
        is_complete = try_chip_move(state, state_queue, False)

      if not is_complete:
        is_complete = try_generator_move(state, state_queue, False)

  print MIN_MOVES


if __name__ == "__main__":
  find_answer()
