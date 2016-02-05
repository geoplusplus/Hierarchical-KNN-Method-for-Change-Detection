import numpy

def main():
  d1 = numpy.random.random_integers(1, 4800*9600, 1000)
  d1.sort()
  print d1,len(d1)
    
    
if __name__ == '__main__':
  main()
  
