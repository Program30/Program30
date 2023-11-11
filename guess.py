#- 👋 Hi, I’m @Program30
#-  My name is XiaoYuXuan
#-  I'am from China
#-  I'am eleven years old
#-  I like porgram
#-  I'm a happy boy.
#-  I'm use the GitHub first time.
#-  I'm program is not very good.
#-  But I hope you can provide me with more opinions to make my work better.
<!---
Program30/Program30 is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->
import random as rd



print('This is a guess numbers game')
print('Let's play it!')
# number and number middle use space separation 
a = input('Please input a guess number range') 
a1 = split(' ')
b = []
for i in range(a1)：
    b.apppend(int(i))
while True:
    d = rd.randint(b[0], b[1]+1)
    e = input('Please input a your guess number')
    if int(e) == d:
        print('guess right!')
        break
    elif e < d or e > d:
        print('guess worng')
        if e < d:
            print('The number is on the ' + str(e) + 'and' + str(b[1]))
        elif e > d:
            print('The number is on the ' + str(d) + 'and' + str(e))
    else:
        print('Your input character(s) is not number')
