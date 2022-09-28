from fileinput import filename
from app.tools.file_operations.get_file_path import get_file_path
from app.tools.file_operations.read_json_file import read_json_file

def get_vpc_code(manufacturer, uid):
    filename = '%s-%s' % (manufacturer, uid)
    VCP_CODE_PATH = get_file_path('%s_vcp_code.json' % filename)
    if len(VCP_CODE_PATH) < 1:
        print('未找到文件: %s_vcp_code.json' % filename)
        return {}
    else:
        VCP_CODE_PATH = VCP_CODE_PATH[0]
        vpc_codes = read_json_file(VCP_CODE_PATH)
        return vpc_codes
