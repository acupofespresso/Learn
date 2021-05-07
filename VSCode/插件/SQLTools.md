### 连接数据库报错
##### 不支持 mysql 8.0+ 默认的密码加密方式
```
# 修改用户密码为指定加密方式
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'root';
```
