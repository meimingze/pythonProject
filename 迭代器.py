class MyNumber:

    ## 类似java中的构造器，定义类的基本属性，有参的构造函数
    def __iter__(self):
        self.a = 2;
        return self;
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1;
            return x;
        else:
            raise StopIteration;
ma = MyNumber()
my = iter(ma)
print(next(ma))
for x in ma:
    print(x);