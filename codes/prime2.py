lim=int(input('enter limit'))
prime_list=[]
for i in range(2,lim):
    prime=True
    for j in range(2,i):
        if(i%j==0):
            prime=False
    if prime:
        prime_list.append(i)        
print(prime_list)