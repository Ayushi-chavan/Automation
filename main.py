from os import access
import cv2
import dropbox
import time
import random 

def take_snapshot():
    
    number = random.random(0,100)

    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        img_name = 'img'+str(number)+'.png'
        cv2.imwrite(img_name,frame)
        start_time = time.time
        result=False
    return img_name
    print("snapshot taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(img_name):
    img_counter=+1
    access_token = "sl.BSPb1-5p9eRvTv-6uDeNc_1HHz-5YuMZNQoFYl8Ysl6K2VNDJ3n6Gm93PKWsKDAZHuGjVbDr6JThdeyOXXI0xZymfAqGLdSvUXRrsa_pU3tbUriq7iZPmELD2mQzqGMqWwncFFE"
    file = img_counter
    file_from = file
    file_to="/NewFolders/"+(img_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(), file_to,mode=dropbox.files.writeMode.overwrite)
        print("file uploaded")

def main():
    while(True):
        start_time=0
        if((time.time() - start_time) >= 300):
            name = take_snapshot()
            upload_file(name)

main()