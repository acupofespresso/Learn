`[a*2 for x in range(10)]`

`(a*2 for x in range(10))`

## yield
* 如果函数中有`yield`语句,该函数就是一个生成器模板
* 如果调用该函数时发现`yield`语句时,不调用函数,而是创建一个生成器对象
* 当执行到`yield`语句时,会先将`yield`语句后的值返回,然后从`yield`所在的位置继续执行
* 该函数结束时的返回值,返回到异常对象的 value
* 通过`next()`迭代
    1. 启动迭代 
* 通过`send()`迭代
    1. `send()`可传参
    2. 使用`send()`前,需先使用`next()`启动迭代
```python
class classMate(object):
    def __init__(self):
        self.name = list()
        self.maxCount = 0
        self.objCount = 0
    def add(self,content):
        self.name.append(content)
        self.maxCount += 1
    def getName(self):
        while self.objCount < self.maxCount:
            # print(self.name[self.objCount])
            yield self.name[self.objCount]
            self.objCount += 1
        # 当迭代结束时返回到异常对象的 value
        return 'END'
classmate = classMate()
classmate.add('qwe')
classmate.add('zxc')
classmate.add('asd')

gName = classmate.getName()
# next() 方式
print(next(gName))
# 迭代取值
while True:
    try:
        # send() 方式
        print(gName.send('send传参'))
    except Exception as e:
        print(e.value)
        breakalue)
        break
```