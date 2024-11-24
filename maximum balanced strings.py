'''

'''

a=input().strip()
i=0
b=""
c=""
while(i<len(a)):
  
  if(a[i]=='R'):
    x=0
    b+='('
    while(i<len(a) and a[i]=='R'):
      x+=1
      i+=1
      b+='R'
    y=0
    while(i<len(a) and a[i]=='L' and y<x):
      b+='L'
      i+=1
      y+=1
    b+=')'
  else:
    x=0
    b+='('
    while(i<len(a) and a[i]=='L'):
      x+=1
      i+=1
      b+='L'
    y=0
    while(i<len(a) and a[i]=='R' and y<x):
      b+='R'
      i+=1
      y+=1
    b+=')'
print(b)