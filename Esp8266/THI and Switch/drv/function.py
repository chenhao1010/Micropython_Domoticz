# !/usr/bin/python
# -*- encoding: utf-8 -*-

"""
:开发者:   陈浩
:开发日期: 2018年11月19日
:邮箱地址: chenhao1010@163.com
:个人博客: https://www.chenhao-home.cn/
:开发芯片: ESP-01S
:修订日志: 
          1、
          2、
          3、
          4、
"""
import dht
import time
import onewire
import ds18x20
from machine import Pin


# 开关
def switch_off(pin_num):
    """
    :param pin_num:
    :return:
    """
    Pin(pin_num, Pin.OUT).value(1)


def switch_on(pin_num):
    """
    :param pin_num:
    :return:
    """
    Pin(pin_num, Pin.OUT).value(0)


# 流水灯
def led_play(Pin_list):
    """
    :param Pin_list: 
    """
    for num in Pin_list:
      switch_on(num)
      time.sleep(2)
      switch_off(num)
      time.sleep(0.2)


# 温度（ds18x20_工作电压3.3V）
def ds18x20(pin_num):
    """
    :param pin_num:
    :return:
    """
    ow = onewire.OneWire(Pin(pin_num))
    ds = ds18x20.DS18X20(ow)
    roms = ds.scan()
    ds.convert_temp()
    for rom in roms:
        temp_num = ds.read_temp(rom)
        return round(temp_num, 2)


# 温湿度（DHT22_工作电压5V）
def DHT22(pin_num):
    """
    :param pin_num:
    :return:
    """
    THI = dht.DHT22(Pin(pin_num))
    THI.measure()
    THI_List = [THI.temperature(), THI.humidity()]
    return THI_List

def DHT11(pin_num):
    """
    :param pin_num:
    :return:
    """
    THI = dht.DHT11(Pin(pin_num))
    THI.measure()
    THI_List = [THI.temperature(), THI.humidity()]
    return THI_List


# 人体感应(工作电压5V）
def detectMotion(pin_num):
    """
    :param pin_num:
    :return:
    """
    motion_detect = Pin(pin_num, Pin.IN, Pin.PULL_UP)
    return motion_detect.value()


# 声音触发模块（工作电压3.3V ~ 5V）
def mic(pin_num):
    """
    :param pin_num:
    :return:
    """
    mic_detect = Pin(pin_num, Pin.IN, Pin.PULL_UP)
    return mic_detect.value()


# 感光模块（工作电压3.3V，D0输入）
def photosensitive(pin_num):
    """
    :param pin_num:
    :return:
    """
    photosensitive_data = Pin(pin_num, Pin.IN, Pin.PULL_UP)
    return photosensitive_data.value()


# 超声波测距模块（工作电压5V）
def checkdist(Trig_Pin_Num, Echo_Pin_Num):
    """
    :param Trig_Pin_Num:
    :param Echo_Pin_Num:
    :return:
    """
    Trig = Pin(Trig_Pin_Num, Pin.OUT)
    Echo = Pin(Echo_Pin_Num, Pin.IN)
    Trig.value(0)
    Echo.value(0)
    Trig.value(1)
    time.sleep(0.00001)
    Trig.value(0)
    while Echo.value() == 0:
        pass
    t1 = time.ticks_us()
    while Echo.value() == 1:
        pass
    t2 = time.ticks_us()
    t3 = time.ticks_diff(t2, t1) / 10000
    return round(t3 * 340 / 2, 2)


