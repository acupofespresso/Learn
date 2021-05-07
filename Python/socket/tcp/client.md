```python
import socket

def send(s,t):
    # 使用套接字发送数据
    # 发送内容必须是 bytes 类型
    s.send(bytes(t.encode('utf-8')))

def clientRevc(s):
    # 接收数据 (单次接收最大字节数)
    reData = s.recv(1024)
    print(reData)
    # 尝试解码方式
    try:
        content = reData.decode("utf-8")
    except:
        content = reData.decode("GBK")
    print("content:" + content)

def main():
    # 创建socket
    # # （协议ipv4，tcp）
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(s)
    t = "输入发送内容,输入空结束"

    # ip = input("输入对方ip")
    # portNum = int(input("输入对方port"))
    ip = "192.168.1.105"
    portNum = 7788

    # 连接
    s.connect((ip,portNum))

    while t:
        op = int(input("1.接收; 2.发送; 3.退出"))
        try:
            op = int(op)
        except:
            print("重新输入")
            continue
        if op == 1:
            # 接收数据
            clientRevc(s)
        elif op == 2:
            # 发送数据
            t = input("输入发送内容")
            send(s,t)
        elif op == 3:
            break
        else:
            print("重新输入")
            continue

    # 关闭
    s.close()

if __name__ == '__main__':
    main()

```