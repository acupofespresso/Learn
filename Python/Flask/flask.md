# Flask
##
```python
# 导入Flask扩展
from flask import Flask
# 创建Flask应用程序实例
# 传入__name__,作为确定资源所在路径
app = Flask(__name__)

# 定义路由及视图函数
@app.route('/')
def hello_world():
    return 'Hello, World!'
@app.route('/luelue/')
def lue():
    return '<h1>略略</h1>'
    
if __name__ == '__main__':
    # 启动
    app.run()
```
## route 路由
* 使用 route() 装饰器来把函数绑定到 URL:
```python
@app.route('/')
def hello_world():
    return 'Hello, World!'
@app.route('/luelue/')
def lue():
    return '<h1>略略</h1>'
```
### 路由变量规则
* 通过把 URL 的一部分标记为 <variable_name> 就可以在 URL 中添加变量。标记的 部分会作为关键字参数传递给函数。通过使用 <converter:variable_name> ，可以 选择性的加上一个转换器，为变量指定规则
```python
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id
    
@app.route('/post/<float:f>')
def show_post(f):
    return 'f %d' % f

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)
```
|||
|:-:|:-:|
|string|（缺省值） 接受任何不包含斜杠的文本|
|int|接受正整数|
|float|接受正浮点数|
|path|类似 string ，但可以包含斜杠|
|uuid|接受 UUID 字符串|

### url_for() URL构建
* url_for() 函数用于构建指定函数的 URL。它把函数名称作为第一个 参数。它可以接受任意个关键字参数，每个关键字参数对应 URL 中的变量。未知变量 将添加到 URL 中作为查询参数。

### methods 
* 缺省情况下，一个路由只回应 GET 请求。 可以使用 route() 装饰器的 methods 参数来处理不同的 HTTP 方法
```
from flask import request

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()
```

## 静态文件
* 静态文件位于应用的 /static 中
* 使用特定的 'static' 端点就可以生成相应的 URL
```python
# static/style.css
url_for('static', filename='style.css')
```

## 模板
### Jinja2 模板
### 创建模板
* 在路由文件的根目录下,创建 templates 文件夹,在 templates 文件夹下,创建模板文件

### 渲染模板 render_template
* 使用 render_template() 方法可以渲染模板, 提供模板名称和要传递给模板的变量
```python
from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    # render_template('模板名', Key=Value)
    return render_template('hello.html', name=name)
```
```html
<!doctype html>
<title>Hello from Flask</title>
{% if name %}
  <h1>Hello {{ name }}!</h1>
{% else %}
  <h1>Hello, World!</h1>
{% endif %}
```
* Flask 会在 templates 文件夹内寻找模板
* 如果应用是一个模块， 模板文件夹应在模块旁边；
```
/application.py
/templates
    /hello.html
```
* 如果应用是一个包，模板文件应在包里面;
```
/application
    /__init__.py
    /templates
        /hello.html
```
### 模板的变量展示
`{{ 变量名 }}`
```python
@app.route('/luelue/<name>')
def lue(name):
    d = {
        'a':'aaa',
        'b':'bbb',
        'c':'ccc',
    }
    l = ['q','w','e','r']
    return render_template('test.html', name=name,d=d,l=l)
```

```html
<h1>测试模板:{{ name }}</h1>
<!--列表的取值-->
<h3>{{ l }}</h3>
<h3>{{ l.2 }}</h3>
<h3>{{ l[2] }}</h3>
<!--字典的取值-->
<h3>{{ d }}</h3>
<h3>{{ d.a }}</h3>
<h3>{{ d['c'] }}</h3>
```

### 模板的代码块
* 使用`{% %}`包裹
##### for
```
{% for foo in l %}
    <li>{{ foo }}</li>
{% endfor %}
```
##### if-else
```
{% if foo <= 2 %}
    <li>{{ foo }}</li>
{% endif %}
```


### 模板的注释
`{# 注释内容 #}`

## 文件上传
* 需在 HTML 表单中设置 enctype="multipart/form-data" 属性,否则浏览器将不会传送文件。
* 已上传的文件被储存在内存或文件系统的临时位置。可以通过请求对象 files 属性来访问上传的文件。
* 每个上传的文件都储存在这个 字典型属性中。这个属性基本和标准 Python file 对象一样，另外多出一个 用于把上传文件保存到服务器的文件系统中的 save() 方法。
```python
from flask import request

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/uploaded_file.txt')
    ...
```
* 文件上传之前在客户端系统中的名称，可以使用 filename 属性获取。
* 把客户端的文件名作为服务器上的文件名， 可以通过 Werkzeug 提供的 secure_filename() 函数
```python
from flask import request
from werkzeug.utils import secure_filename

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/' + secure_filename(f.filename))
    ...
```

## Cookies
* 访问 cookies ，可以使用 cookies 属性。可以使用响应 对象 的 set_cookie 方法来设置 cookies 。请求对象的 cookies 属性是一个包含了客户端传输的所有 cookies 的字典。在 Flask 中，如果使用 会话 ，那么就不要直接使用 cookies ，因为 会话 比较安全一些。
#### 读取 cookie
```python
from flask import request

@app.route('/')
def index():
    username = request.cookies.get('username')
    # use cookies.get(key) instead of cookies[key] to not get a
    # KeyError if the cookie is missing.
```
#### 存储 cookie
```python
from flask import make_response

@app.route('/')
def index():
    resp = make_response(render_template(...))
    resp.set_cookie('username', 'the username')
    return resp
```
*  cookies 设置在响应对象上。通常只是从视图函数返回字符串， Flask 会把它们 转换为响应对象。如果你想显式地转换，那么可以使用 make_response() 函数，然后再修改它。
* 使用 延迟的请求回调 方案可以在没有响应对象的情况下设置一个 cookie 。

## 重定向和错误
* 使用 redirect() 函数可以重定向。使用 abort() 可以 更早退出请求，并返回错误代码
```python
from flask import abort, redirect, url_for

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    abort(401)
    this_is_never_executed()
```
* 缺省情况下每种出错代码都会对应显示一个黑白的出错页面。使用 errorhandler() 装饰器可以定制出错页面
* render_template() 后面的 404 ，这表示页面对就的出错 代码是 404, 缺省情况下为 200
```python
from flask import render_template

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404
```
