import requests
import json

# API 端点
url = "https://mass-gz-api.ai-yuanjing.com/openapi/vl/unicom-7b-chat"

# 你的访问令牌
access_token = "YOUR_ACCESS_TOKEN"

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
            "content": "请介绍一下你自己"
        },
        {
            "role": "assistant",
            "content": "您好，我是联通AI助手，由联通开发的人工智能助手。我可以回答"
        },
        {
            "role": "user",
            "content": "我在上海，周末可以去哪里玩?"
        },
        {
            "role": "assistant",
            "content": "上海是一个充满活力和文化氛围的城市。"
        },
        {
            "role": "user",
            "content": "上海有哪些美食?"
        }
    ]
}

# 发送 POST 请求
response = requests.post(url, headers=headers, data=json.dumps(payload), verify=False)

# 处理响应
if response.status_code == 200:
    response_data = response.json()
    print(json.dumps(response_data, indent=4, ensure_ascii=False))
else:
    print(f"请求失败，状态码: {response.status_code}")
    print(response.text)