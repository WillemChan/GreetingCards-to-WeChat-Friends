import os
import glob
import win32com
import win32com.client

# 将PPT导出为jpg图片所对应的数值
ppSaveAsJPG = 17


def PPTtoJPG(pptfile):
    ppt_app = win32com.client.Dispatch('PowerPoint.Application')
    ppt_app.Visible = 1
    ppt = ppt_app.Presentations.Open(pptfile)
    ppt.SaveAs(pptfile + '_result.jpg', ppSaveAsJPG)
    ppt_app.Quit()


if __name__ == '__main__':
    for pptfile in glob.glob("C:/Users/Willem/Jupyter_Exercise/*.pptx"):
        PPTtoJPG(pptfile)
    print("处理完毕")
