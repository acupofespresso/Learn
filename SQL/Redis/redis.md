# 安装
## window
redis-server.exe redis.windows.conf  
redis-server --service-start  
redis-server --service-stop  
redis-cli

**redis**字符串限制在**512M**

# 命令
||||
|:-:|:-:|:-:|
|APPEND|在末尾追加|APPEND key value|
|BITCOUNT|||
|BITFIELD|||
|BITOP|||

## APPEND key value
如**key**已经存在，且为字符串，则将**value**追加到原来**value**的末尾  
如**key**不存在，则创建空字符串的**key**，然后执行追加操作
### 返回值
Integer reply  
返回**APPEND**后，**value**的长度
### 模式——节拍序列（Time series）
***

## BITCOUNT key [star end]
统计字符串被设置为1的bit数
***

## BITFIELD
***

## BITOP
***

## BITPOS
***

## DECR key
如**key**对应的**value**存在，且能够表示成数字，则减一  
如**key**对应的**value**不存在，则先将**value**置为**0**，然后再减一    
如**key**对应的**value**是错误类型，或不能表示成数字，则返回错误
### 返回值
数字  
操作后的**value**
***

## DECRBY key decrement
如**key**对应的**value**存在，且能够表示成数字，则减**decrement**  
如**key**对应的**value**不存在，则先将**value**置为**0**，然后再减**decrement**  
如**key**对应的**value**是错误类型，或不能表示成数字，则返回错误
### 返回值
数字  
操作后的**value**
***

## GET key
**GET**只处理**string**类型的**value**  
如**key**不存在，返回**nil**  
如**key**对应的**value**不是**string**，就返回错误
### 返回值
simple-string-reply  
**key**对应的**value**
***

## GETBIT key offset
***

## GETRANGE key start end
返回**key**对应**value**下标从**start**开始，到**end**结束的字串（**0**开始）  
可通过负数来表示下标从尾部开始（**-1**为最后一个字符）  
处理超过**value**范围的请求时，返回结果限制在**string**内
### 返回值
bulk-reply


## GETSET key value
用**新value**替换**key**对应的**旧value**，并返回**旧value**  
如**key**存在，但对应的**value**不是字符串，则返回错误
如**key**不存在，则返回**nil**
### 返回值
bulk-string-reply   
返回**key**对应的**旧value**  
如**key**不存在，则返回**nil**
***

## INCR key
对**key**对应的**value**执行原子的加一  
如**key**对应的**value**存在，且能表示为数字，则加一  
如**key**对应的**value**存在，但不能表示为数字，则返回错误  
如指定的**key**不存在，则先创建**key**，并将对应**value**的值置为**0**，然后执行**INCR**操作  
### 返回值
Integer-reply  
返回执行后**value**的值
***

## INCRBY key increment
对**key**对应的**value**执行加**increment**  
如**key**对应的**value**存在，且能表示为数字，则加**increment  
如**key**对应的**value**存在，但不能表示为数字，则返回错误  
如指定的**key**不存在，则先创建**key**，并将对应**value**的值置为**0**，然后再执行操作
### 返回值
Integer-reply  
增加后**value**的值
***

## MGET key [key ...]
返回所有指定**key**的**value**  
如所指定**key**不对应**string**或不存在，则返回**nil**
### 返回值
array-reply  
所有指定**key**对应**value**的**list**
***

## MSET key value [key value ...]
原子的设置所有指定**key**的**value**，如指定**key**的**value**已存在，则覆盖  
### 返回值
simple-string-reply  
返回**OK**，**MSET**不会失败
***

## MSETNX key value [key value ...]
原子的设置所有指定**key**的**value**，如指定的**key**已存在，则**MSETNX**一个操作都不会执行
### 返回值
Integer-reply
所有**key**被**set**，返回**1**  
没有**key**被**set**，返回**0**
***

