#### 运行jar包
```
// java -jar jar包 
java -jar YoudaoFanyiCrawl.jar 
```
#### 指定程序入口运行jar包
```
// java -cp jar包 入口路径
java -cp YoudaoFanyiCrawl.jar crawl.netEase.ja.YoudaoFanyiEs
```
#### 指定编码运行jar包解决乱码问题
```
// java -Dfile.encoding=编码 -cp jar包 入口路径
java -Dfile.encoding=utf-8  -cp YoudaoFanyiCrawl.jar crawl.netEase.ja.YoudaoFanyiEs
```