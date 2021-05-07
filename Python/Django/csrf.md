# csrf伪造
1. 登录网站1后，并且没有登出网站1，浏览器保存了网站1的 session
2. 通过使用浏览器保存的 session 向网站1发送模拟请求
3. Django 默认对 post 表单添加 csrf 防护
`'django.middleware.csrf.CsrfViewMiddleware',`
```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```
```html
<!-- 添加 {% csrf_token %} -->
<form method="POST" action="/booktest/login_Ajax/">
    {% csrf_token %}
    用户名:<input type="text" name="user" value="{{ user }}"><br/>
    密码:<input type="password" name="password"><br/>
    <input type="checkbox" name="remember">记住用户名
    <input type="submit" value="登录">
</form>
```
## 原理
* {% csrf_token %} 生成一个隐藏的 input,并生成对应 input 值的 cookie 参数（csrftoken）
* 通过对比 post 提交参数与 cookie 参数来判断是否为正常请求
```html
<input type="hidden" name="csrfmiddlewaretoken" value="EQhRqLM0ZgxjFDvcWV0P6yWo1V5hTixd1VejdF0143r54DtkHcr9YqjfXZkkechy">
```
