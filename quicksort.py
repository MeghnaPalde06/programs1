import time
import xml.etree.ElementTree as ET
tree=ET.parse('quick.xml')
root=tree.getroot()

def qsort(sets,left,right):
	if(left>=right):
		return -1
	pivot=partition(sets,left,right)
	qsort(sets,left,pivot)
	qsort(sets,pivot+1,right)
	return sets

def partition(sets,left,right):
	i=left+1
	j=right
	pivot=sets[left]
  
	while(1):
		while(pivot>=sets[i])and(i<right):
			i=i+1
		while(pivot<sets[j]):
			j=j-1
		if(i<j):
			temp=sets[i]
			sets[i]=sets[j]
			sets[j]=temp
		else:
			temp=sets[left]
			sets[left]=sets[j]
			sets[j]=temp
			return j

ip=[]
for neighbor in root.iter('value'):
	ip.append(neighbor.text)
print "Input array is:",ip
res=qsort(ip,0,len(ip)-1)
print "Outpur array is:",res

