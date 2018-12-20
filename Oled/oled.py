# !/usr/bin/python
# -*- encoding: utf-8 -*-
"""
:开发者:   陈浩
:开发日期: 2018年12月5日
:邮箱地址: chenhao1010@163.com
:个人博客: https://www.chenhao-home.cn/
:开发芯片: ESP-32
:修订日志:
        1、
        2、
        3、
        4、
        5、
:函数说明：
	1、text(string, x, y)，在(x, y)处显示字符串，注意text()函数内置的字体是8x8的，暂时不能替换
        2、poweroff()，关闭OLED显示
        3、poweron()，空函数，无任何效果。可以用 write_cmd(0xAF) 代替
        4、fill(n)，n=0，清空屏幕，n大于0，填充屏幕
        5、contrast()，调整亮度。0最暗，255最亮
        6、invert()，奇数时反相显示，偶数时正常显示
        7、pixel(x, y, c)，在(x, y)处画点
        8、show()，更新显示内容。前面大部分函数只是写入幕，能显示出来。
        9、line(x1,y1,x2,y2,c)，画直线
        10、vline(x,y,w,c)，画垂直直线
        11、fill_rect(x,y,w,h,c)，画填充矩形
        12、rect(x,y,w,h,c)，画空心 矩形
        13、chinese(string, x, y), 显示汉字，汉字字体是16x16的。
"""

import machine
import drv.ssd1306

i2c = machine.I2C(scl =machine.Pin(18), sda = machine.Pin(19))
oled = drv.ssd1306.SSD1306_I2C(128, 64, i2c)

oled.fill(0)
oled.chinese("新起点智能家居", 0, 0)
oled.chinese("温度", 0, 3)
oled.chinese("▏", 2, 3)
oled.text("27.6", 60, 27)
oled.chinese("℃", 6, 3)
oled.chinese("湿度", 0, 6)
oled.chinese("▒", 2, 6)
oled.text("45.3", 60, 55)
oled.text("%RH", 98, 54)
oled.show()