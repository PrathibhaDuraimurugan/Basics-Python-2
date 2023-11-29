# To Check If the Number is Armstrong or Not
num = int(input("Enter the number here: "))
sum = 0
temp = num

while temp > 0:
    digit = temp % 10
    cube = digit ** 3
    sum = sum + cube
    temp //= 10  

if sum == num:
    print('It is an Armstrong number')
else:
    print('It is not an Armstrong number')
