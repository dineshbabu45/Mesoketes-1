a=input().split(' ')
s=0 #Intialising the south wall's height to be 0 since no attck has hapened.
w=0 #Intialising the West wall's height to be 0 since no attck has hapened.
n=0 #Intialising the North wall's height to be 0 since no attck has hapened.
e=0 #Intialising the East wall's height to be 0 since no attck has hapened.
c=0 #Intialising the count that number of times the wall's have heightened. 
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
#I have directions in list 'l' and strength in list 'l1'.
for i in range(0,len(l)):#Since two lenths will be equal we can access with same index numbers.
    if l[i]=='E':
        if l1[i]>e: #Chechs whether the East direction's attacked strength is greater than prevoius attack.
            c+=1  #Increament the c if the strenth is greater (Wall rises for that attack ).
            e=l1[i]#Changing the value which is the highest attack on East side.

    if l[i]=='W':
        if l1[i]>w:#Chechs whether the West direction's attacked strength is greater than prevoius attack.
            c+=1#Increament the c if the strenth is greater (Wall rises for that attack ).
            w=l1[i]#Changing the value which is the highest attack on West side.
    if l[i]=='N':
        if l1[i]>n:#Chechs whether the North direction's attacked strength is greater than prevoius attack.
            c+=1#Increament the c if the strenth is greater (Wall rises for that attack ).
            n=l1[i]#Changing the value which is the highest attack North side.

    if l[i]=='S':
        if l1[i]>s:#Chechs whether the South direction's attacked strength is greater than prevoius attack.
            c+=1#Increament the c if the strenth is greater (Wall rises for that attack ).
            s=l1[i]#Changing the value which is the highest attack on South side.
if k!=1:
    print(c)
