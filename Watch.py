# Write a program which reads an integer 
# S[second] and converts it to h:m:s where h, m, s denote hours, minutes (less than 60) and seconds (less than 60) respectively.
# Input An integer S is given in a line.
# Output Print h, m and s separated by ':'. You do not need to put '0' for a value, which consists of a digit.

S = int(input())
print("%d:%d:%d"%(S/3600,(S%3600)/60,S%60))
