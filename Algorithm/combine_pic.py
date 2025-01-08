from PIL import Image

def merge_images(top_image_path, bottom_image_path, output_image_path):
    # 打开顶部和底部图片
    top_image = Image.open(top_image_path)
    bottom_image = Image.open(bottom_image_path)

    # 获取顶部和底部图片的宽度和高度
    top_width, top_height = top_image.size
    bottom_width, bottom_height = bottom_image.size

    # 确保两张图片宽度相同，如果不同，可以选择裁剪或填充其中一张图片以匹配另一张的宽度
    if top_width != bottom_width:
        print("图片宽度不一致，需要裁剪或填充以匹配宽度。")
        return

    # 创建一个新的图片，宽度与原图相同，高度为两张图片高度之和
    new_image = Image.new('RGB', (top_width, top_height + bottom_height))

    # 将顶部和底部图片粘贴到新图片上
    new_image.paste(top_image, (0, 0))
    new_image.paste(bottom_image, (0, top_height))

    # 保存新图片
    new_image.save(output_image_path)
    print(f"合并后的图片已保存为：{output_image_path}")

# 使用示例
merge_images('path_to_top_image.png', 'path_to_bottom_image.png', 'merged_image.jpg')