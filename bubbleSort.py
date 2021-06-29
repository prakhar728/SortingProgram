

def bubbleSorting(arr):
	n = len(arr)
	for i in range(n):
		for j in range(0, n-i-1):
			if arr[j] > arr[j+1] :
				arr[j], arr[j+1] = arr[j+1], arr[j]


arr=[]
n=int(input("Enter the number of elements in the list"))

for i in range(n):
    temp=int(input())
    arr.append(temp)

bubbleSorting(arr)

print ("Array after sorting is")
for i in range(len(arr)):
	print (arr[i],end=",")
