import requests
import json

API_KEY = "你的API Key"
SECRET_KEY = "你的Secret Key"


def main():
    #  API端点
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/ernie_speed?access_token=" + get_access_token()

    # 请求体
    # json.dumps：将数据调整成json格式
    payload = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": "你好"
            },
        ]
    })

    # 请求头
    headers = {
        'Content-Type': 'application/json'
    }

    # 发送POST请求
    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))


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

if __name__ == '__main__':
    main()
