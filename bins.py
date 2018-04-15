import csv

def binarysearch(a,left,right,key):
    if(right>=left):
        mid=(right+left)/2;
        if(key==a[mid]):
            print"Book found"
        elif(key>a[mid]):
            return binarysearch(a,mid+1,right,key)
            print"book found"
        else:
            return binarysearch(a,left,mid-1,key)
    else:
        print"Book not found"

a=list()
with open('abc.csv','rb')as csvfile:
    reader1=csv.reader(csvfile)
    for row in reader1:
        print(row[0])
        a.append(row[0])

num=len(a)
print"The book list is",a

newlist=list()

for book in a:
    newlist.append(book.lower())

newlist.sort()
print"The new sorted list is",newlist

choice='y'
while(choice=='y'):

    key=raw_input("Enter the book to be searched:")
    key=key.lower()
    print(key)
    binarysearch(newlist,0,num-1,key)
    choice=raw_input("Do you want to search more:(y/n)")
