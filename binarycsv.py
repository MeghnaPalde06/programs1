import csv

def binarysearch(arr,left,right,key):
	if (right>=left):
		mid = (left+right)/2
		if (arr[mid]==key):
			print ("Key found at position"),mid+1
		elif (arr[mid]>key):
			return binarysearch(arr,left,mid-1,key)
		else:
			return binarysearch(arr,mid+1,right,key)
	else:
		print ("Book not found.")


a=list()
with open('data2.csv','rb') as csvfile:
	reader1=csv.reader(csvfile)
	for row1 in reader1:
		print (row1[0])
		a.append(row1[0])

print ("The list of books is : "),a
num=len(a)

new_list=list()

for book in a :
	new_list.append(book.lower())

print ("List of book:"),new_list

new_list.sort()
print ("The sorted list of books is:"),new_list

choice='y'
while (choice=='y'):
	key=raw_input("Enyer the book to be searched:")
	key=key.lower()
	binarysearch(new_list,0,num-1,key)
	choice=raw_input("Do you want to continue?(y/n)")
