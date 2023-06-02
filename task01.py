def init():
    global a
    b=[]
    for i in range(a):
       b.append("hello world")
    for j in range(len(b)):
        print(b[j])
                      
a=int(input())
init()

