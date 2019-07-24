# -*- encoding=utf8 -*-
__author__ = "admin"

from airtest.core.api import *

auto_setup(__file__)

from poco.drivers.unity3d import UnityPoco
poco = UnityPoco()

import re

#打开联盟
poco("HomeUIPanel").child("RightSideBar").child("ClubBtn").click()

#-----打开改名界面-------
poco("AllianceUI(Clone)").child("BackBtn").child("label").click()
assert poco("PopupCanvas").offspring("RenameAllianceNameWindow(Clone)").child("CostGemConfirmBtn").child("Text").wait(3).get_text() == "修改","改名界面未打开"
poco("CloseBtn").click()
poco("AllianceUI(Clone)").child("BackBtn").child("label").child("BtnRename").wait(3).click()
assert poco("PopupCanvas").offspring("RenameAllianceNameWindow(Clone)").child("CostGemConfirmBtn").child("Text").wait(3).get_text() == "修改","改名界面未打开"
poco("PopupCanvas").offspring("RenameAllianceNameWindow(Clone)").child("Bg").child("CloseBtn").click()

#-----改名，联盟名为空---------
poco("AllianceUI(Clone)").child("BackBtn").child("label").click()
poco("PopupCanvas").offspring("RenameAllianceNameWindow(Clone)").child("CostGemConfirmBtn").wait(3).click()
assert poco("TopMessageBar(Clone)").child("Panel").child("Text").get_text() == "联盟名不能为空","联盟名修改为空"
poco("PopupCanvas").offspring("RenameAllianceNameWindow(Clone)").child("Bg").child("CloseBtn").click()

#-----改名，字符过短----------
poco("AllianceUI(Clone)").child("BackBtn").child("label").click()
poco("PopupCanvas").offspring("RenameAllianceNameWindow(Clone)").child("InputName").wait(3).set_text('11111')
sleep(2)
poco("PopupCanvas").offspring("RenameAllianceNameWindow(Clone)").child("CostGemConfirmBtn").click()
assert poco("TopMessageBar(Clone)").child("Panel").child("Text").get_text() == "请输入6到14位数的联盟名（一个汉字等于2位数）","联盟名修改过短"
poco("PopupCanvas").offspring("RenameAllianceNameWindow(Clone)").child("Bg").child("CloseBtn").click()

#-----改名，字符过长----------
poco("AllianceUI(Clone)").child("BackBtn").child("label").click()
poco("PopupCanvas").offspring("RenameAllianceNameWindow(Clone)").child("InputName").wait(3).set_text('啦啦啦啦啦啦啦0')
sleep(2)
poco("PopupCanvas").offspring("RenameAllianceNameWindow(Clone)").child("CostGemConfirmBtn").click()
assert poco("TopMessageBar(Clone)").child("Panel").child("Text").get_text() == "请输入6到14位数的联盟名（一个汉字等于2位数）","联盟名修改过长"
poco("PopupCanvas").offspring("RenameAllianceNameWindow(Clone)").child("Bg").child("CloseBtn").click()

#-----改名，特殊字符----------
poco("AllianceUI(Clone)").child("BackBtn").child("label").click()
poco("PopupCanvas").offspring("RenameAllianceNameWindow(Clone)").child("InputName").wait(3).set_text('1@#（就这样')
sleep(2)
poco("PopupCanvas").offspring("RenameAllianceNameWindow(Clone)").child("CostGemConfirmBtn").click()
assert poco("TopMessageBar(Clone)").child("Panel").child("Text").get_text() == "输入内容包含特殊字符","联盟名修改包含特殊字符"
poco("PopupCanvas").offspring("RenameAllianceNameWindow(Clone)").child("Bg").child("CloseBtn").click()

#-----改名，敏感字----------
poco("AllianceUI(Clone)").child("BackBtn").child("label").click()
poco("PopupCanvas").offspring("RenameAllianceNameWindow(Clone)").child("InputName").wait(3).set_text('习大大')
sleep(2)
poco("PopupCanvas").offspring("RenameAllianceNameWindow(Clone)").child("CostGemConfirmBtn").click()
assert poco("TopMessageBar(Clone)").child("Panel").child("Text").get_text() == "输入内容包含敏感字符","联盟名修改包含敏感字"
poco("PopupCanvas").offspring("RenameAllianceNameWindow(Clone)").child("Bg").child("CloseBtn").click()

#-----改名，原来一样的联盟名----------
allianceName_now = poco("AllianceUI(Clone)").child("BackBtn").child("label").get_text()
allianceName_now = re.match( r'(.*)联盟', allianceName_now).group(1)
poco("AllianceUI(Clone)").child("BackBtn").child("label").click()
poco("PopupCanvas").offspring("RenameAllianceNameWindow(Clone)").child("InputName").wait(3).set_text(allianceName_now)
sleep(2)
poco("PopupCanvas").offspring("RenameAllianceNameWindow(Clone)").child("CostGemConfirmBtn").click()
assert poco("TopMessageBar(Clone)").child("Panel").child("Text").get_text() == "新联盟名不能与原名相同","联盟名与原联盟名相同，修改成功"
poco("PopupCanvas").offspring("RenameAllianceNameWindow(Clone)").child("Bg").child("CloseBtn").click()

#-----改名，和其他联盟名重复（重复用的联盟名是23232323）----------
poco("AllianceUI(Clone)").child("BackBtn").child("label").click()
poco("PopupCanvas").offspring("RenameAllianceNameWindow(Clone)").child("InputName").wait(3).set_text('23232323')
sleep(2)
poco("PopupCanvas").offspring("RenameAllianceNameWindow(Clone)").child("CostGemConfirmBtn").click()
assert poco("TopMessageBar(Clone)").child("Panel").child("Text").get_text() == "此联盟名已被占用","联盟名改成了和其他联盟名一样"
poco("PopupCanvas").offspring("RenameAllianceNameWindow(Clone)").child("Bg").child("CloseBtn").click()

#-----改名，正常，成功（要先用sql修改可能存在的即将修改的联盟名。且要确保宝石充足）----------
#sql: UPDATE t_alliance set alliance_name = '123123###' WHERE alliance_name = '999哦哦999';
poco("AllianceUI(Clone)").child("BackBtn").child("label").click()
poco("PopupCanvas").offspring("RenameAllianceNameWindow(Clone)").child("InputName").wait(3).set_text('999哦哦999')
sleep(2)
poco("PopupCanvas").offspring("RenameAllianceNameWindow(Clone)").child("CostGemConfirmBtn").click()
assert poco("TopMessageBar(Clone)").child("Panel").child("Text").get_text() == "联盟名修改成功","联盟名应修改可能成功，但肯定没正确提示"
allianceName_now = poco("AllianceUI(Clone)").child("BackBtn").child("label").get_text()
allianceName_now = re.match( r'(.*)联盟', allianceName_now).group(1)
assert allianceName_now == '999哦哦999','修改后的联盟名和修改时输入的联盟名不一致'