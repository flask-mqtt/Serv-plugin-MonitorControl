from plugins.MonitorControl.packages import VCP
from plugins.MonitorControl.packages.VCP.get_vpc_codes import *

def find_monitor_index(manufacturer, uid):
    monitors = VCP.list_monitors()
    for index in range(len(monitors)):
        if monitors[index]['manufacturer'].lower().find(manufacturer.lower()) > -1:
            if str(monitors[index]['serial'].lower().split('uid')[1]) == str(uid):
                return index
    return -1