## SET key value [EX seconds] [PX milliseconds] [NX|XX]
设置指定**key**的**value**  
如指定**key**已存在**value**，则覆盖  
当**SET**执行成功后，之前设置的过期时间都将失效  
### 选项
* EX seconds 以秒为单位设置**key**的过期时间
* PX milliseconds 以毫秒为单位设置**key**的过期时间
* NX 只有**key**不存在时才会设置**key**的**value**
* XX 只有**key**已经存在时才会设置**key**的**value**
### 返回值
simple-string-reply  
如**SET**正常执行，则返回**OK**，否则返回**nil**（如加了**NX**但没有设置条件）
### 设计模式
SET resource-name anystring NX EX max-lock-time  
是一种用**Redis**实现锁机制的简单方法  
如命令返回**OK**，则客户端获得锁  
如命令返回**nil**，则客户端在一段时间后重新尝试，并可通过**DEL**命令释放锁  
客户端加锁后，如没有主动释放，则会在过期之后自动释放  
#### 可通过如下优化是上面的锁系统变得更加鲁棒：
* 不设置固定的字符串，而设置随机的大字符串，称为**token**
* 通过脚步删除指定锁的**key**，而不是**DEL**命令  
###### 通过优化可避免**A**客户端获得的锁（键key）由于过期时间到了已经被**redis**服务器删除，但**A**客户端仍然去执行**DEL**命令，而**B**客户端已经在**A**设置的过期时间之后重新获取了这个同样**key**的锁，那么**A**执行**DEL**就会释放**B**加载好的锁。
### NX
如**key**不存在对应的**value**，则设置**key**的**value**，否则不做任何操作  
#### 返回值
Integer reply  
如**key**被设置了，则返回**1**，否则返回**0**
#### 设计模式：使用**!SETNX**加锁

#### 处理死锁
***


## SETBIT key offset value
***

## SETRANGE key offset value
从**key**的下标**offset**处开始用**value**覆盖对应的**string**  
如**offset**要覆盖的长度比**string**长，则在**string**后面补**0**以达到**offset**  
### 模式
通过**SETRANGE**和**GETRANGE**命令，可以把**redis**字符串当成线性数组
### 返回值
Integer-reply  
修改后字符串的长度  
***

## STRLEN key
返回**key**的**string**类型**value**的长度  
如**key**对应非**string**类型，则返回错误
### 返回值
Integer-reply  
**key**对应的字符串**value**的长度，或**0**（**key**不存在）
***

# 请求/响应协议和RTT
**redis**是基于**客户端-服务端模型**以及**请求/响应协议**的**TCP**服务  
请求遵循：
* 客户端向服务端发送查询请求，并监听**Socker**返回，通常以阻塞模式，等待服务端响应  
* 服务端处理命令，并将结果返回给客户端  
数据包从客户端到达服务器，并从服务器返回数据回复客户端，这个时间称为**RTT**（Round Trip Time - **往返时间**）
## redis 管道（Pipelining）
将多个命令发送到到服务器，而不用等待回复，最有在一个步骤中读取该答复  
POP3协议通过实现这个功能，加快了从服务器下载新邮件的过程
***

# Pub/Sub
## 发布/订阅 解耦
* 发布者发布消息到不同的频道，不需要知道什么样的订阅者订阅  
* 订阅者对一个或多个频道感兴趣，只需接收感兴趣的消息，不需要知道什么样的发布者发布  
* 订阅和取消订阅的响应被封装在发送的消息中，客户端只需读一个连续的消息流，其中第一个元素表示消息类型
## 推送消息的格式
消息是有三个元素的多块响应  
* 第一个元素是消息类型  
1. subscribe：表示成功订阅到响应的第二个元素提供的频道。第三个参数代表我们现在订阅频道的数量
2. unsubscribe：表示成功取消订阅到响应的第二个元素提供的频道。第三个参数代表目前订阅频道的数量。当最后一个参数为**0**时，则不在订阅任何频道。当在**Pub/Sub**以外状态，客户端可以发出任何**redis**命令
3. message：是另一个客户端发出的发布命令结果，第二个元素是来源频道的名称，第三个参数是实际消息的内容

## 数据库与作用域

## 模式匹配订阅
