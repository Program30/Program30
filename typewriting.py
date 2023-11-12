import random as rd




# After entering the victory conditions, failure conditions, and typing, you need to press the Enter button once you have finished typing
els = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
rc = 0
wc = 0

print('This is a typewriting game.')
print("Let's play this game!")
print('Please input victory condition(how many characters; input a number)')
wonc = int(input())
print('Please input failed condition(how many characters; input a number)')
failedc = int(input())
while True:
    a = rd.choice(els)
    b = input()
    if b == a:
        rc += 1
        if rc == wonc:
            print('You win!')
            break
    else:
        failedc += 1
        if failedc == wc:
            print('You failed!')
            break
