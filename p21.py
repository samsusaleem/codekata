y1,s1=map(int,input().split(' '))
y2,s2=map(int,input().split(' '))
y3,s3=map(int,input().split(' '))
if (y1==y2 and y2==y3) or(s1==s2 and s2==s3):
    print("yes")
else:
    print("no")
