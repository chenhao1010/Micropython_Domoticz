# !/usr/bin/python
# -*- encoding: utf-8 -*-

"""
:开发者:   陈浩
:开发日期: 2018年11月19日
:邮箱地址: chenhao1010@163.com
:个人博客: https://www.chenhao-home.cn/
:开发芯片: ESP-32
:修订日志: 
          1、
          2、
          3、
          4、
"""



def network_connect(SSID, PASSWORD):
    """
    :param PASSWORD: WIFI password
    :param SSID: WIFI SSID
    :return:
    """
    import network
    station = network.WLAN(network.STA_IF)
    if station.isconnected():
        print("Network Already Connected !")
        return
    station.active(True)
    station.connect(SSID, PASSWORD)
    while not station.isconnected():
        pass
    print("Network Connection successful !")
    print(station.ifconfig())



