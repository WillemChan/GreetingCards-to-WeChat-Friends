import os.path, math, glob
from PIL import Image


def convert_image_to_circle(jpgfile, outdir):
    ima = Image.open(jpgfile).convert("RGBA")
    size = ima.size

    # 剪切为圆形，首先需要正方形的图片
    r2 = min(size[0], size[1])
    if size[0] != size[1]:  # 先判断是否为正方形，不是正方形的画需要先把矩形裁剪为正方形
        imb = Image.new('RGBA', (r2, r2), (255, 255, 255, 0))
        pima = ima.load()  # 像素的访问对象
        pimb = imb.load()
        for i in range(r2):
            for j in range(r2):
                pimb[i, j] = pima[(size[0] - r2) / 2 + i, (size[1] - r2) / 2 + j]  # 矩形的中心点与正方形的中心点重合
    else:
        imb = ima

    # 最后生成圆的半径
    r3 = int(r2 / 2)  # 圆心横坐标 圆的半径
    imc = Image.new('RGBA', (r3 * 2, r3 * 2), (255, 255, 255, 0))
    pimb = imb.load()  # 像素的访问对象
    pimc = imc.load()

    for i in range(r2):
        for j in range(r2):
            lx = abs(i - r3)  # 到圆心距离的横坐标
            ly = abs(j - r3)  # 到圆心距离的纵坐标
            l = (pow(lx, 2) + pow(ly, 2)) ** 0.5  # 三角函数 半径

            if l < r3:
                pimc[i, j] = pimb[i, j]
    # os.path.splitext()用于将文件名与扩展名分离，否则图片仍然会保存为jpg格式，从而报错
    imc.save(os.path.join(outdir, os.path.basename(os.path.splitext(jpgfile)[0]) + '.png'))

if __name__ == "__main__":
    # glob.glob可以返回所有匹配的文件路径列表
    for jpgfile in glob.glob("C:/Users/*.jpg"):  # 输入待处理图片所在的文件夹
        convert_image_to_circle(jpgfile, "C:/Users/")  # 输入处理之后的图片导出的路径
    print("处理完毕")
