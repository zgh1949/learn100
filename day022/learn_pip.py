"""
pip search ujson # 
pip install ujson # 安装
pip install -U ujson # 更新
pip list
pip uninstall -y ujson
pip install requests
"""

import ujson
import requests

api_key = '06ceab3fc72c1bf26509b95ee0138084'

resp = requests.get(f"https://apis.tianapi.com/networkhot/index?key={api_key}")
if resp.status_code == 200:
    data_model = resp.json()
    print(ujson.dumps(data_model, ensure_ascii=False))