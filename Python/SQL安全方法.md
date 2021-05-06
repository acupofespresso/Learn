```python
# python 安全方式(防注入)
# 构造参数列表
params = [参数]
sql = 'select * from 表名 where name=%s'
# 执行 sql 语句
cursor.execute(sql, params)
print(cursor.fetchall())
```