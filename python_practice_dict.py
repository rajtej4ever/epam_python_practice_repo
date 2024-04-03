'''myDict = {'ravi': 10, 'rajnish': 9,
        'sanjeev': 15, 'yash': 2, 'suraj': 32}

lst1=list(myDict.keys())
lst1.sort()
lst2={}
for i in lst1:
    lst2[i]=myDict[i]
print(lst2)'''

'''keys = ['a', 'b', 'c']
values = [1, 2, 3]
result=dict(zip(keys,values))
print(result)

print(result.get('d'))'''

my_dict = {'a': 10, 'b': 20, 'c': 30, 'd': 40}

def avg_dict(d):
    avg=sum(d.values())/len(d)
    return avg
    
avg=avg_dict(my_dict)
print(avg)