###################################################################################
# Plot the change detection result image                                          #
# Author: Zexi Chen                                                               #
# Date: 01/17/2016                                                                #
# #################################################################################

library(utils)
library(fields)


setwd("C:\\Users\\czx\\Google Drive\\Research\\From professor\\Not_published_yet\\")

mydata = read.table("whole_possible_change_map_Euclidean.txt", sep=" ")

#image.plot(x,y,mydata,col=c(0,1))

mydata <- as.matrix(mydata)

image.plot(mydata,col=c(0,1))