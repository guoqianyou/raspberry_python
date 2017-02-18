import socket
import time

from myloger import logger

_address=("192.168.1.18", 8899)


def connect_socket():
    sk = socket.socket()
    logger.info('客户端开始连接,地址：' + _address.__str__())
    conect_status = sk.connect_ex(_address)
    logger.info("socket 连接成功！" if conect_status == 0 else conect_status)
    while True :
        send_data="发发发发发发发发发发发发发发发发发" \
                  "发发发发发发发发发发发发发发发发发发发发发发发发发发发发" \
                  "发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发" \
                  "发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发" \
                  "发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发" \
                  "发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发" \
                  "发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发" \
                  "发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发" \
                  "发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发"
        sk.send(str(len(send_data.encode("utf-8"))).encode("utf-8"))
        time.sleep(0.5)
        sk.send(send_data.encode('utf-8'))
        logger.info("：发送成功!")
        data_size = sk.recv(1024)
        received_size = 0  # 记录接收长度
        received_data = b''  # 声明空bytes
        while received_size != int(data_size.decode()):
            data = sk.recv(1024)
            received_size += len(data)
            received_data += data  # 接收命令结果
        else:
            print(received_data.decode())
        logger.info("客户端：接受完成！")

if __name__ == "__main__":
    connect_socket()