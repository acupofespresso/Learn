## 添加账号
```
create user 'crawl'@'192.168.1.%' identified by 'crawlpi';
<!--create user '账号'@'ip' identified by '密码';-->
```
## 赋权
```
<!--grant usage on 库名.表名 to '账号'@'ip' with grant option;-->
grant usage on crawl.* to 'crawl'@'192.168.1.%' with grant option;
<!--grant 操作权限 on 库名.表名 to '用户'@'ip' with grant option-->
grant select,insert,update,delete,create,drop on crawl.* to 'crawl'@'192.168.1.%' with grant option;
grant ALL PRIVILEGES ON crawl.* to 'crawl'@'192.168.1.%' with grant option;
```
## 刷新
```sql
flush privileges
```
查看 mysql.user 表是否新增用户