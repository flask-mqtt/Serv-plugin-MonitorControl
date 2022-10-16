# MonitorControl
## 概述
- 用于配合serv端使用的监视器控制工具
## 功能
- 控制信号源切换
- 控制背光亮度
- 控制RGB色彩
- 控制电源开关
## 安装
- MonitorControl项目复制到serv项目下的plugins目录下
- 重启服务
## 初次运行
- 第一次run时在安装完包后会出现一个异常，程序自动重启因为这个包安装完需要重启一下忽略即可。
- 除第一次以外的无法启动都是有问题的。请查看命令窗口 查看方法 run.bat 编辑 将 -WindowStyle Hidden 删除即可
# 已知问题
- 部分显示器无法获取UID的暂时不能使用
TODO:在考虑上述情况如何获取唯一，并修改
TODO:添加切换主副屏 
``` cmd
DisplaySwitch.exe /internal # 仅主屏
DisplaySwitch.exe /clone # 复制
DisplaySwitch.exe /extend # 扩展
DisplaySwitch.exe /external # 仅副屏
```
TODO:添加屏幕旋转控制
``` cmd
Display.exe /rotate:0-270
```
