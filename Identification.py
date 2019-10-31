from PIL import Image
import sys
'''
获取图片
'''
def getImage(filename):
    fileName = filename
    img = Image.open(fileName,'r')
    # 打印当前图片的模式以及格式
    #print('未转化前的: ', img.mode, img.format)
    # 使用系统默认工具打开图片
    #img.show()
    return img
'''
1) 将图片进行降噪处理, 通过二值化去掉后面的背景色并加深文字对比度
'''
def convert_Image(img, standard=250):
    '''
    【灰度转换】
    '''
    image = img.convert('L')

    '''
    【二值化】
    根据阈值 standard , 将所有像素都置为 0(黑色) 或 255(白色), 便于接下来的分割
    '''
    pixels = image.load()
    for x in range(image.width):
        for y in range(image.height):
            if pixels[x, y] > standard:
                pixels[x, y] = 255
            else:
                pixels[x, y] = 0
    return image

import pytesseract
import re
'''
使用 pytesseract 库来识别图片中的字符
'''
def change_Image_to_text(img):
    '''
    如果出现找不到训练库的位置, 需要我们手动自动
    语法: tessdata_dir_config = '--tessdata-dir "<replace_with_your_tessdata_dir_path>"'
    '''
    testdata_dir_config = '--tessdata-dir "/usr/share/tesseract-ocr/4.00/tessdata"'
    textCode = pytesseract.image_to_string(img, lang='eng', config=testdata_dir_config)
    # 去掉非法字符，只保留字母数字
    #print(textCode)
    textCode = re.sub("\W", "", textCode)
    return textCode

def main(filename):

    img = convert_Image(getImage(filename))
    #img.show()
    change_Image_to_text(img)
    return change_Image_to_text(img)

if __name__ == '__main__':
    filename = sys.argv[1]
    #"C:\\Users\\Administrator\\Desktop\\no\\page\\upload\\2019_9_4_16_16.png"
    #sys.argv[1]
    print(main(filename))
