#  -*- coding: UTF-8 -*-

# MindPlus
# Python
import math

# 自定义函数

print("          凸透镜成像规律, BY Shenyu_Yan 版本号：测试版Alpha 21y12c")
print("")
print("          更新日志：")
print("          版本号：测试版 Alpha 21y12c")
print("          更新时间：2021-12-7 22:36:01")
print("          更新内容：       4.本次主要更新了模式选择，打算开发下一个模式，正在策划中。")
print("                          5.修复了亿些Bug，并且增加了新的Bug。（/doge）")
print("                          1.移除了Him。")
print("                          3.增加了更新日志,并且排版了。")
print("                          2.你会发现好像序号乱了，这是第五条。算了，不改了。")
print("")
def TuTouJingChengXiangGuiLv():
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
    print("此时既不成虚像也不成实像")



while True:
  XuanZeMoShi = (int(input("请选择模式，输入数字：凸透镜成像规律=1，其他版本=2         回答：")))
  if (XuanZeMoShi == 1):
    TuTouJingChengXiangGuiLv()
  else:
    if (XuanZeMoShi == 2):
      print("目前此功能正在测试中，暂未开放。如果你看到这段文字，说明没有什么问题，将来这段文字会用新功能代替。")
    print("请输入数字1或者2，PLZ")
