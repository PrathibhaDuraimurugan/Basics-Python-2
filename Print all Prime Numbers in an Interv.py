lower = int(input("Enter the Lower limit here:"))
upper = int(input("Enter the Upper limit here:"))

for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)

