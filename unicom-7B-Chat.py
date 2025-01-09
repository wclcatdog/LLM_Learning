#调用元景API示例 元景大语言模型7B
import requests
import json

app_id = "xxxxxxxxxxxxxxxxxxxxxxxx"
client_id = "xxxxxxxxxxxxxxxxxxxxxxxxx"
client_secret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"

def get_access_token(app_id, client_id, client_secret):

    url = "https://maas-gz-api.ai-yuanjing.com/openapi/service/v1/oauth/" + app_id + "/token"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()["data"].get("access_token")
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None

# API 端点
url = "https://maas-gz-api.ai-yuanjing.com/openapi/v1/unicom-7b-chat"

# 你的访问令牌
access_token = get_access_token(app_id,client_id,client_secret)

# 请求头
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {access_token}"
}

# 请求体
payload = {
    "model": "unicom-7b",
    "pad_token_id": 0,
    "bos_token_id": 1,
    "eos_token_id": 2,
    "max_new_tokens": 2048,
    "temperature": 0.3,
    "top_k": 5,
    "top_p": 0.85,
    "repetition_penalty": 1.1,
    "do_sample": True,
    "stream": False,
    "messages": [
        {
            "role": "user",
            "content": "1+1等于几"
        }

    ]
}

# 发送 POST 请求
response = requests.post(url, headers=headers, json=payload, verify=False)

# 处理响应
if response.status_code == 200:
    response_data = response.json()
    ans = response_data["data"]["choices"][0]["message"]["content"]
    print(ans)
else:
    print(f"请求失败，状态码: {response.status_code}")
    print(response.text)

