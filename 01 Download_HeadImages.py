import itchat
import os

#Get the QR code to log in to the web version of WeChat
itchat.auto_login()
friends = itchat.get_friends(update=True)[0:]
print(len(friends)) #Get the number of friends
user = friends[0]["NickName"][0:]
print(user)  #Get the user's name

path = 'C:/users/'  #Input your path here that you want to store HeadImages.
os.mkdir(path)
os.chdir(path)
os.getcwd()  #Get the path

for i in friends[1:100]:
    try:
        i['img'] = itchat.get_head_img(userName=i["UserName"])
        i['ImgName']=i["RemarkName"][0:] + ".jpg"
    except ConnectionError:  #Network disconnection will cause an error
        print('get '+i["RemarkName"][0:]+' fail')
    fileImage=open(i['ImgName'],'wb')
    fileImage.write(i['img'])
    fileImage.close()

print("下载完毕")
