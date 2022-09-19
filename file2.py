import string
password= input('enter your password')

num=0
lower= 0
upper= 0
punctuation=0

if len(password)>=8:
    password.strip()
    for i in password:
        if i.isnumeric():
            num+=1
        else:
            if i.isupper():
                upper+=1
           # elif i in string.punctuation:
            elif i in '!@#$%^&*()_+-=;:/?.>,<`~':
                punctuation += 1
            else:
                lower += 1


if num > 0 and upper > 0 and lower > 0 and punctuation > 0:
    print('your password is achieve the all items👍🏻')
else:
    print('your password is incorrect maybe your lose some items😅', num, upper,lower,punctuation)


