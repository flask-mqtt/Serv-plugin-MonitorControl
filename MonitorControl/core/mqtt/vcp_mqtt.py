from plugins.MonitorControl.core.service.vcp_service import *

def message_analysis(msg):
    '''
        解析接收的 消息 然后根据判断 进入执行函数
    '''
    try:
        if msg != '':
            entrance = msg.split('|')[0]
            manufacturer = msg.split('|')[1]
            uid = msg.split('|')[2]
            if 'brightness' == entrance:
                val = int(msg.split('|')[3])
                res = set_brightness(manufacturer, uid, val)
                if res != '':
                    return res
                else:
                    return ''
            elif 'dp' == entrance:
                res = activation_dp(manufacturer, uid)
                if res != '':
                    return res
                else:
                    return ''
            elif 'hdmi1' == entrance:
                res = activation_hdmi1(manufacturer, uid)
                if res != '':
                    return res
                else:
                    return ''
            elif 'cmode' == entrance:
                res = activation_cmode(manufacturer, uid)
                if res != '':
                    return res
                else:
                    return ''
            elif 'on' == entrance:
                res = monitor_on(manufacturer, uid)
                if res != '':
                    return res
                else:
                    return ''
            elif 'off' == entrance:
                res = monitor_off(manufacturer, uid)
                if res != '':
                    return res
                else:
                    return ''
            else:
                print('无效消息:%s' % msg)
                return ''
        else:
            print('空消息')
            return ''
    except Exception as ex:
        print(ex)
        return ''

