# Convert a given string to int using a single line of code
'''str1=("123")
print(int(str1))
'''

# Write a code snippet to convert a string to a list.
'''str1="My name is raj"
print(str1.split())

str1="My name is raj"
print(str1.split(" "))
'''

# Write a code snippet to reverse a string
'''str1="India is my country"
print(str1[::-1])
'''

'''str1="India is my country"
str2=""
for i in str1:
    str2=i+str2
print(str2)
'''

# Write a code snippet to sort a list in Python
'''my_list=[5,6,8,1,3,5,9]
my_list.sort()
print(my_list)'''

# delete a file in Python
'''import os
os.remove("file_path/name")'''

#  access an element of a list
'''
list1=[1,202,3,45,89]
print(list1[3])
'''

# deleting an element from a list
'''my_list=[2,25,8,7,6]
my_list.remove(8)
print(my_list)
my_list.pop(1)
print(my_list)'''

# delete an entire list
'''my_list=[1,2,3]
my_list.clear()
print(my_list)'''

# delete an entire list
'''import numpy as np
array1=np.array([1,2,3,4,5,6])
#print(np.flip(array1))
array2=[]
for i in array1:
    array2=[i]+array2
print(array2)'''

# code snippet to get an element, delete an element, and update an element in an array.
'''import numpy as np
array1=np.array([5,8,5,6,4])
print(array1[0])
array1=array1+2
print(array1)
array1=array1*2
print(array1)
print(array1[::-1])
print(array1[1:3])
array3=array1.flatten()
print(array3)
array3[2]=256
print(array3)
array3=np.delete(array3,2)
print(array3)'''

# Write a code snippet to concatenate lists
'''list1=[1,2,3,4,5]
list2=[6,7,8,9,10]
print(list1+list2)'''

'''List1= ['W', 'a', 'w','b']
List2 = ['e', ' ','riting','log']
list3=[]
for x,y in zip(List1,List2):
    list3.append(x+y)
print(list3)
'''

# code snippet to generate the square of every element of a list
'''my_list=[1,2,3,4,5]
sqr_list=[]
for i in my_list:
    sqr_list.append(i*i)
print(sqr_list)'''

# split and join
'''my_str="Hello Doctor"
txt=my_str.split(" ")
print(" ".join(txt))'''

# functions used for Python strings
'''my_str=" Hello word "
print(len(my_str))
print(my_str.strip())
print(my_str.replace("Hello","Enter the"))
print(my_str.split(" "))
print(my_str.lower())
'''
# global and local variables in Python
'''x=20
def func():
    x=4
    print("Inside function",x)
print("outside function",x)
func()
'''

# return and yield keywords
'''list1=[1,2,3,4,5]
def list2(lst):
    for i in list1:
        print(i)
        if i!=2:
            yield i
print(list(list2(list1)))
'''
# generate list
'''def generate_number(n):
    for i in range(n):
        yield i
num=generate_number(10)
print(num)
'''
# Fibnocii series
'''
def fib(n):
    a,b=0,1
    for _ in range(n):
        yield a
        a,b=b,a+b
print(list(fib(10)))
'''
'''
def squares(n):
    for i in range(n):
        yield i ** 2

# Using the generator
square_gen = squares(5)
for num in square_gen:
    print(num)

'''
# Generator expression
'''
squares_gen = (x ** 2 for x in range(5))
print(list(squares_gen))
'''

# lambda functions in Python
'''a = lambda x: x + 10
print(a(5))
'''

# various ways of adding elements to a list
'''
list1=[1,2,3,4]
list1.append(6)
print(list1)
list1.reverse()
print(list1)
list1.sort()
print(list1)
list1.insert(4,5)
print(list1)
list1.extend([7,8])
print(list1)
list1=list1+[9]
print(list1)
'''

# program to check whether a number is prime or not
'''def prime_check(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True


num=int(input("Enter no to check it is prime or not: "))
if prime_check(num):
    print("Prime")
else:
    print("Not a Prime")


#2,3,5,7,11'''

# program in Python to return the factorial of a given number using recursion
'''
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))        
'''
# min value in the list
'''my_list=[2,5,8,12,25]
#min_num=min(my_list,key=lambda x:x)
#print(min_num)
min_val=my_list[0]
for i in my_list:
    if min_val>i:
        min_val=i
print(min_val)'''

#my_list=['a','e','i','o','u']

#print(",".join(my_list))


# List Excercise

# Python program to interchange first and last elements in a list
#my_list=[1,12,56,45,25]
'''temp=my_list[0]
print(temp)
a=len(my_list)
last=my_list[a-1]
print(last)
my_list[0]=last
my_list[a-1]=temp
print(my_list)
'''
#my_list[0],my_list[-1]=my_list[-1],my_list[0]
#my_list=my_list[-1:]+my_list[1:-1]+my_list[:1]
#print(my_list)
# Python program to swap two elements in a list
'''my_list=[34,24,76,44,52]
pos1=2
pos2=4
def swap_list(lst,pos1,pos2):
    my_list[pos1],my_list[pos2]=my_list[pos2],my_list[pos1]
    return my_list
print(swap_list(my_list,pos1,pos2))'''

