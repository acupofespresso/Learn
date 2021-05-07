# 安装部署
下载 https://www.oracle.com/java/technologies/javase/javase-jdk8-downloads.html 
```
# ARM 32
https://www.oracle.com/webapps/redirect/signon?nexturl=https://download.oracle.com/otn/java/jdk/8u281-b09/89d678f2be164786b292527658ca1605/jdk-8u281-linux-arm32-vfp-hflt.tar.gz
# ARM 64
https://www.oracle.com/webapps/redirect/signon?nexturl=https://download.oracle.com/otn/java/jdk/8u281-b09/89d678f2be164786b292527658ca1605/jdk-8u281-linux-aarch64.tar.gz

# 64
https://www.oracle.com/webapps/redirect/signon?nexturl=https://download.oracle.com/otn/java/jdk/8u281-b09/89d678f2be164786b292527658ca1605/jdk-8u281-linux-x64.tar.gz

```
解压：`tar -xvf jdk-8u271-linux-arm32-vfp-hflt.tar.gz`  
配置环境变量：`vim /etc/profile`  
文件末尾添加：  
```
JAVA_HOME=/home/pi/software/jdk1.8.0_271
CLASSPATH=.:$JAVA_HOME/lib/tools.jar:$JAVA_HOME/lib/dt.jar
PATH=$JAVA_HOME/bin:$PATH
export JAVA_HOME
export PATH
export CLASSPATH
```  
重启：`reboot`