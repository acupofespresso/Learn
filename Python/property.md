# property
#### 可用于实现 get/set 方法
#### 创建方式
* 装饰器: 在方法上加上装饰器 @property
    1. 获取:
    ```python
    class test:
        @property
        def price(self):
            return 100
    t = test()
    # 获取属性
    a = t.price
    print(a)
    ```
    2. 修改:
    ```python
    class test:
        @price.setter
        def price(self,value):
            return 100
    t = test()
    # 传参修改属性 调用setter
    a = t.price = 123
    print(a)
    ```
    3. 删除:
    ```python
    class test:
        @price.deleter
        def price(self):
            return 100
    t = test()
    # 删除属性 调用deleter
    del t.price
    ```
* 类属性: 在类中定义值为 property(方法名) 对象的类属性 

## @property
* 调用方法时不需要在方法后写`()`
* 以调用属性的方式调用方法,提高可读性

```python
class test:
    @property
    def size(self):
        return 100
t = test()
s = t.size
print(s)
```

## property()
```python
class test:
    NAME = '宥宥'
    # 获取
    def getName(self):
        return self.NAME
    # 修改
    def setName(self,name):
        self.NAME = self.NAME + name
        return self.NAME
    # 删除
    def delName(self):
        return self.NAME
    # property(获取方法名,修改方法名,删除方法名,'文档信息')
    name = property(getName,setName,delName,'文档信息')

t = test()
# 获取
print(t.name)
# 修改
t.name = '夙夙'
print(t.name)
# 获取文档信息
print(test.name.__doc__)
# 删除
del t.name

```