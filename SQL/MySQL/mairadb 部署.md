### 下载安装
`sudo apt-get install mysql`
`sudo apt-get install mariadb-server`    
`sudo mysql -uroot -p`    
`mysql -uroot -p`    
### 配置远程连接
#### 修改配置文件
`sudo vim /etc/mysql/ mariadb.conf.d/50-server.cnf `
![](https://note.youdao.com/yws/api/personal/file/00DF682E73FB47A4B35EC21AB07F7644?method=download&shareKey=80dbbc8d1ee03381a37b58b16a0b94d9)

#### 修改root密码
```
ALTER user 'root'@'localhost' IDENTIFIED BY 'newpassward'; //newpassward 新密码`
# 指定密码加密方式
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'root';
```
#### 添加账户
`  mysql -uroot -p`
```sql
USE mysql
# create user '账号'@'ip' identified by '密码';
create user 'crawl'@'192.168.1.%' identified by 'crawlpi';
# grant usage on 库.表 to '账号'@'ip' with grant option;
grant usage on crawl.* to 'crawl'@'192.168.1.%' with grant option;
# 赋予部分权限 （grant 权限 on 库.表 to '账号'@'ip' with grant option;）
grant select,insert,update,delete,create,drop on crawl.* to 'crawl'@'192.168.1.%' with grant option;
# 赋予全部权限
grant ALL PRIVILEGES ON crawl.* to 'crawl'@'192.168.1.%' with grant option;
SELECT host,user FROM user;
# 刷新
flush privileges;
  ```

#### 重启mysql
`sudo service mysql restart`    
`more conf.d/mysql.cnf`
