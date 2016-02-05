"""
create on Jan 20, 2016

@author: Zexo Chen
"""

import math
import operator
from fastdtw import fastdtw,dtw
import time

# length is the number of attributes we use to compute the euclidean distance
#http://machinelearningmastery.com/tutorial-to-implement-k-nearest-neighbors-in-python-from-scratch/
def euclideanDist(list1,list2,length):
  distance = 0
  for x in range(length):
    distance += pow((list1[x]-list2[x]),2)
  return math.sqrt(distance)

def getNeighbors(trainingSet, testInstance,k):
  distances = []
  length = len(trainingSet[0])-1
  for x in range(len(trainingSet)):
    dist = euclideanDist(testInstance,trainingSet[x],length)
    #dist = fastdtw(testInstance,trainingSet[x])[0]
    distances.append((trainingSet[x][-1],dist))
  distances.sort(key=(lambda x: x[1]))
  '''
  for x in range(k):
    neighbors.append(distances[x][0])
  classVotes = {}
  for x in neighbors:
    if x in classVotes:
      classVotes[x] += 1
    else:
      classVotes[x] = 1
  voteResult = sorted(classVotes.items(),key = (lambda x:x[1]),reverse=True)
  '''
  classVotes = {}
  for x in range(k):
    if distances[x][0] in classVotes:
      classVotes[distances[x][0]] += 1
    else:
      classVotes[distances[x][0]] = 1

  largeCount = -1
  largeSet = []
  for key in classVotes:
    if classVotes[key] > largeCount:
      largeCount = classVotes[key]

  for key in classVotes:
    if largeCount == classVotes[key]:
      largeSet.append(key)

  for x in range(k):
    if distances[x][0] in largeSet:
      return distances[x][0]



  #return voteResult[0][0]
    
def main():
  start = time.clock()
  resultfile = open("knn_result_10_9600.txt",'w')
  trainfile = open("hierarchical_clustering_result_Euclidean.txt",'r')
  trainData = trainfile.readlines()
  for i in range(len(trainData)):
    trainData[i] = map(float,trainData[i].split(" ")) 
  
  #mystring = "251 232 219 238 223 218 233 204 228 227 223 232 235 234 237 234 235 229 200 157 235 206 253"
  #testData = map(float,mystring.split(" "))

  testfile_2001 = open("10_col_s_2001.txt",'r')
  testfile_2006 = open("10_col_s_2006.txt",'r')
  totalcount = 0
  matchingcount = 0
  mylist = []
  
  while 1:
    line1 = testfile_2001.readline()
    line2 = testfile_2006.readline()

    if line1 and line2:
      totalcount += 1
      test1 = map(float,line1.split(" "))
      test2 = map(float,line2.split(" "))
      result1 = getNeighbors(trainData,test1,9)
      result2 = getNeighbors(trainData,test2,9)
      #print result1,result2
      
      if result1 == result2:
        matchingcount +=1
        mylist.append(0)
      else:
        mylist.append(1)

      if totalcount % 9600 == 0:
        #print "The number of rows finished: " + str(totalcount//9600)
        output = ' '.join(map(str,mylist))
        resultfile.write(output+'\n')
        mylist = []
        end1 = time.clock()
        #print "Running time: " + str((end1-start))
    else:
      break
  
  print totalcount, matchingcount, float(matchingcount) / totalcount
  #960000 611123 0.636586458333

  testfile_2001.close()
  testfile_2006.close()
  end = time.clock()
  print "The running time: " + str((end-start))

if __name__ == '__main__':
  main()
