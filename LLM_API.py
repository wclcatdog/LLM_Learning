import requests
import json
import time
import jwt
import requests

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

def test_GLM4():    
    # 实际KEY，过期时间
    def generate_token(apikey: str, exp_seconds: int):
        try:
            id, secret = apikey.split(".")
        except Exception as e:
            raise Exception("invalid apikey", e)
    
        payload = {
            "api_key": id,
            "exp": int(round(time.time() * 1000)) + exp_seconds * 1000,
            "timestamp": int(round(time.time() * 1000)),
        }
        return jwt.encode(
            payload,
            secret,
            algorithm="HS256",
            headers={"alg": "HS256", "sign_type": "SIGN"},
        )
    #https://open.bigmodel.cn/api/paas/v4/chat/completions
    url = "https://open.bigmodel.cn/api/paas/v4/chat/completions"
    API_KEY = "YOUR API KEY"
    headers = {
      'Content-Type': 'application/json',
      'Authorization': f"Bearer {API_KEY}"
    }
    
    data = {
        "model": "glm-3-turbo",
        "messages": [{"role": "user", "content": """你好"""}]
    }
    
    response = requests.post(url, headers=headers, json=data)
    
    print("Status Code", response.status_code)
    #print("JSON Response ", response.json())
    print(response.json()['choices'][0]['message']['content'])

if __name__ == '__main__':
    main()
