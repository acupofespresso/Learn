```
scp [可选参数] file_source file_target 
```
-r 递归复制    
-c 允许压缩    
-v 显示详情    
-P port 指定传输端口    
#### 指定 user 需输入密码
```
scp local_file user@ip:filePath  
```
#### 不指定 user 需输入账号和密码
```
scp local_file ip:filePath  
```
