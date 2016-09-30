# this file is used to compare whether two txt files are identical
import sys

def main():
	file1 = open("knn_result_10_9600.txt",'r')
	file2 = open("10_col_p_out.txt",'r')

	miscount = 0
	while 1:
	    line1 = file1.readline()
	    line2 = file2.readline()

	    if line1 and line2:

	      test1 = map(int,line1.split(" "))
	      test2 = map(int,line2.split(" "))
	      if len(test1) == len(test2):
		totalcount += len(test1)
		for i in range(len(test1)):
		  if test1[i]!= test2[i]:
		    miscount += 1
	      else:
		print "length of lines are not matched"
	    else:
	      break

	file1.close()
	file2.colse() 

if __name__ == '__main__':
  main()
   



