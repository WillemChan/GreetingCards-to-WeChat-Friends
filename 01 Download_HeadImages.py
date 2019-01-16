import itchat
import os

def dld_hImages(outdir):
    # Get the QR code to log in to the web version of WeChat
    itchat.auto_login()
    friends = itchat.get_friends(update=True)[0:]
    print(len(friends))  # Get the number of friends
    user = friends[0]["NickName"][0:]
    path = outdir  # Input your path here that you want to store HeadImages.
    os.mkdir(path)
    os.chdir(path)
    os.getcwd()  # Get the path
    for i in friends[1:len(friends)]:  # 不从0开始的原因是friends[0]是账户本人
        try:
            i['img'] = itchat.get_head_img(userName=i["UserName"])
            i['ImgName'] = i["RemarkName"][0:] + ".jpg"
        except ConnectionError:  # Network disconnection will cause an error
            print('get '+i["RemarkName"][0:]+' fail')
        fileImage = open(i['ImgName'], 'wb')
        fileImage.write(i['img'])
        fileImage.close()


if __name__ == "__main__":
    dld_hImages('C:/Users/Willem/Jupyter_Exercise/sending_pictures/headImages_bef')
    print('头像下载完毕')
