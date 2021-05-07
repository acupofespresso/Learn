import json
import requests

url = "https://app.mokahr.com/api/outer/ats-jc-apply/website/job"

payload = {
    "orgId":"zhihu",
    "jobId":"eac28920-4a31-4362-878a-66e4b1f01aa4",
    "siteId":3819,
}
headers = {
    'Host': 'app.mokahr.com',
    'Connection': 'keep-alive',
    'Content-Length': '78',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
    'use-http-status': '0',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
    'moka-tracing': '{"op_no":"553fec96-453b-4c53-8006-3428dcfa85f1","locale":"zh_CN","time_zone":"GMT+08:00","source":"apply-web","org_id":"zhihu"}',
    'Content-Type': 'application/json',
    'Accept': '*/*',
    'Origin': 'https://app.mokahr.com',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://app.mokahr.com/apply/zhihu/3819',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cookie': 'acw_tc=2760828716197534874897885e8e795c7a391304e6aa20747310c947b6a0a0; locale=zh-CN; moka-apply=X970AMlGvYyFhNBMNl2Byx1VU9ALKLcrE8kehZb7etc%3D; connect.sid=s%3ArhGTRbtN2lwCC6YG4glfpkkuvYKd4eca.E8S2VRJo1sufZpQXmVQ5SYY4doYnv%2FQqcnrZ8scrf%2Fg',
}

response = requests.request("POST", url, data=json.dumps(payload), headers=headers)

print(response.status_code)
print(response.content.decode('utf-8'))
