import struct
import numpy

def main():
  f1 = open("MODIS/s_2006.raw", "rb")
  f2 = open("MODIS/s_2001.raw","rb")
  #outputfile = open("4800_col_s_2006.txt",'w')
  outputfile = open("sampling_1000_col_s.txt",'w')
  colnum = 0
  
  mylist = []
  for i in range(1,24):
    mylist.append("b"+str(i))
  output = ' '.join(mylist)
  outputfile.write(output+'\n')
  mylist = []

  samples = numpy.random.random_integers(0, 4800*9600-1, 500)
  samples.sort()
  sample_count = 0
  
  mylist1=[]
  mylist2=[]
  try:
    while colnum<4800*9600 and sample_count < len(samples):
      byte1 = f1.read(1)
      byte2 = f2.read(1)
      if byte1 == "" or byte2 == "":
        break
      
      value1 = struct.unpack('B',byte1)[0]
      mylist1.append(value1)
      value2 = struct.unpack('B',byte2)[0]
      mylist2.append(value2)
      if len(mylist1)==23:
        if samples[sample_count] == colnum:
          output = ' '.join(map(str,mylist1))
          outputfile.write(output+'\n')
          output = ' '.join(map(str,mylist2))
          outputfile.write(output+'\n')
          sample_count += 1
        mylist1 = []
        mylist2 = []
        colnum +=1
        if colnum%9600==0:
      	  print colnum//9600

    print colnum,sample_count
  finally:
  	f1.close()
        f2.close()
  	outputfile.close()

if __name__ == '__main__':
  main()