# Python – Swap elements in String list
'''mylist=['apple','banana','orange','chiku']
res=[]
for i,item in enumerate(mylist):
    if i==0:
        updated_item=(item.replace('a', 'A', 1)
                      .replace('b', 'B', 1)
                      .replace('o', 'O', 1)
                      .replace('c', 'C', 1))
        updated_item=updated_item.capitalize()
    else:
        updated_item=item.capitalize()
    res.append(updated_item)
print(res)
'''

# Find Maximum of two numbers in Python
#Input: a = -1, b = -4
#Output: -1

'''def max_check(a,b):
   if a>b:
       print("Max no is :",a)
   else:
        print("Max no is:",b)

a=-1
b=-4
max_check(a,b)
'''
'''
a=5
b=6
print(a if a>=b else b)'''

'''a=17
b=10
x=[a,b]
x.sort()
print("Max no is",x[-1])'''

# Minimum of two numbers in Python
'''a=-4
b=-5
print("Min no is" ,a if a<=b else b)'''
'''def num_check(list1,n):
    for i in list1:
        if i==n:
            return True
    return False'''
#Check if element exists in list in Python
'''test_list = [1, 6, 3, 5, 3, 4]
num=6
print(num_check(test_list,num))

test_list = [1, 6, 3, 5, 3, 4]
num=6
if num in test_list:
    print("Present")
else:
    print("Not Present")
'''

# Different ways to clear a list in Python
'''test_list = [1, 6, 3, 5, 3, 4]
test_list.clear()
print(test_list)
while(len(test_list)!=0):
    test_list.pop()
print(test_list)'''
# Reversing a List in Python
'''List = [4, 5, 6, 7, 8, 9]
#print(List[::-1])
List1=[]
for i in List:
    List1.insert(0,i)
print(List1)'''

# Count occurrences of an element in a list
'''def count_num(lst,x):
    count=0
    for i in lst:
        if i==x:
            count+=1
    return count

lst = [15, 6, 7, 10, 12, 20, 10, 28, 10]
x = 10
print(count_num(lst,x))'''
'''lst = [15, 6, 7, 10, 12, 20, 10, 28, 10]
x = 10
print(lst.count(x))'''

# find sum and average of List in Python
'''Input: [4, 5, 1, 2, 9, 7, 10, 8]
Output:
sum =  46
average =  5.75
'''
'''def sum_avg(lst):
    length=len(lst)
    sum=0
    for i in lst:
        sum+=i
    print("sum is :",sum)
    avg=sum/length
    print("avg is :",avg)

my_list=[4, 5, 1, 2, 9, 7, 10, 8]
sum_avg(my_list)
'''
'''my_list=[4, 5, 1, 2, 9, 7, 10, 8]
sum=sum(my_list)
print(sum)'''
'''
test_list = [12, 67, 98, 34]
res = []
for ele in test_list:
    sum = 0
    for digit in str(ele):
        sum += int(digit)
        print(sum)
    res.append(sum)
    print(res)'''

# Multiply all numbers in the list
'''list1 = [1, 2, 3]
mul=1
for i in list1:
    mul=mul*i
print(mul)'''

# program to find smallest number in a list
'''list1 = [10, 20, 4]
#print(min(list1))
temp=list1[0]
for i in list1:
    if i<temp:
        temp=i
print(temp)'''


# program to print even numbers in a list
'''list1 = [2, 7, 5, 64, 14]
even_list=[]
for i in list1:
    if i%2==0:
        even_list.append(i)
print(even_list)
'''
# program to print all even numbers in a range
'''def even_range(x,y):
    even=[]
    for i in range(x,y+1):
        if i%2==0:
            even.append(i)
    return even

start = 4
end = 16
print(even_range(start,end))'''

# program to count Even and Odd numbers in a List
#Input: list1 = [2, 7, 5, 64, 14]
#Output: Even = 3, odd = 2

'''def even_odd_count(lst):
    even = 0
    odd = 0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd

list1 = [2, 7, 5, 64, 14]
a,b=even_odd_count(list1)
print("even: ",a)
print("odd: ",b)'''


'''def even_odd_count(lst):
    even = 0
    odd = 0
    for i in lst:
        if i>=0:
            even+=1
        else:
            odd+=1
    return even,odd

list1 = [2, -7, 5, -64, -14]
a,b=even_odd_count(list1)
print("pos: ",a)
print("neg: ",b)'''

# Remove multiple elements from a list in Python
#Input: [12, 15, 3, 10]
#Output: Remove = [12, 3], New_List = [15, 10]

'''my_list=[12, 15, 3, 10]
rem_list=[12, 3]

for i in rem_list:
    my_list.remove(i)
print(my_list)'''

# Convert List to List of dictionaries
'''test_list = ["Gfg", 10]
key_list = ["name", "id"]
res=[]
#for i in range(len(key_list)):
#    res.append({key_list[i]:test_list[i]})
#print(res)

for k,v in zip(key_list,test_list):
    res.append({k:v})
print(res)'''