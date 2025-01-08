import requests
from PIL import Image, ImageDraw, ImageFont


url = 'http://1473119283406975.cn-hangzhou.pai-eas.aliyuncs.com/api/predict/ms_eas_323b56b4_6f92_4fe9_aa1e_6fb687017c2f/invoke'
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'MzcwNTY1N2U2N2NkOGIwNDI4YTVlNTFjZDEwMjdjNjAzYjcwOTVmOA=='
}
data = {"input":{"image":"http://modelscope.oss-cn-beijing.aliyuncs.com/demo/images/image_detection.jpg"}}

response = requests.post(url, headers=headers, json=data)
print(response.json())

'''

'''
def visualize_detection(image_url, result):
    # 加载图片
    image = Image.open(requests.get(image_url, stream=True).raw)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", 15)  # 根据需要选择合适的字体和大小

    # 解析检测结果
    boxes = result['Data']['boxes']
    labels = result['Data']['labels']
    scores = result['Data']['scores']

    # 绘制边界框和标签
    for box, label, score in zip(boxes, labels, scores):
        # 边界框坐标
        x1, y1, x2, y2 = map(int, box)
        # 绘制边界框
        draw.rectangle([x1, y1, x2, y2], outline="red", width=2)
        # 绘制标签和置信度
        label_text = f"{label}: {score:.2f}"
        draw.text((x1, y1), label_text, fill="red", font=font)

    # 展示图片
    image.show()

# 调用可视化函数
visualize_detection('http://modelscope.oss-cn-beijing.aliyuncs.com/demo/images/image_detection.jpg', response.json())