from time import time
from termcolor import colored
from colorama import init
import math

init()

t=time()
f=open("c:/Users/srinivas/Downloads/Telegram Desktop/words.txt","r").read()
arr = f.split("\n")
# arr = [x for x in range(0,10000000)]
print(time()-t,len(arr))

def regularSearch(val, arr):
	print(colored("Regular Search:","cyan"))
	t0=time()
	for i in range(0,len(arr)):
		if arr[i]==val:
			print(colored("Yes, got it at","green"), colored(i,"green"))
			break
		elif i==len(arr)-1:
			print(colored("Word not found","red"))
			break
	t1=time()
	print(t1-t0)
	return t1-t0

def binarySearch(val, arr):
	print(colored("Binary Search:","cyan"))
	start = 0
	end = len(arr)-1
	t0=time()
	while start<=end:
		mid = math.floor((start + end) / 2)
		# print(start, mid, end)
		# print(arr[mid]<val)
		if arr[mid]==val:
			t1=time()
			print(t1-t0)
			return (mid,t1-t0)
		elif arr[mid]<val:
			start=mid+1
		elif arr[mid]>val:
			end=mid-1
		
	t1=time()
	print(t1-t0)
	return (-1,t1-t0)

while True:
	
	print(colored("====================================","green"))

	val = input("Enter value to search: ")
	if val=="q":
		exit()
	# val = int(val)
	
	r=regularSearch(val, arr)
	b=binarySearch(val, arr)
	
	if b[0] != -1:
		print(colored("Yes, got it at","green"),colored(b[0],"green"))
	else:
		print(colored("Word not found","red"))

	if r<b[1]:
		print("Regular wins!!!")
	elif r>b[1]:
		print("Binary wins!!!")
	else:
		print("Both wins!!!")