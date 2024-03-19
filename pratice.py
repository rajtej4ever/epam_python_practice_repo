def prime_check(n):
    if n<=1:
        print("Not a prime no")
    else :
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                print("Not prime")
            else:
                print("prime")

prime_check(10)