# sample Sets
import sys
Set1 = {"A", 1, "B", 2, "C", 3}
Set2 = {"Geek1", "Raju", "Geek2", "Nikhil", "Geek3", "Deepanshu"}
Set3 = {(1, "Lion"), ( 2, "Tiger"), (3, "Fox")}

#print(Set1.__sizeof__())

#for i in Set1:
#    print(i)

sets = set([8, 16, 24, 1, 25, 3, 10, 65, 55])

#print(max(sets))
#print(min(sets))
set1=set([12, 10, 13, 15, 8, 9])
#remove,discard,pop
set_copy=set1.copy()
#for i in set_copy:
#    set1.pop()
#    print(set1)

'''for i in set_copy:
    set1.remove(i)
    print(set1)
'''
'''for i in set_copy:
    set1.discard(i)
    print(set1)
'''

a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]

c=set(a)
d=set(b)
#print(c&d)
#print(c | d)

ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]
#print(set(ar1) & set(ar2) & set(ar3))

'''Input : list1 = [1, 2, 3, 4, 5, 6] 
        list2 = [4, 5, 6, 7, 8] 
Output : Missing values in list1 = [8, 7] 
         Additional values in list1 = [1, 2, 3] 
         Missing values in list2 = [1, 2, 3] 
         Additional values in list2 = [7, 8] 
'''
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8]

a=set(list1)
b=set(list2)
#print(a.difference(b))
#print(b.difference(a))
#print(zip(a,b))

A = [1, 4, 5, 7, 9]
B = [4, 5, 7, 9]
x=set(A)
y=set(B)


def convert(s):
    # Use a list comprehension to create a new list from the elements in the set
    for elem in s:
        return elem


s = {1, 2, 3}
print(convert(s))
