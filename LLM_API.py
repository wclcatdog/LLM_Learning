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


if __name__ == '__main__':
    main()
