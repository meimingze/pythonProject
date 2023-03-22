import sys
def fibonaci(m):
    a,b,counter = 0,1,0
    while True:
        if(counter > m):
            return
        yield a;
        a,b = b , a+b;
        counter += 1;
f = fibonaci(10) # f 是一个迭代器，由生成器返回生成
while True:
    try:
        print(next(f),end=" ")
    except StopIteration:
        sys.exit()