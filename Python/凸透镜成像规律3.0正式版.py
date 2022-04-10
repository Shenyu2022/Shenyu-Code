#  -*- coding: UTF-8 -*-

# MindPlus

# Python

import math

# 自定义函数


print("凸透镜成像规律, BY Shenyu_Yan 正式版3.0")

while True:

  JiaoJuf = (int(input("请输入焦距f = ")))
  WuJuu = (int(input("请输入物距u = ")))
  if (WuJuu > (2 * JiaoJuf)):
    print("此时的像成 倒立 缩小 的 实像")
  if ((JiaoJuf < WuJuu) and (WuJuu < (2 * JiaoJuf))):
    print("此时的像成 倒立 放大 的 实像")
  if (WuJuu == (2 * JiaoJuf)):
    print("此时的像成 倒立 等大 的 实像")
  if (WuJuu < JiaoJuf):
    print("此时的像成 正立 放大 的 虚像")
  if (WuJuu == JiaoJuf):
    print("\"此时既不成虚像也不成实像\"")

#本程序代码，Shenyu_Yan 拥有自主知识产权   2022.3.23
#开源项目，免费提供使用