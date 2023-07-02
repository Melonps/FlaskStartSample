from PIL import Image, ImageFont, ImageDraw


def drawnameimage(name):
    image_path = "./GeneratedData/name.png"
    width = 400  # 画像の幅
    height = 400  # 画像の高さ
    font_path = "./font/SourceHanSansJP-Regular.otf"
    # Macの場合は下記のパスを指定
    # font_path = "/System/Library/Fonts/ヒラギノ角ゴシック W4.ttc"
    font_size = 100  # 文字の大きさ
    text = name
    color = (255, 255, 255)  # 文字の色
    background_color = (0, 0, 0)  # 背景色

    image = Image.new("RGB", (width, height), background_color)  # 新しいイメージを作成
    font = ImageFont.truetype(font_path, font_size)  # フォントの指定
    draw = ImageDraw.Draw(image)
    draw.line(((0, 200), (400, 200)), "gray")  # 横の線を描画
    draw.line(((200, 0), (200, 400)), "gray")  # 縦の線を描画
    text_position = (200, 200)  # テキストの配置位置を計算
    draw.text(text_position, text, font=font, fill=color, anchor="mm")  # テキストを描画
    image.save(image_path)
