



def get_count():
  f = open('day9.dat', 'r')
  index = 0
  buckets = []

  for line in f:
    buckets = [1] * len(line)

    while index < len(line):    
      next_par = line.find('(', index)
      if next_par == -1: # we done
        index = len(line)
      else:
        
        close_paren = line.find(')', next_par)
        repeat = line[next_par + 1: close_paren]
        spl = repeat.split('x')
        chars = int(spl[0])
        times = int(spl[1])

        for n in range(chars + 1):
          buckets[close_paren + n] *= times

        for n in range(close_paren - next_par + 1):
          buckets[next_par + n] = 0

        index = close_paren  # first char after close paren

    print sum(buckets)
    

if __name__ == "__main__":
  get_count()