### 创建进程池
```python
# Pool(最大进程数)
p = Pool(3)
for i in range(10):
    # p.apply_async(函数名,(参数,))
    p.apply_async(worker,(i,))
# 关闭
p.close()
# 等待p中所有子进程执行完成
p.join()
```