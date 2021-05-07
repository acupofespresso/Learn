```python
import socket

def send(s,t):
    # 使用套接字发送数据
    # 发送内容必须是 bytes 类型
    s.send(bytes(t.encode('utf-8')))

def recv(client_s,clientAddr):
    # 接收数据 (单次接收最大字节数)
    reData = client_s.recv(1024)
    # 尝试解码方式
    try:
        content = reData.decode("utf-8")
    except:
        content = reData.decode("GBK")
    # 取ip,prot
    ip = clientAddr[0]
    prot = clientAddr[1]
    print("content:" + content)
    print("ip: %s:%s" % (ip, prot))
    return client_s

def main():
    # 创建socket
    # # （协议ipv4，tcp）
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(s)
    t = "输入发送内容,输入空结束"

    # 绑定端口 如不绑定默认随机端口发送数据
    s.bind(('',7788))

    # 监听
    s.listen(128)

    # 等待建立连接
    # 数据返回格式: (接收到的数据,(新的套接字,客户端ip,port信息))
    client_s, clientAddr = s.accept()
    while t:
        op = input("1.接收; 2.发送; 3.退出; 4.关闭套接字")
        try:
            op = int(op)
        except:
            print("重新输入")
            continue
        if op == 1:
            # 接收数据
            recv(client_s,clientAddr)
        elif op == 2 and client_s:
            # 发送数据
            t = input("输入发送内容")
            send(client_s,t)
        elif op == 3:
            break
        elif op == 4:
            if client_s:
                client_s.close()
                # 等待建立连接
                # 数据返回格式: (接收到的数据,(新的套接字,客户端ip,port信息))
                client_s, clientAddr = s.accept()
                continue
        else:
            print("重新输入")
            continue

    # 关闭
    s.close()

if __name__ == '__main__':
    main()


```