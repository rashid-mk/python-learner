num=int(input('Enter a Number : '))
prime=True
if num>1:
    for i in range(2,num):
        if(num%i==0):
            prime=False
            break
    if prime:    
        print('prime')  
    else:
        print('not prime')      
else:
    print('not prime')        
