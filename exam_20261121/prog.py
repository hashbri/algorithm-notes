w,h,v=map(int,input().split())
for i in range(h):
    print('Q'*w)
for x in range(w):
    print('Q'*(w+v))