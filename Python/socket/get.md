```python
import socket

def main():
    # 创建socket
    # # （协议ipv4，tcp）
    # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # udp
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print(s)

    # 绑定 ip,端口 信息
    # (ip地址,端口号) 端口号如省略,默认为本机的任何一个ip
    local_addr = ('',7788)
    s.bind(local_addr)

    while True:
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
        print("content:"+content)
        print("ip: %s:%s"%(ip,prot))

    # 关闭
    s.close()

if __name__ == '__main__':
    main()

```