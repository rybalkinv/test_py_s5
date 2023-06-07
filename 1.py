def check(n):
    i = 2
    for i in range(2, n):
        if n % i == 0:
            return "no"
       
    return "yes"
        
num = int(input("input number: "))

print(check(num))
