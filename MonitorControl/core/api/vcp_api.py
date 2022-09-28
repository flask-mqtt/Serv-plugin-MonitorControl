from flask import *
from app.tools.my_global import *
from plugins.MonitorControl.core.service.vcp_service import *

api = Blueprint('vcp_api', __name__)


@api.route("/vcpcode", methods=["GET", "POST"])
def getmonitors():
    monitors = VCP.list_monitors()
    html = '<html>'
    for index in range(len(monitors)):

        html += 'Manufacturer: %s <br>' % monitors[index]['manufacturer']

        html += 'UID: %s <br>' % monitors[index]['serial'].split('UID')[1]

        html += 'Please create file in the <b style="color:red">plugins/MonitorControl/vcp_codes/%s-%s_vcp_code.json</b> directory and write the corresponding key value.' % (
            monitors[index]['manufacturer'],
            monitors[index]['serial'].split('UID')[1])
        html += '<br><br>'
    html += '[ manufacturer ] -> Used to combine key parameters in mqtt | request.get()/post() <b style="color:red">required</b>, the function is to find the key parameters displayed. It needs to be used with [uid]<br><br>'
    html += '[ uid ] -> Used for the combined key parameters in mqtt | request.get()/post() , <b style="color:red">required</b>, the function is to find the key parameters of the display It needs to be used together with [ manufacturer ]'
    html += '<br><br>'
    html += 'Please refer to the template description for the creation of key-value content. <br>Please use ControlMyMonitor.exe to view the code value.<br>'
    html += 'The VCP CODE displayed by <b style="color:red">ControlMyMonitor.exe</b> is the code in the corresponding xxx-xxx_vcp_code.json configuration<br>'
    html += 'For example, <b style="color:red">if the VCP CODE displays D1, the xxx-xxx_vcp_code.json code: "0XD1"</b>'
    html += '</html>'
    return render_template_string(html)


@api.route("/monitor_get_brightness", methods=["GET", "POST"])
def monitor_get_brightness():
    manufacturer = request.args.get('manufacturer', None)
    uid = request.args.get('uid', None)
    if manufacturer != None or uid != None:
        res = get_brightness_service(manufacturer, uid)
    else:
        res = 'Missing argument, must contain (manufacturer, uid)'
    return res


@api.route("/monitor_set_brightness", methods=["GET", "POST"])
def monitor_set_brightness():
    manufacturer = request.args.get('manufacturer', None)
    uid = request.args.get('uid', None)
    value = request.args.get('value', None)
    if manufacturer != None or uid != None or value != None:
        value = int(value)
        res = set_brightness_service(manufacturer, uid, value)
    else:
        res = 'Missing argument, must contain (manufacturer, uid, value)'
    return res


@api.route("/monitor_select_color_preset", methods=["GET", "POST"])
def monitor_select_color_preset():
    manufacturer = request.args.get('manufacturer', None)
    uid = request.args.get('uid', None)
    value = request.args.get('value', None)
    if manufacturer != None or uid != None or value != None:
        res = Select_Color_Preset_service(manufacturer, uid, value)
    else:
        res = 'Missing argument, must contain (manufacturer, uid, value)'
    return res


@api.route("/monitor_hdmi1", methods=["GET", "POST"])
def monitor_hdmi1():
    '''
    激活HDMI-1
    '''
    manufacturer = request.args.get('manufacturer', None)
    uid = request.args.get('uid', None)
    if manufacturer != None or uid != None:
        res = activation_hdmi1_service(manufacturer, uid)
    else:
        res = 'Missing argument, must contain (manufacturer, uid)'
    return res


@api.route("/monitor_dp", methods=["GET", "POST"])
def monitor_dp():
    '''
    激活DP
    '''
    manufacturer = request.args.get('manufacturer', None)
    uid = request.args.get('uid', None)
    if manufacturer != None or uid != None:
        res = activation_dp_service(manufacturer, uid)
    else:
        res = 'Missing argument, must contain (manufacturer, uid)'
    return res


@api.route("/monitor_off", methods=["GET", "POST"])
def monitor_off():
    '''
    关闭显示器
    '''
    manufacturer = request.args.get('manufacturer', None)
    uid = request.args.get('uid', None)
    if manufacturer != None or uid != None:
        res = monitor_off_service(manufacturer, uid)
    else:
        res = 'Missing argument, must contain (manufacturer, uid)'
    return res


@api.route("/monitor_on", methods=["GET", "POST"])
def monitor_on():
    '''
    打开显示器
    '''
    manufacturer = request.args.get('manufacturer', None)
    uid = request.args.get('uid', None)
    if manufacturer != None or uid != None:
        res = monitor_on_service(manufacturer, uid)
    else:
        res = 'Missing argument, must contain (manufacturer, uid)'
    return res
