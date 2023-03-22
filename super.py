'''
super()函数用于调用父类的一个方法
super()是用来解决多重继承问题的，直接用类名调用父类方法在使用单继承的时候没有问题，但是如果使用多继承涉及到查找顺序（MRO）、重复调用（钻石继承）等种种问题
MRO 就是类的方法解析顺序表, 其实也就是继承父类方法时的顺序表。
'''


class FooParent(object):
    def __init__(self):
        self.parent = 'I\'m the parent.'
        print('Parent')

    def bar(self, message):
        print("%s from Parent" % message)


class FooChild(FooParent):
    def __init__(self):
        # super(FooChild,self) 首先找到 FooChild 的父类（就是类 FooParent），然后把类 FooChild 的对象转换为类 FooParent 的对象
        super(FooChild, self).__init__()
        print('Child')

    def bar(self, message):
        super(FooChild, self).bar(message)
        print('Child bar fuction')
        print(self.parent)


if __name__ == '__main__':
    fooChild = FooChild()
    fooChild.bar('HelloWorld')