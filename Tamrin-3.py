x = 0
i = 1
i_1 = 1
s = 1
a = 1
z = 1
y_list = []

while i<=10:
    x = int(input('x{} ra vared konid : '.format(z)))
    if x == 5:
        print('please import another number , there nothin defind for 5')
        continue
    z+=1
    if x > 5 :
        while i_1 <= x:
            s = a * s
            a+=1
            i_1+=1
        y_list.append(s)
        s = 1
        a = 1
        i_1 = 1
    elif x>=0 and x<5:
        y_list.append(3*x**4)
    elif x<0:
        m = 3*x
        y_list.append(m**6)
    i+=1
print(y_list)