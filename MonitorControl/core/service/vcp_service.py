from plugins.MonitorControl.packages import VCP
from plugins.MonitorControl.packages.VCP.get_vpc_codes import get_vpc_code
from plugins.MonitorControl.packages.VCP.find_monitor import find_monitor_index


def Select_Color_Preset_service(manufacturer, uid, value):
    '''
        颜色预设
    '''
    vcp_code = get_vpc_code(manufacturer, uid)
    if len(vcp_code) < 1:
        return 'Monitor configuration file not found %s-%s_vcp_code.json' % (manufacturer, uid)
    monitor_index = find_monitor_index(manufacturer, uid)
    if monitor_index > - 1:
        new_preset_code = vcp_code['Select_Color_Preset']['possible_values'][value]
        preset_dict = vcp_code['Select_Color_Preset']['possible_values']
        if len(preset_dict) > 0:
            for key in preset_dict.keys():
                if preset_dict[key] == new_preset_code[0]:
                    VCP.windows.VCP.set_VCP(code=int(
                        vcp_code['Select_Color_Preset']['code'], 16),
                        value=vcp_code['Select_Color_Preset']
                        ['possible_values'][value],
                        display=monitor_index)
                    return key
            return 'The new preset is not in the configuration file, you cannot set the new preset, please check the configuration file of %s-%s_vcp_code.json' % (manufacturer, uid)
        else:
            return 'No corresponding color preset found, please check the configuration file of %s-%s_vcp_code.json' % (manufacturer, uid)


def get_brightness_service(manufacturer, uid):
    '''
        获取监视器亮度
    '''
    vcp_code = get_vpc_code(manufacturer, uid)
    if len(vcp_code) < 1:
        return 'Monitor configuration file not found %s-%s_vcp_code.json' % (manufacturer, uid)
    monitor_index = find_monitor_index(manufacturer, uid)
    if monitor_index > -1:
        preset_code = VCP.windows.VCP.get_VCP(
            code=int(vcp_code['Brightness']['code'], 16), display=monitor_index)
        return '%s' % preset_code[0]
    else:
        return 'No monitors found'


def set_brightness_service(manufacturer, uid, value):
    '''
        设置显示器亮度
    '''

    vcp_code = get_vpc_code(manufacturer, uid)
    if len(vcp_code) < 1:
        return 'Monitor configuration file not found %s-%s_vcp_code.json' % (manufacturer, uid)
    monitor_index = find_monitor_index(manufacturer, uid)
    if monitor_index > -1:
        newbrightness = value
        VCP.windows.VCP.set_VCP(code=int(vcp_code['Brightness']['code'], 16),
                                value=newbrightness,
                                display=monitor_index)  # 亮度
        return '%s' % newbrightness
    else:
        return 'Monitor not found'


def activation_dp_service(manufacturer, uid):
    '''
    激活DP
    '''
    vcp_code = get_vpc_code(manufacturer, uid)
    if len(vcp_code) < 1:
        return 'Monitor configuration file not found %s-%s_vcp_code.json' % (manufacturer, uid)
    monitor_index = find_monitor_index(manufacturer, uid)
    if monitor_index > -1:
        # 切换dp信号
        VCP.windows.VCP.set_VCP(
            code=int(vcp_code['Input_Select']['code'], 16),
            value=vcp_code['Input_Select']['possible_values']['DP'],
            display=monitor_index)
        return 'DP'
    else:
        return 'Monitor not found'


def activation_hdmi1_service(manufacturer, uid):
    '''
    激活HDMI-1
    '''
    vcp_code = get_vpc_code(manufacturer, uid)
    if len(vcp_code) < 1:
        return 'Monitor configuration file not found %s-%s_vcp_code.json' % (manufacturer, uid)
    monitor_index = find_monitor_index(manufacturer, uid)
    if monitor_index > -1:
        # 切换信号
        VCP.windows.VCP.set_VCP(code=int(vcp_code['Input_Select']['code'], 16),
                                value=vcp_code['Input_Select']['possible_values']['HDMI_1'], display=monitor_index)
        return 'HDMI-1'
    else:
        return 'Monitor not found'


def monitor_off_service(manufacturer, uid):
    '''
    关闭显示器
    '''
    try:
        vcp_code = get_vpc_code(manufacturer, uid)
        if len(vcp_code) < 1:
            return 'Monitor configuration file not found %s-%s_vcp_code.json' % (manufacturer, uid)
        monitor_index = find_monitor_index(manufacturer, uid)
        if monitor_index > -1:
            VCP.windows.VCP.set_VCP(
                code=int(vcp_code['Off']['code'], 16),
                value=vcp_code['Off']['value'],
                display=monitor_index)
            return 'off'
        else:
            return 'Monitor not found'
    except Exception as ex:
        print(ex)
        return str(ex)


def monitor_on_service(manufacturer, uid):
    '''
    打开显示器
    '''
    vcp_code = get_vpc_code(manufacturer, uid)
    if len(vcp_code) < 1:
        return 'Monitor configuration file not found %s-%s_vcp_code.json' % (manufacturer, uid)
    monitor_index = find_monitor_index(manufacturer, uid)
    if monitor_index > -1:
        # 切换dp信号
        VCP.windows.VCP.set_VCP(
            code=int(vcp_code['On']['code'], 16),
            value=vcp_code['On']['value'],
            display=monitor_index)
        return 'on'
    else:
        return 'Monitor not found'
