# 查询
|函数|功能|返回值|说明|
|:--:|:--:|:----:|:--:|
|get|查询并返回满足条件的一条数据(只能有一条符合条件,否则报错)|模型类对象|可写查询条件<br>1.如查询到多条数据,则抛出异常:MultipleObjectReturned<br>2.如没有查询到数据,则抛出异常:DoesNotExist|
|all|返回模型类对应表中的全部数据|QuerySet类型|查询集|
|filter|返回满足条件的数据|QuerySet类型|可写查询条件|
|exclude|返回不满足条件的数据|QuerySet类型|可写查询条件|
|rder_by|对查询结果排序|QuerySet类型|参数:对哪个字段进行排序<br>默认升序,字段前加`-`降序<br>BookInfo.objects.all().order_by('字段1','字段2')|

## get, filter, exclude 条件使用
* 方法示例:模型类属性名__条件名=值

|条件名|功能|
|:-:|:-:|
|exact|判等|
|contains|模糊查询(包含)|
|startswith|模糊查询(开头为...)|
|endswith|模糊查询(结尾为...)|
|isnull|不为空:=False, 为空:=True|
|in|范围查询:=(), =[]|
|gt|比较查询(大于)|
|lt|比较查询(小于)|
|gte|比较查询(大于等于)|
|lte|比较查询(小于等于)|
|date|日期查询:=(年,月,日)|
|yea|日期查询(年)|
|month|日期查询(月)|
|day|日期查询(日)|


## Q对象
* &(与)  |(或)  ~(非)
* 多个条件默认为 &
```
# 与
BookInfo.objects.filter(条件1,条件2)
BookInfo.objects.filter(Q(条件1)&Q(条件2))
# 或
BookInfo.objects.filter(Q(条件1)|Q(条件2))
# 非
BookInfo.objects.filter(~Q(条件1))
```

## F对象
* 类属性间的比较
* 可进行算术运算
```
# 查询阅读量大于评论量的数据
BookInfo.objects.filter(bookRead__get=F('bookComment'))

# 查询阅读量大于评论量两倍的数据
BookInfo.objects.filter(bookRead__get=F('bookComment')*2)
```

## 聚合
* 对查询结果进行聚合操作
* sum, count, avg, max, min
* 调用 aggregate 函数,返回一个字典
```
from django.db.models import Sum,Count,Max,Min,Avg
BookInfo.objects.all.count()
BookInfo.objects.filter(id_gt=3).sum()

```

## 特性
### 查询集特性
1. 惰性查询：只有实际查询**集**中的数据时，才会对数据库进行真正的查询
2. 缓存：当使用同一个**查询集**时，第一次对数据库进行真正的查询之后，会把结果缓存起来，之后再使用这个**查询集**时，使用的是缓存中的结果     
### 限制查询集
1. 可对一个查询集进行取下标或切片操作
    * 对一个查询集进行切片操作会产生一个新的查询集。
    ```
    book = BookInfo.objects.all()
    # 取前3条
    book1 = book[0:3]
    # 取第一条
    book[0]
    book[0:1].get()
    ```
2. exists 判断一个查询集中是否有数据(True/False)


# 插入/更新
调用`save()`方法实现插入和更新    
插入: BookInfo.objects.create(字段名1=值,字段名2=值)

# 删除
调用`delete()`方法实现删除