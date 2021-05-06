```python
class File():
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode
    # 执行 with 时调用__enter__并返回返回值
    def __enter__(self):
        self.f = open(self.name,self.mode)
        return f
    # with 执行完毕,一定会执行__exit__
    def __exit__(self, *args):
        self.f.close()
with File('123.txt', 'w') as f:
    f.write('ewqqwesda')
```


```python
from contextlib import contextmanager

@contextmanager
def contextOpen(path, mode):
    f = open(path,mode)
    # yield之前相当于 __enter__
    yield f
    # yield之后相当于 __exit__
    f.close()
with contextOpen('123.txt','w') as f:
    f.write('dsasdasdw')
```