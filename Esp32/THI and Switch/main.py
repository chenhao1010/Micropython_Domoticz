# !/usr/bin/python
# -*- encoding: utf-8 -*-
"""
:开发者:   陈浩
:开发日期: 2018年12月19日
:邮箱地址: chenhao1010@163.com
:个人博客: https://www.chenhao-home.cn/
:开发芯片: ESP-01S
:修订日志:
        1、温度及湿度一分钟更新一次
        2、开关状态0.2秒刷新一次
        3、wifi中断重新连接
        4、mqtt中断重新连接
        5、
"""

import gc
import time
import ujson
import urandom
import mqtt.simple
import drv.function
import drv.ConnectWIFI

SERVER = "www.chenhao-home.cn"  # MQTT服务器地址
PORT = 1883  # MQTT服务器端口
USER = "*****************"  # MQTT用户名
PASSWORD = "****************"  # MQTT密码
CLIENT_ID = (urandom.randrange(0, 10000000, 8)) # 客户端ID，随机8位数字
TOPIC1 = "domoticz/in"  # Domoticz接收主题
TOPIC2 = "domoticz/out"  # Domoticz发送主题
SSID = "*****************"  # WiFi SSID
WIFI_PASSWORD = "*******************"  # WiFi 密码
SW_idx = [2, 3, 4, 5]  # domoticz 开关IDX值
SW_Pin = [2, 4, 14, 15]  # 各个开关Pin引脚
THI_idx = [8]
THI_Pin = [13]  # 温湿度采集引脚

# 为紧急异常缓冲区分配RAM(ESP-32下使用)
micropython.alloc_emergency_exception_buf(100)
# 分配最小内存保证系统正常运行
gc.threshold(gc.mem_free() // 4 + gc.mem_alloc())
# WiFi开始连接
drv.ConnectWIFI.network_connect(SSID, WIFI_PASSWORD)
# THI计时
THI_time = 0


def switch_def(msg_dict_dict, idx_list, Pin_list):
    """
    :根据客户端发过来的JSON数据，判断IDX值是否包含在字典内，如果包含，根据nvalue的值判断GPIO接口高低。
    """
    msg_idx = msg_dict_dict["idx"]  # 取字典内IDX的值
    msg_nvalue = msg_dict_dict["nvalue"]  # 取字典内nvalue的值
    switch_dict = dict(zip(idx_list, Pin_list))  # 合并IDX与Pin列表为字典
    if msg_idx in switch_dict and msg_nvalue == 1:  # 判断switch_dict字典内是否包含idx
        drv.function.switch_on(switch_dict[msg_idx])  # 根据idx值取switch_dict内的引脚元素
        conn.publish(Topic_In, sw_on_data)
    elif msg_idx in switch_dict and msg_nvalue == 0:
        drv.function.switch_off(switch_dict[msg_idx])
    else:
        print(msg_dict_dict)


def sub_cb(topic, msg):
    """
    :取MQTT服务发送来的json数据,然后判断GPIO口的高低。
    """
    msg_str = msg.decode()  # 将byte转换为str
    msg_dict = ujson.loads(msg_str)  # 将JSON转换为字典
    if "switchType" in msg_dict:
        switch_def(msg_dict, SW_idx, SW_Pin)
    else:
        print(msg_dict)

 
def connect():
    """
    :判断MQTT服务器状态，如果域名或者IP地址错误，则提示ERROR，如果无法打开
    :服务器，则提示Not Open,如果MQTT服务器上线后，自动重新连接。
    """
    global conn
    while True:
        try:
            conn = mqtt.simple.MQTTClient(CLIENT_ID, SERVER, PORT, USER, PASSWORD, 60)
            conn.set_callback(sub_cb)
            conn.connect()
            conn.subscribe(TOPIC2)
            # 打印服务器地址以及订阅主题
            print("Connected to %s, subscribed to %s topic" % (SERVER, TOPIC1))
            break
        except IndexError:
            print("MQTT Server %s ERROR!" % (SERVER))
            time.sleep(1)
        except OSError:
            print("MQTT Server %s Not Open!" % (SERVER))
            time.sleep(3)


def THI_num():
    try:
        THI = drv.function.DHT22(THI_Pin[0])
        return THI
    except OSError:
        print("THI ERROR!")
        THI = [44.0, 44.0]
        return THI


def main():
    """
    :return:
    """
    global THI_time
    connect()
    # 总循环
    while True:
        try:
            if THI_time == 120:
                THI_temp = THI_num()
                data = {
                   "idx": THI_idx[0],
                   "nvalue": 0,
                   "svalue": "%.2f; %.2f; 1" % (THI_temp[0], THI_temp[1])
                }
                conn.publish(TOPIC1, ujson.dumps(data))
                THI_time = 0
            conn.check_msg()
            THI_time += 1
            time.sleep(0.2)
        except ValueError:  # 如果传回JSON字符串有问题自动忽略并运行垃圾回收函数
            gc.collect()
        except OSError:  # MQTT服务器中断后自动重新连接
            gc.collect()
            connect()
        continue


if __name__ == "__main__":
      main()
