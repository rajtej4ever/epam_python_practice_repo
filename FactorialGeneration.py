fact_num=int(input("Enter the factorial no: "))
def fact_gen(fact):
    if fact<=1:
        return 1
    else:
        return fact*fact_gen(fact-1)
print(fact_gen(fact_num))