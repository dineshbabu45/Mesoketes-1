a=input().split(' ')
s=[]
w=[]
n=[]
e=[]
k=0
l=[]# To store the directions.
l1=[]# To strore the attacking strength.
for i in range(0,len(a)): # The loop is to extract the directions along with attacking strenth.
    if a[1]=='1$':#Checks whether the input starts with day 1.
        if a[i]=='W' or a[i]=='E' or a[i]=='N' or a[i]=='S' :
            l.append(a[i])#Updates the direction to list 'l'.
            l1.append(int(a[i+4]))#Updates the attacking strength to list 'l1' with same index corresponding to direction.
    else:#If the input not starts with day 1.
        print("Enter from day 1")
        k=1
        break
l2=[]
for i in range(0,len(l)):#This loop is to split the first occurence of direction because we cannot compare with null values.
    if l[i] not in l2:#Checks whether the direction is occured for first time.
        if l[i]=='E':
            e.append(l1[i])#Updates the strenth of attack occured on East.
            l2.append(l[i])#Updates the direction in list 'l2'.
        if l[i]=='W':
            w.append(l1[i])#Updates the strenth of attack occured on West.
            l2.append(l[i])#Updates the direction in list 'l2'.
        if l[i]=='N':
            n.append(l1[i])#Updates the strenth of attack occured on North.
            l2.append(l[i])#Updates the direction in list 'l2'.
        if l[i]=='S':
            s.append(l1[i])#Updates the strenth of attack occured on South.
            l2.append(l[i])#Updates the direction in list 'l2'.
    else:#This statement works if the direction is occuring second time.
        if l[i]=='E':#East side.
            el=sorted(e)
            if el[len(el)-1] < l1[i]:#Checks whether the strenth is greater than previous one.
                e.append(l1[i])

        if l[i]=='W':#West side.
            wl=sorted(w)
            if wl[len(wl)-1] < l1[i]:#Checks whether the strenth is greater than previous one.
                w.append(l1[i])
        if l[i]=='N':#North side.
            nl=sorted(n)
            if nl[len(nl)-1] < l1[i]:#Checks whether the strenth is greater than previous one.
                n.append(l1[i])

        if l[i]=='S':#South side.
            sl=sorted(s)
            if sl[len(sl)-1] < l1[i]:#Checks whether the strenth is greater than previous one.
                s.append(l1[i])
n=len(e)+len(w)+len(n)+len(s)
if k!=1:#Prints only if input starts with day 1.
    print(n)
