#Input : [12, 35, 9, 56, 24]
#Output : [24, 35, 9, 56, 12]
"""
def swap_list(lst):
    lst[0],lst[-1]=lst[-1],lst[0]
    return lst


list2=[12, 35, 9, 56, 24]

print(swap_list(list2))


def swap_list(lst):
    temp=lst[0]
    lst[0]=lst[-1]
    lst[-1]=temp
    return lst

list2 = [12, 35, 9, 56, 24]
print(swap_list(list2))

def swap_list(lst):
    lst=lst[-1:]+lst[1:-1]+lst[:1]
    return lst

list2 = [12, 35, 9, 56, 24]
print(swap_list(list2))

list2 = [12, 35, 9, 56, 24]
print(list2[:1])

#Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
#Output : [19, 65, 23, 90]


def swap_lst(lst,pos1,pos2):
    lst[pos1],lst[pos2]=lst[pos2],lst[pos1]
    return lst

list1=[23, 65, 19, 90]
pos1=1
pos2=3
print(swap_lst(list1,pos1-1,pos2-1))

lst = [10,20,30,40]
print(len(lst))

counter=0
lst = [10,20,30,40]
for i in lst:
    counter+=1
print(counter)

#Input: a = 2, b = 4
#Output: 4


def max_no(a,b):
    if a>b:
        print(a)
    else:
        print(b)
max_no(2,4)

def num_check(test_list,no):
    for i in test_list:
        if i ==no:
            return True
        else:
            return False
test_list = [1, 6, 3, 5, 3, 4]
no=2
print(num_check(test_list,no))

#Input: [2, 3, 5, 6, 7]
#Output: []

lst=[2, 3, 5, 6, 7]
lst.clear()
print(lst)
"""
#Input: list = [4, 5, 6, 7, 8, 9]
#Output: [9, 8, 7, 6, 5, 4]

