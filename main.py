import base64
import msvcrt

import requests
from bs4 import BeautifulSoup
import re
import numpy as np
import urllib.parse
import getpass


# import pandas as pd
# import io
# import matplotlib.pyplot as plt
# import json


def getParam(url, flag, name, pwd):
    tableUrl = "http://124.160.107.91:6379/" + url
    headers1 = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Referer": "http://124.160.107.91:6379",
        "Accept-Language": "zh-Hans,en-US;q=0.7,en;q=0.3",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "Keep-Alive",
        "DNT": "1",
        "Host": "124.160.107.91:6379",
        "Cookie": ""
    }
    if flag:
        headers2 = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Referer": "http://124.160.107.91:6379",
            "Accept-Language": "zh-Hans,en-US;q=0.7,en;q=0.3",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "Keep-Alive",
            "DNT": "1",
            "Host": "124.160.107.91:6379",
            "Cookie": "ASP.NET_SessionId=" + getCookie(name, pwd)
        }
        resp = requests.get(tableUrl, headers=headers2)
    else:
        resp = requests.get(tableUrl, headers=headers1)
    resp.encoding = resp.apparent_encoding
    html_text = resp.text
    soup1 = BeautifulSoup(html_text, 'html.parser')
    return np.array([soup1.find("input", {"id": "__VIEWSTATE"}).get("value"),
                     soup1.find("input", {"id": "__EVENTVALIDATION"}).get("value")])


def getCookie(name, pwd):
    para = getParam('default2.aspx', False, name, pwd)
    VIEWSTATE = para[0]
    EVENTVALIDATION = para[1]
    url = "http://124.160.107.91:6379/default2.aspx"
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Referer": "http://124.160.107.91:6379",
        "Accept-Language": "zh-Hans,en-US;q=0.7,en;q=0.3",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "Keep-Alive",
        "DNT": "1",
        "Host": "124.160.107.91:6379"
    }
    data = {
        '__VIEWSTATE': VIEWSTATE,
        '__EVENTVALIDATION': EVENTVALIDATION,
        'TextBox1': name,
        'TextBox2': pwd,
        'RadioButtonList1': '%D1%A7%C9%FA',
        'Button1': ''
    }
    resp = requests.post(url, headers=headers, data=data, allow_redirects=False)
    red_header = resp.headers
    set_cookie_headers = red_header.get('Set-Cookie', None)
    cookies = set_cookie_headers.split(';')
    cookie_name, cookie_value = cookies[0].split('=', 1)
    return cookie_value.strip()


print("  ______          _     ____________ ")
print(" |  ____|        | |   |___  /  ____|")
print(" | |__ _   _  ___| | __   / /| |__   ")
print(" |  __| | | |/ __| |/ /  / / |  __|  ")
print(" | |  | |_| | (__|   <  / /__| |     ")
print(" |_|   \__,_|\___|_|\_\/_____|_|     ")
print("             v1.0.0                  ")
print("       仅供学习，请勿转载 ——ByZR        ")
print("                                     ")

username = input("请输入学号：")
password = input("请输入密码：")
stuName = input("请输入姓名：")

para = getParam('xscjcx_dq.aspx?xh=' + username + '&xm=' + urllib.parse.quote(stuName.encode('GB2312')) + '&gnmkdm=N121605', True, username, password)
VIEWSTATE = para[0]
EVENTVALIDATION = para[1]

data = {
    '__EVENTTARGET': '',
    '__EVENTARGUMENT': '',
    '__LASTFOCUS': '',
    '__VIEWSTATE': VIEWSTATE,
    '__EVENTVALIDATION': EVENTVALIDATION,
    'ddlxn': '',
    'ddlxq': '',
    'btnCx': '+%B2%E9++%D1%AF+'
}
tableUrl = "http://124.160.107.91:6379/xscjcx_dq.aspx?xh=" + username + "&xm=" + urllib.parse.quote(stuName.encode("GB2312")) + "&gnmkdm=N121605"
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Referer": "http://124.160.107.91:6379",
    "Accept-Language": "zh-Hans,en-US;q=0.7,en;q=0.3",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "Keep-Alive",
    "DNT": "1",
    "Host": "124.160.107.91:6379",
    "Cookie": "ASP.NET_SessionId=" + getCookie(username, password)
}
response = requests.post(tableUrl, headers=headers, data=data)
response.encoding = response.apparent_encoding
soup = BeautifulSoup(response.text, 'html.parser')
score_base64 = soup.find("input", {"id": "__VIEWSTATE"}).get("value")
score_data = base64.b64decode(score_base64).decode("utf-8", "ignore")

separator = "dd"
data_entries = re.split(separator, score_data)
skip_lines = 2
result = ""
for entry in data_entries:
    if skip_lines > 0:
        skip_lines -= 1
        continue
    if entry.__contains__("&nbsp;") or entry.__contains__("de"):
        continue
    if (entry.__contains__("d$f")):
        result = result[:-1] + "\n"
        continue
    entry = entry.strip()
    pattern = r'[0-9a-zA-Z\u4e00-\u9fa5\.\-]+'
    extracted_chars = re.findall(pattern, entry)
    tmp = ''.join(extracted_chars)
    result += tmp + " "

print(result[:-1])
print("按下任意键退出...")
msvcrt.getch()

# data = io.StringIO(result[:-1])
# columns = [
#     "学年", "学期", "课程编号", "课程名称", "课程类型", "学分",
#     "成绩1", "成绩2", "成绩3", "成绩4", "成绩5", "开课单位"
# ]
# df = pd.read_csv(data, sep="\t", header=None, names=columns)
# df.replace(pd.NA, "", inplace=True)
#
# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.figure(figsize=(10, 6))
# plt.axis('off')
# table = plt.table(cellText=df.values, colWidths=[0.12, 0.05, 0.1, 0.3, 0.1, 0.08, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15], cellLoc='center', loc='center')
# table.auto_set_font_size(False)
# table.set_fontsize(10)
# table.scale(1, 1)
#
# plt.savefig('table_image.png', dpi=500, bbox_inches='tight', pad_inches=0.5, transparent=True)
# plt.show()
