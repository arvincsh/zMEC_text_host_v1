from PIL import Image
import sys
'''
'''
def getImage(filename):
    fileName = filename
    img = Image.open(fileName,'r')
    return img
'''
'''
def convert_Image(img, standard=250):
    '''
    '''
    image = img.convert('L')

    '''
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

'''
def change_Image_to_text(img):
    '''
    
    '''
    testdata_dir_config = '--tessdata-dir "/usr/share/tesseract-ocr/4.00/tessdata"'
    textCode = pytesseract.image_to_string(img, lang='eng', config=testdata_dir_config)
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