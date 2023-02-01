#Fibonacci
import time as timer1
num1 = 1
num2 = 0
num3 = 0
while True:
    num3 = num1 + num2
    num2 = num1
    num1 = num3
    timer1.sleep(1)
    print(num3)
