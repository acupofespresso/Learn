## 克隆
`git clone 'url'`
***
## 分支
### 查看分支
`git branch -a`
### 创建分支
`git branch 分支名`
### 切换分支
`git checkout 分支名`
### 创建并切换分支
`git checkout -b 分支名 origin/分支名`
***
## 合并
### 单路快进合并
```
# 切换到主分支
git checkout master
git merge 开发分支名
```
***

## 添加内容
`git add .`
### 查看状态
`git status`
***

### 添加内容描述
`git commit -m 描述`
### 重新提交 ()
`git commit --amend`
```
强制提交
git push -uf
```
***

### 撤销暂存
`git reset HEAD <file>`

### 撤销修改
`git checkout -- <file>`

### 忽略提交指定内容
`touch .gitignore`
***
### push
`git push`
### pull
`git pull`
***

设置用户名    
`git config --global user.name "CWT"`    
设置邮箱    
`git config --global user.email "wenteng.cui@percent.cn"`    
查看    
```
git config user.email
git config user.name
```
***
## clone 私有仓库
设置公钥    
`ssh-keygen -t rsa -C "邮箱"`    
查看公钥(复制公钥到git的ssh公钥)    
`cat ~/.ssh/id_rsa.pub`    
测试链接    
```
ssh -T git@gitee.com
ssh -T git@github.com
```    
***

## 问题：
##### Key is invalid. You must supply a key in OpenSSH public key format github     
* 直接赋值粘贴 .ssh的文件会破坏格式
需要打开 git bash    
回车后就复制到剪切板了，到github添加ssh keys的地方直接就能粘贴上    
`clip < ~/.ssh/id_rsa.pub`
***
##### clone 失败
1. 用户权限不够
2. 登录用户错误, 修改Windows用户凭证
***
##### fatal: unable to access 'https://github.com/xxxx.git/': OpenSSL SSL_read:Connection was reset, errno 10054
执行
```
git config --global http.sslVerify "false"
```
