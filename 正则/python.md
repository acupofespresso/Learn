```python
# 导入re模块
import re

# match匹配
d = re.match(r'正则表达式','str')

# 获取返回结果
reData = d.group()
```
### 匹配方式
1. match
    * 从头匹配第一个符合条件的字符串
2. search
    * 从任意位置匹配第一个符合条件的字符串
3. findall
    * 从任意位置匹配全部符合条件的字符串
    * 从返回值取值; 返回值为 list
4. sub
    * 正则替换
    * re.sub(r'正则表达式','替换str','原str')
    * 替换str 可使用函数名代替,传入匹配到的字符串,返回值需为处理后的str类型的数据
    * 返回值为替换后的字符串
5. split
    * 切割
    * re.split(r'正则表达式','str')
    * 返回值为 list