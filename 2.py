def rotate (n):
    if n == 0:
        return " "
    else:
        a = int(input("value "))
        return rotate(n-1) + f" {a} "


n = int(input("Enter n: "))

print(rotate(n))
