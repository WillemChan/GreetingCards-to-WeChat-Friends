import os.path
import glob
from pptx import Presentation
from pptx.util import Cm  # 导入单位-厘米
from pptx.util import Pt  # 导入单位-磅


def insert_images(pngfile):
    img_path = pngfile
    img_left, img_top, img_width, img_height = Cm(11.7), Cm(8.53), Cm(2), Cm(2)  # 设置图片位置和大小，距离左边、上边，图片的宽、高
    img = slide.shapes.add_picture(img_path, img_left, img_top, img_width, img_height)
    tx_left, tx_top, tx_width, tx_height = Cm(17), Cm(8.53), Cm(2), Cm(1)  # 设置文本框的位置和大小，距离左边、上边，文本框的宽、高
    textbox = slide.shapes.add_textbox(tx_left, tx_top, tx_width, tx_height)
    textbox.text = os.path.basename(os.path.splitext(pngfile)[0])  # 文本框中文字的内容是png格式图片的文件名


prs = Presentation()
for pngfile in glob.glob("C:/Users/*.png"):  # 此处为png图片的路径
    slide = prs.slides.add_slide(prs.slide_layouts[6])  # 插入图片之前需要先插入一页空白PPT
    insert_images(pngfile)
prs.save('test.pptx')  # 保存PPT文件
print('完成')
