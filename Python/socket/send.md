```python
import socket

# 发送数据
def send(s,ip,portNum,t):
    # 使用套接字发送数据
    # （发送的内容，(ip,端口)）
    # 发送内容必须是 bytes 类型
    s.sendto(bytes(t.encode('utf-8')), (ip, portNum))

# 接收数据
def recv(s):
    # 接收数据 (单次接收最大字节数)
    # 数据返回格式: (接收到的数据,(发送方ip,prot))
    reData = s.recvfrom(1024)
    print(reData)
    try:
        content = reData[0].decode("utf-8")
    except:
        content = reData[0].decode("GBK")
    ip = reData[1][0]
    prot = reData[1][1]
    print("content:" + content)
    print("ip: %s:%s" % (ip, prot))

def main():
    # 创建socket
    # # （协议ipv4，tcp）
    # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # udp
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print(s)
    t = "输入发送内容,输入空结束"
    # 绑定 ip,端口 信息
    # (ip地址,端口号) 端口号如省略,默认为本机的任何一个ip
    local_addr = ('',7789)
    s.bind(local_addr)
    ip = input("输入对方ip")
    portNum = int(input("输入对方port"))

    # 绑定端口 如不绑定默认随机端口发送数据
    # s.bind((ip,portNum))

    while t:
        t = input("输入发送内容")
        op = int(input("1.接收; 2.发送; 3.退出"))
        if op == 1:
            # 接收数据
            recv(s)
        elif op == 2:
            # 发送数据
            send(s,ip,portNum,t)
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