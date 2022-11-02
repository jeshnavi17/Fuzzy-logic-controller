#a is membership value of VN
#b is membership value of NR
#c is membership value of FR
#d is membership value of VFR

D=float(input("Enter the distance in metres:"))
A=float(input("Enter the angle in degrees:"))
a=0
b=0
c=0
d=0
a1=0
b1=0
c1=0
d1=0
e1=0

if D==0.1:
  a=1
  b=0
  print(a)
  
elif 0.1<D<0.8:
  a= (0.8-D)/0.7
  b= (D-0.1)/0.7
  print(a)
  print(b)

elif D==0.8:
  a=0
  b=1
  c=0
  print(b)
  
elif 0.8<D<1.5:
  b= (1.5-D)/0.7
  c= (D-0.8)/0.7
  print(b)
  print(c)

elif D==1.5:
  b=0
  c=1
  d=0
  print(c)

elif 1.5<D<2.2:
  c= (2.2-D)/0.7
  d= (D-1.5)/0.7 
  print(c)
  print(d)

elif D==2.2:
  c=0
  d=1
  print(d)

#a1 is membership value of LT
#b1 is membership value of AL
#c1 is membership value of A
#d1 is membership value of ART
#e1 is membership value of RT

if A==-90:
  a1=1
  b1=0
  print(a1)

elif -90<A<-45:
  a1= (-45-A)/45
  b1= (A+90)/45
  print(a1)
  print(b1)

elif A==-45:
  a1=0
  b1=1
  c1=0
  print(b1)

elif -45<A<0:
  b1= (0-A)/45
  c1= (A+45)/45
  print(b1)
  print(c1)

elif A==0:
  b1=0
  c1=1
  d1=0
  print(c1)

elif 0<A<45:
  c1= (45-A)/45
  d1= (A-0)/45
  print(c1)
  print(d1) 

elif A==45:
  c1=0
  d1=1
  e1=0
  print(d1)

elif 45<A<90:
  d1= (90-A)/45
  e1= (A-45)/45 
  print(d1)
  print(e1)

elif A==90:
  d1=0
  e1=1
  print(e1)

# Initialise numerator and denominator to zero
num = 0
den = 0

print("The following rules are being fired:")

if a>0 and a1>0:
  print("If distance is VN and angle is LT Then Deviation is A")
  temp = min(a, a1)
  num += (90-45*temp)*temp*0
  den += (90-45*temp)*temp

if a>0 and b1>0:
  print("If distance is VN and angle is AL Then Deviation is ART")
  temp = min(a, b1)
  num += (90-45*temp)*temp*45
  den += (90-45*temp)*temp

if a>0 and c1>0:
  print("If distance is VN and angle is A Then Deviation is AL")
  temp = min(a, c1)
  num += (90-45*temp)*temp*(-45)
  den += (90-45*temp)*temp

if a>0 and d1>0:
  print("If distance is VN and angle is ART Then Deviation is AL")
  temp = min(a, d1)
  num += (90-45*temp)*temp*(-45)
  den += (90-45*temp)*temp

if a>0 and e1>0:
  print("If distance is VN and angle is RT Then Deviation is A")
  temp = min(a, e1)
  num += (90-45*temp)*temp*0
  den += (90-45*temp)*temp

if b>0 and a1>0:
  print("If distance is NR and angle is LT Then Deviation is A")
  temp = min(b, a1)
  num += (90-45*temp)*temp*0
  den += (90-45*temp)*temp

if b>0 and b1>0:
  print("If distance is NR and angle is AL Then Deviation is A")
  temp = min(b, b1)
  num += (90-45*temp)*temp*0
  den += (90-45*temp)*temp

if b>0 and c1>0:
  print("If distance is NR and angle is A Then Deviation is RT")
  temp = min(b, c1)
  num += (45-22.5*temp)*temp*71
  den += (45-22.5*temp)*temp
  
if b>0 and d1>0:
  print("If distance is NR and angle is ART Then Deviation is A")
  temp = min(b, d1)
  num += (90-45*temp)*temp*0
  den += (90-45*temp)*temp

if b>0 and e1>0:
  print("If distance is NR and angle is RT Then Deviation is A")
  temp = min(b, e1)
  num += (90-45*temp)*temp*0
  den += (90-45*temp)*temp

if c>0 and a1>0:
  print("If distance is FR and angle is LT Then Deviation is A")
  temp = min(c, a1)
  num += (90-45*temp)*temp*0
  den += (90-45*temp)*temp

if c>0 and b1>0:
  print("If distance is FR and angle is AL Then Deviation is A")
  temp = min(c, b1)
  num += (90-45*temp)*temp*0
  den += (90-45*temp)*temp

if c>0 and c1>0:
  print("If distance is FR and angle is A Then Deviation is ART")
  temp = min(c, c1)
  num += (90-45*temp)*temp*45
  den += (90-45*temp)*temp

if c>0 and d1>0:
  print("If distance is FR and angle is ART Then Deviation is A")
  temp = min(c, d1)
  num += (90-45*temp)*temp*0
  den += (90-45*temp)*temp

if c>0 and e1>0:
  print("If distance is FR and angle is RT Then Deviation is A")
  temp = min(c, e1)
  num += (90-45*temp)*temp*0
  den += (90-45*temp)*temp

if d>0 and a1>0:
  print("If distance is VFR and angle is LT Then Deviation is A")
  temp = min(d, a1)
  num += (90-45*temp)*temp*0
  den += (90-45*temp)*temp

if d>0 and b1>0:
  print("If distance is VFR and angle is AL Then Deviation is A")
  temp = min(d, b1)
  num += (90-45*temp)*temp*0
  den += (90-45*temp)*temp

if d>0 and c1>0:
  print("If distance is VFR and angle is A Then Deviation is A")
  temp = min(d, c1)
  num += (90-45*temp)*temp*0
  den += (90-45*temp)*temp

if d>0 and d1>0:
  print("If distance is VFR and angle is ART Then Deviation is A")
  temp = min(d, d1)
  num += (90-45*temp)*temp*0
  den += (90-45*temp)*temp

if d>0 and e1>0:
  print("If distance is VFR and angle is RT Then Deviation is A")
  temp = min(d, e1)
  num += (90-45*temp)*temp*0
  den += (90-45*temp)*temp

# By using center of sums method, crisp output U  
U = num/den

print('The value of U is {}'.format(U))
