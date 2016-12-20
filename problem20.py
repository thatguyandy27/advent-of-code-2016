import re
from collections import deque

bot_commands = [''] * 210

bot_chips = []
for i in range(210):
    bot_chips.append([])
output = []
for i in range(21):
    output.append([])   # 

command_pattern = 'bot (\d*) gives low to (bot|output) (\d*) and high to (bot|output) (\d*)'
value_pattern = 'value (\d*) goes to bot (\d*)'

command_regex = re.compile(command_pattern)
value_regex = re.compile(value_pattern)
bot_queue = deque([])

class Bot:
  
  def __init__(self, bot_num, low_type, low_num, high_type, high_num):
    self.low_type = low_type
    self.low_num = low_num
    self.bot_num = bot_num
    self.high_type = high_type
    self.high_num = high_num

def read_commands():
  f = open('day10.dat', 'r')

  for line in f:
    command_match = command_regex.match(line)
    value_match = value_regex.match(line)

    if command_match and value_match:
      print 'bothmatch: ' + line
    elif not command_match and not value_match:
      print 'neithermatch: ' + line
    elif command_match:
      bot_num = int(command_match.groups()[0])
      bot = Bot(bot_num, command_match.groups()[1], int(command_match.groups()[2]), command_match.groups()[3], int(command_match.groups()[4]))
      bot_commands[bot_num] = bot
    else:

      index = int(value_match.groups()[1])
      value = int(value_match.groups()[0])

      bot_chips[index].append(value)

      if len(bot_chips[index]) == 2:
        
        bot_queue.append(index)

# bot queue?
def execute_commands():

  while True:
    index = bot_queue.popleft()

    bot = bot_commands[index]
    chips = bot_chips[index]
    chips.sort()

    if len(output[0]) == 1 and len(output[1]) == 1 and len(output[2]) == 1:
      print output[0][0] * output[1][0] * output[2][0]
      return False

    if bot.low_type == 'output':
      output[bot.low_num].append(chips[0])
    else:
      low_chips = bot_chips[bot.low_num]

      low_chips.append(chips[0])

      if len(low_chips) == 2:
        bot_queue.append(bot.low_num)

    if bot.high_type == 'output':
      output[bot.high_num].append(chips[1])

    else:
      high_chips = bot_chips[bot.high_num]

      high_chips.append(chips[1])

      if len(high_chips) == 2:
        bot_queue.append(bot.high_num)

    bot_chips[index] = []

  print bot_index

if __name__ == "__main__":
  read_commands()


  execute_commands()