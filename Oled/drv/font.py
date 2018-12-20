# !/usr/bin/python
# -*- encoding: utf-8 -*-
"""
:开发者:   陈浩
:开发日期: 2018年12月5日
:邮箱地址: chenhao1010@163.com
:个人博客: https://www.chenhao-home.cn/
:开发芯片: ESP-32
:修订日志:
        1、字符生成请使用PCtoLCD2002(完美版)
        2、
        3、
        4、
        5、
"""

byte = {

0xe696b0:
    [
    0x00,0x08,0x0C,0x7F,0x22,0x12,0x7F,0x7F,0x08,0x7F,0x08,0x3A,0x69,0x48,0x18,0x10,
    0x00,0x06,0x78,0x60,0x60,0x60,0xFE,0xE4,0x64,0xE4,0x64,0x44,0x44,0xC4,0x84,0x84
    ],#新
0xe8b5b7:
    [
    0x00,0x08,0x08,0x3E,0x08,0x08,0x08,0x7F,0x0C,0x3C,0x2F,0x2C,0x3C,0x4C,0x47,0x00,
    0x00,0x00,0xFC,0x04,0x04,0x04,0x7C,0x7C,0x40,0x40,0x46,0x46,0x7C,0x00,0xFE,0x00
    ],#起
0xe782b9:
    [
    0x00,0x01,0x01,0x01,0x01,0x01,0x1F,0x10,0x10,0x10,0x1F,0x00,0x34,0x26,0x62,0x00,
    0x00,0x00,0x00,0xFC,0x00,0x00,0xF8,0x08,0x08,0x08,0xF8,0x00,0x4C,0x44,0x26,0x00
    ],#点
0xe699ba:
    [
    0x00,0x18,0x10,0x3F,0x24,0x7F,0x0C,0x1B,0x31,0x2F,0x08,0x0F,0x08,0x08,0x0F,0x08,
    0x00,0x00,0x00,0xFC,0x24,0xA4,0x24,0x3C,0xC0,0xF8,0x18,0xF8,0x18,0x18,0xF8,0x18
    ],#智
0xe883bd:
    [
    0x00,0x08,0x18,0x36,0x23,0x7F,0x00,0x3F,0x23,0x3F,0x23,0x23,0x3F,0x23,0x27,0x20,
    0x00,0x40,0x44,0x58,0x60,0xC2,0x7E,0x00,0x40,0x44,0x78,0x60,0x40,0x42,0x7E,0x00
    ],#能
0xe5aeb6:
    [
    0x00,0x01,0x01,0x7F,0x60,0x6F,0x03,0x07,0x39,0x63,0x0C,0x71,0x06,0x18,0x63,0x01,
    0x00,0x80,0x80,0xFE,0x06,0xF6,0x00,0x08,0x98,0xF0,0xD0,0x58,0x4C,0x46,0x80,0x00
    ],#家
0xe5b185:
    [
    0x00,0x00,0x3F,0x30,0x3F,0x30,0x30,0x3F,0x30,0x30,0x27,0x24,0x24,0x67,0x44,0x00,
    0x00,0x00,0xFC,0x0C,0xFC,0xC0,0xC0,0xFE,0xC0,0xC0,0xFC,0x0C,0x0C,0xFC,0x0C,0x00
    ],#居
0xe6b8a9:
    [
    0x00,0x00,0x33,0x12,0x03,0x42,0x32,0x03,0x00,0x17,0x34,0x24,0x24,0x64,0x5F,0x00,
    0x00,0x00,0xF8,0x08,0xF8,0x08,0x08,0xF8,0x00,0xFC,0xA4,0xA4,0xA4,0xA4,0xFE,0x00
    ],#温
0xe6b9bf:
    [
    0x00,0x00,0x23,0x1A,0x03,0x02,0x62,0x33,0x00,0x04,0x14,0x22,0x22,0x60,0x4F,0x00,
    0x00,0x00,0xFC,0x04,0xFC,0x04,0x04,0xFC,0x00,0x92,0x92,0x94,0x9C,0x90,0xFE,0x00
    ],#湿
0xe5baa6:
    [
    0x00,0x00,0x00,0x3F,0x22,0x22,0x2F,0x22,0x23,0x20,0x2F,0x23,0x21,0x60,0x47,0x08,
    0x00,0x80,0x80,0xFC,0x10,0x10,0xFC,0x10,0xF0,0x00,0xF8,0x10,0xA0,0xC0,0x3E,0x02
    ],#度
0xe28483:
    [
    0x00,0x20,0x50,0x50,0x23,0x02,0x06,0x04,0x04,0x04,0x04,0x06,0x03,0x01,0x00,0x00,
    0x00,0x00,0x00,0xF0,0x0C,0x04,0x00,0x00,0x00,0x00,0x04,0x04,0x0C,0xF8,0x00,0x00
    ],#℃
0xe2968f: 
    [
    0x01,0x02,0x04,0x05,0x05,0x05,0x05,0x05,0x05,0x05,0x09,0x0A,0x0A,0x09,0x04,0x03,
    0x80,0x40,0x20,0xA0,0xA0,0xA0,0xA0,0xA0,0xA0,0xA0,0x90,0x50,0x50,0x90,0x20,0xC0
    ], #温度计 "▏"
0xe29692: 
    [
    0x00,0x01,0x01,0x02,0x02,0x02,0x06,0x04,0x0C,0x08,0x0A,0x0A,0x0D,0x04,0x03,0x00,
    0x00,0x80,0x80,0x40,0x40,0x40,0x20,0x20,0x10,0x10,0x10,0x10,0xB0,0x20,0xC0,0x00
    ], # 湿度计 "▒"
}