'''
python中类的单继承演示
'''

class people:
    name = ''
    age = 0;
    #定义私有属性，私有属性在类外部无法直接进行访问
    _wight = 0;
    #定义构造方法：
    def __init__(self,name,age,wight):
        self.name = name;
        self.age = age;
        self._wight = wight;
    def speak(self):
        print("%s 说： 我 %d 岁." %(self.name,self.age))
#单继承示例
class student(people):
    grade = '';
    def __init__(self,name,age,wight,grade):
        people.__init__(self,name,age,wight)
        self.grade = grade
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级"%(self.name,self.age,self.grade))
s = student('ghe',12,123,11)
s.speak();