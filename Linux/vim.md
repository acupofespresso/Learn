### 缩进
* `>>` 向右缩进
* `<<` 向左缩进
#### 批量缩进
* `V` 进入可视块选中缩进代码    
* `<` 左缩进    
* `>` 右缩进

### 重复
* `.` 重复上次命令

### 查找
* `/` 查找
* `n` 向下查找
* `N` 向上查找

### 查找并替换
#### 命令格式
* `:%s///g`
#### 全局替换
* `:%s/查找内容/替换内容/g`
##### 确认替换
* `:%s/查找内容/替换内容/gc`
    * y 替换
    * n 不替换
    * a 全部替换
    * q 退出
    * l 替换后退出
    * ctrl+E 向下翻页
    * ctrl+Y 向上翻页

### 批量注释
* `^`或`0` 来到行首
* `V` 进入可视块选中注释行首 
* `I` 进入编辑模式
* 输入注释符
* Esc 退出编辑模式

### vim中文件操作
#### 编辑其他文件
* `:e 文件名`
#### 创建文件
* `:n 文件名`
#### 另存为
* `:w 文件名`

### 分屏命令
* `:sp 文件名` 水平分屏
* `:vsp 文件名` 垂直分屏
#### 切换窗口
* `CTRL+w` 进入窗口控制
    * `w` 切换窗口
    * `r` 交换窗口
    * `c` 关闭窗口
    * `q` 退出窗口
    * `o` 关闭其他窗口