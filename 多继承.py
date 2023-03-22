class people:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0

    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说: 我 %d 岁。" % (self.name, self.age))


# 单继承示例
class student(people):
    grade = ''

    def __init__(self, n, a, w, g):
        # 调用父类的构函
        people.__init__(self, n, a, w)
        self.grade = g

    # 覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))
class asda():
    topic = ''
    def __init__(self,t):
        self.topic = t

    def speak(self):
        print("我叫我是一个演说家，我演讲的主题是 %s" % (self.topic))
class sample(student,asda):
    a = ''
    name = ''
    def __init__(self,n,a,w,g,t):
        student.__init__(self,n, a, w, g)
        asda.__init__(self,t)
test = sample('Tim',15,84,4,"pyhton");
test.speak()