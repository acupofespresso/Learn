### `__iter__`
可迭代对象必须实现`__iter__`方法,`__iter__`需要return一个对象的引用,return对象必须实现`__iter__`,`__next__`
#### 方法一
```python
class classMate(object):
    def __init__(self):
        pass
    def add(self,content):
        pass
    def __iter__(self):
        return classIterator(self)
class classIterator(object):
    def __init__(self,obj):
        self.obj = obj
    def __iter__(self):
        pass
    def __next__(self):
        try:
            # 返回迭代数据
            return reData
        except:
            # 通过引发异常结束迭代
            raise StopIteration

```
#### 方法二
```python
class classMate(object):
    def __init__(self):
        pass
    def add(self,content):
        pass
    def __iter__(self):
        return classIterator(self)
    def __next__(self):
        try:
            # 返回迭代数据
            return reData
        except:
            # 通过引发异常结束迭代
            raise StopIteration
```
1. 判断对象是否为可迭代对象
2. 通过调用`__iter__`函数,得到`__iter__`的返回值(`__iter__`函数的返回值是一个迭代器)
3. `__iter__`返回值是一个实现`__iter__`和`__next__`的对象
4. 迭代时调用`__iter__`返回值的`__next__`对象