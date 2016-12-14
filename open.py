#!/usr/bin/python
# -*- coding: utf-8 -*-

############################
'''
project:excel文件写入
module：xlwt，XFStyle,Font,Alignment
method:add_sheet()
write()
while for 循环
'''
############################
import xlwt
import time
import sys


def set_style(name, height, bold = False):
    style = xlwt.XFStyle()
    font = xlwt.Font()
    alignment = xlwt.Alignment()
    font.name = name
    font.height = height
    font.bold = bold
    font.colour_index = 4
    alignment.horz = xlwt.Alignment.HORZ_CENTER  # 水平居中
    style.font = font
    style.alignment = alignment
    return style


def set_style2(name, height, bold = False):
    style2 = xlwt.XFStyle()
    font = xlwt.Font()
    alignment = xlwt.Alignment()
    font.name = name
    font.height = height
    font.bold = bold
    font.colour_index = 0
    alignment.vert = xlwt.Alignment.VERT_CENTER  # 垂直居中
    style2.font = font
    style2.alignment = alignment
    return style2


def write_excel():
    workbook = xlwt.Workbook()  # ��excel�ļ�
    sheet1 = workbook.add_sheet(u'测试', cell_overwrite_ok=True)
    row0 = [u'业务', u'上海', u'北京',u'天津',  u'深圳',u'广州', u'南京', u'西安', u'合计']
    column0 = [u'火车票', u'汽车票', u'飞机票', u'船票', u'地铁票', u'其他']
    status = [u'预定', u'出票', u'退票', u'错误', u'未知']
    for i in range(0, len(row0)): # 创建第一行
        sheet1.write(0, i, row0[i], set_style('Times New Roman', 200, True))
    i, j = 1, 0
    while i < 5*len(column0) and j < len(column0):  # 合并第一列
        sheet1.write_merge(i, i+4, 0, 0, column0[j], set_style2('David', 200, True))
        sheet1.write_merge(i, i+4, 8, 8)
        i += 5
        j += 1

    i = 0
    while i < 5*len(column0):
        for j in range(0, len(status)):
            sheet1.write(i+j+1, 1, status[j])
        i += 5
    workbook.save("tester.xls")
if __name__ == "__main__":
    write_excel()
    time.sleep(3)
    print "测试完毕"
    name = sys.argv[0].split('/')[-1:]
    print name