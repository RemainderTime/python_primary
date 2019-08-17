#循环

#循环语句

# while for

counter =1

while counter <=10:
    counter+=1
    print(counter)


# break   continu
a=[['a','c','b'],(1,2,3)]
for b in a:
    print(b)

#指定循环次数  第三个参数为步长

for x in range(0,10,2):
    print(x,end='|')

#依据上面步长   可使用切片
b= a[0:len(a):2]