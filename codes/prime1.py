lim=int(input("enter the limit : "))
prime_list=[]
if lim>=2:
    for i in range(2,lim+1):
        prime=True
        for j in range(2,i):
            if (i%j==0):
                prime=False
        if prime:
            prime_list.append(i) 

    print('The prime numbers up to',lim,'are' )       
    print(prime_list)

else:
    print("the limit should be greater than or equal to 2")