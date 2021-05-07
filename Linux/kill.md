杀子进程
```
ps -ef | grep -i twitter | awk '{print $2}' | xargs kill -9
```