import os
import glob
import win32com
import win32com.client

# 将PPT导出为jpg图片所对应的数值
ppSaveAsJPG = 17


def PPTtoJPG(pptfile, outdir):
    ppt_app = win32com.client.Dispatch('PowerPoint.Application')
    # 设置打开PPT的时候窗口可见，否则会在后台执行
    ppt_app.Visible = 1
    # 打开PPT文件
    ppt = ppt_app.Presentations.Open(pptfile)
    # 保存图片，第一个参数为保存图片的目录，第二个是保存的格式
    ppt.SaveAs(outdir, ppSaveAsJPG)  # Office2019提示报错，可能是版本问题
    ppt_app.Quit()


if __name__ == '__main__':
    for pptfile in glob.glob("C:/Users/*.pptx"):  # 此处输入PPTx文件所在目录
        PPTtoJPG(pptfile, 'C:/Users/Images')  # 导出图片所在目录
    print("处理完毕")
