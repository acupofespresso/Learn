# Cookie
* 存储在客户端
1. 字典类型存储    
2. cookie 可指定过期时间,默认为关闭浏览器后失效
3. 
## 设置 Cookie
* 需要一个 HTTPResponse 类的对象或者是它子类的对象
* HTTPResponseRedirect, JsonResponse
```python
def set_cookie(request):
    response = HttpResponse('setcookie')
    # 设置cookie信息
    response.set_cookie('num',1)
    return response
```
### 设置过期时效
```
# 通过秒数,设置7天时效
response.set_cookie('num',1,max_age=7*24*3600)
# 通过当前时间,设置7天时效
response.set_cookie('num', 1, expires=datetime.now() + datetime.timedelta(days=7))
```
### 实例
```
def login_Ajax(request):
    context = {
        'res':0,
    }
    u = request.POST.get('user')
    p = request.POST.get('password')
    r = request.POST.get('remember')
    print(u,p)
    print(r)
    if u == '123' and p == 'qwe':
        context['res'] = 1
        if r:
            response = JsonResponse(context)
            response.set_cookie('user',u,max_age=1*3600)
            return response
    return JsonResponse(context)
```
html
```
<script src="https://cdn.jsdelivr.net/npm/jquery@1.12.4/dist/jquery.min.js"></script>
  <script>
      $(function () {
            $('#btnAjax').click(function () {
                user = $('#user').val()
                password = $('#password').val()
                {# 使用 prop 判断 checked 状态 #}
                remember = $('#remember').prop('checked')
                $.ajax({
                    'url':'/booktest/login_Ajax/',
                    'type':'POST',
                    'data':{
                        'user':user,
                        'password':password,
                        'remember':remember,
                    },
                    'dataType':'json',
                    {# 同步请求 #}
                    {# 'async':false, #}
                }).success(function (data) {
                    alert(data.res)
                    if (data.res != 1){
                        $('#message').show().html('校验失败')
                    }else {
                        {# 重定向页面 #}
                        location.href = '/booktest/index'
                    }
                }).fail(function () {
                    alert('error')
                })
            })
      })
  </script>
  <style>
      #message{
          display: none;
          color: red;
      }
  </style>
```

# session
* 存储在服务器
1. 字典类型存储
2. 依赖于 cookie,唯一标识码保存在 sessionid cookie中
3. 可设置失效时间,默认两周后失效
表示当前的会话,当Django启用会话支持时可用

## 设置 session
```
request.session['key']='value'
```
```python
def set_session(request):
    request.session['u']='qqq'
    request.session['p']='aaa'
    # 设置失效时间 单位:秒
    # 设置为 0,则关闭浏览器后失效
    # 设置为 None,则两周后过期
    request.session.set_expiry(3600)
    return HttpResponse('setsession')
```
### 获取 session
```
request.session['key']
```
```python
def get_session(request):
    u = request.session['u']
    p = request.session['p']
    return HttpResponse(u+'<br/>'+p)
```