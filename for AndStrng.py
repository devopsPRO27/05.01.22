'''
# continue
numbers=[2,'hhh',5.15,2,5,6,6,]
for ta in numbers:
    continue
    if ta == 'hhh':
        continue
    print(ta)
#for in range
for i in range(1,400):
    print(i)

    if i%11 ==0 and i%2==0:
        break
#take the input and add the value to the list
numbers=[]
for hodi in range(0,8):
    numbers.append(int(input('please enter a number ')))#add input to the list
print(numbers)

#check the bigger of 8 inputs
max=0
for hodi in range(0,8):
    x=int(input('please enter a number '))
    if  x >max:
        max=x
print(numbers)

#while with condition
input2=input('press q to exit')
while input2 != 'q':
    print('hii you ')
    input2 = input('press q to exit')
print('out of the loop')

# do while
while True:
    input2 = input('press q to exit')
    print('hii you ')
    if input2 == 'q':
        break
print('out of the loop')

#another example of while
sum = 0
while sum < 300:
    #sum+=int(input('please enter a number'))
    x=input('please enter a number')
    x=int(x)
    sum = sum+x
print(f'sum is {sum}')

#do while
while True:
    name=input('please enter a name ')
    if name.lower() == 'mark':
        print(name)
        break
print('out of the loop')

#continue in while
x=0
while x<10:
    if x==3:
        x=x+1
        continue
    print(x)
    print(x+1)
    print(x+2)
    print(x+3)
    print(x+4)
    x = x + 1


# Calculator

x=float(input('please enter the first number '))
y=float(input('please enter the second number '))
while True:
    oper = input('please choose the right operator or q to exit')
    if oper.lower() == '+':
        print(x + y)
    elif oper == 'q':
        break
    elif oper == '-':
        print(x-y);
    elif oper == '*':
        print(x*y)
    elif oper == '/' and y!=0:
        print(x/y)
    else:
        print('choose right this time ')

#nested for-loop (tow loops )
lst=[['12',44,55,66,14],[2,7,8],[3]]
print(lst)
for ta in lst:
    print(ta)
    for x in ta:
        print(x)
        for lt in 'hothaifa':
    print(lt)
'''


names=['jack', 'marry','lolo','avraham','shefbfa']
for name in names:
    if name.count('a')>0:
        print (f'the name {name} ')
        for l in name:
            if l == 'a':
                print(name.index(l))














