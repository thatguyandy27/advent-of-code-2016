
def get_count():
  f = open('day9.dat', 'r')
  index = 0
  output = []

  for line in f:
    while index < len(line):    
      next_par = line.find('(', index)
      if next_par == -1: # we done
        output.append(line[index:])
        index = len(line)
      else:
        output.append(line[index:next_par]) # append all the chars until we hit the marker
        close_paren = line.find(')', next_par)
        repeat = line[next_par + 1: close_paren]
        spl = repeat.split('x')
        chars = int(spl[0])
        times = int(spl[1])

        start = close_paren + 1 # first char after close paren
        end = start + chars 
        index = end # first char after repeat

        sub = line[start:end] # grab substring
        output.append(sub * times) # multiply it out
  
  print len(''.join(output))

if __name__ == "__main__":
  get_count()