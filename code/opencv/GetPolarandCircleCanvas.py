import cv2 as cv
import numpy as np
import math

colorblack = (0, 0, 0)
thickness = 2
circleradius = 272
circlecenter = (circleradius, circleradius)
circlearclinedisdiff = circleradius/10

'''
https://blog.csdn.net/huanglu_thu13/article/details/52332695
'''
def get_red(img):
    redImg = img[:,:,2]
    return redImg

def get_green(img):
    greenImg = img[:,:,1]
    return greenImg

def get_blue(img):
    blueImg = img[:,:,0]
    return blueImg

def GenerateWhiteBG():
    #shape = (circleradius, 2*circleradius, 3)      # y, x, RGB
    shape = (circleradius, 2*circleradius)          # 1-channel 8bit
    origin_img = np.zeros(shape, np.uint8)
    origin_img.fill(255)

    cv.imshow('origin_img', origin_img)
    cv.imwrite('bg_origin_img.bmp', origin_img)    # 存檔儲存為 png

    cv.waitKey(0)

def GeneratePolarCoordinate():
    '''
    https://ithelp.ithome.com.tw/articles/10241685
    https://github.com/makelove/OpenCV-Python-Tutorial/blob/master/ch04-%E5%9B%BE%E7%89%87/%E5%88%9B%E5%BB%BA%E9%BB%91%E7%99%BD%E5%9B%BE%E7%89%871.py
    create the polar with 300-radius in the white background
    '''
    #shape = (circleradius, 2*circleradius, 3)      # y, x, RGB
    shape = (circleradius, 2*circleradius)          # 1-channel 8bit
    origin_img = np.zeros(shape, np.uint8)
    origin_img.fill(255)

    cv.circle(origin_img, circlecenter, 5, colorblack, -1)

    '''
    partition 300-radius as 10 kinds of distance
    '''
    arclineindex = 1
    cv.circle(origin_img, circlecenter, int(arclineindex*circlearclinedisdiff), colorblack, thickness)
    arclineindex += 1
    cv.circle(origin_img, circlecenter, int(arclineindex*circlearclinedisdiff), colorblack, thickness)
    arclineindex += 1
    cv.circle(origin_img, circlecenter, int(arclineindex*circlearclinedisdiff), colorblack, thickness)
    arclineindex += 1
    cv.circle(origin_img, circlecenter, int(arclineindex*circlearclinedisdiff), colorblack, thickness)
    arclineindex += 1
    cv.circle(origin_img, circlecenter, int(arclineindex*circlearclinedisdiff), colorblack, thickness)
    arclineindex += 1
    cv.circle(origin_img, circlecenter, int(arclineindex*circlearclinedisdiff), colorblack, thickness)
    arclineindex += 1
    cv.circle(origin_img, circlecenter, int(arclineindex*circlearclinedisdiff), colorblack, thickness)
    arclineindex += 1
    cv.circle(origin_img, circlecenter, int(arclineindex*circlearclinedisdiff), colorblack, thickness)
    arclineindex += 1
    cv.circle(origin_img, circlecenter, int(arclineindex*circlearclinedisdiff), colorblack, thickness)
    arclineindex += 1
    cv.circle(origin_img, circlecenter, int(arclineindex*circlearclinedisdiff), colorblack, thickness)
    arclineindex += 1


    '''
    base: polarimage origin frame
    x = x0 + r*cos(theta)
    y = y0 - r*sin(theta)
    ---------------------
    base: rtsp origin frame (x', y': 0->polarimage origin frame)
    x'' = x + x'
    y'' = y + y'
    '''
    linetheta = 0
    linept2 = (int(circlecenter[0] + circleradius*math.cos(math.radians(linetheta))), int(circlecenter[1] - circleradius*math.sin(math.radians(linetheta))))
    cv.line(origin_img, circlecenter, linept2, colorblack, thickness)
    linetheta += 15
    linept2 = (int(circlecenter[0] + circleradius*math.cos(math.radians(linetheta))), int(circlecenter[1] - circleradius*math.sin(math.radians(linetheta))))
    cv.line(origin_img, circlecenter, linept2, colorblack, thickness)
    linetheta += 15
    linept2 = (int(circlecenter[0] + circleradius*math.cos(math.radians(linetheta))), int(circlecenter[1] - circleradius*math.sin(math.radians(linetheta))))
    cv.line(origin_img, circlecenter, linept2, colorblack, thickness)
    linetheta += 15
    linept2 = (int(circlecenter[0] + circleradius*math.cos(math.radians(linetheta))), int(circlecenter[1] - circleradius*math.sin(math.radians(linetheta))))
    cv.line(origin_img, circlecenter, linept2, colorblack, thickness)
    linetheta += 15
    linept2 = (int(circlecenter[0] + circleradius*math.cos(math.radians(linetheta))), int(circlecenter[1] - circleradius*math.sin(math.radians(linetheta))))
    cv.line(origin_img, circlecenter, linept2, colorblack, thickness)
    linetheta += 15
    linept2 = (int(circlecenter[0] + circleradius*math.cos(math.radians(linetheta))), int(circlecenter[1] - circleradius*math.sin(math.radians(linetheta))))
    cv.line(origin_img, circlecenter, linept2, colorblack, thickness)
    linetheta += 15
    linept2 = (int(circlecenter[0] + circleradius*math.cos(math.radians(linetheta))), int(circlecenter[1] - circleradius*math.sin(math.radians(linetheta))))
    cv.line(origin_img, circlecenter, linept2, colorblack, thickness)
    linetheta += 15
    linept2 = (int(circlecenter[0] + circleradius*math.cos(math.radians(linetheta))), int(circlecenter[1] - circleradius*math.sin(math.radians(linetheta))))
    cv.line(origin_img, circlecenter, linept2, colorblack, thickness)
    linetheta += 15
    linept2 = (int(circlecenter[0] + circleradius*math.cos(math.radians(linetheta))), int(circlecenter[1] - circleradius*math.sin(math.radians(linetheta))))
    cv.line(origin_img, circlecenter, linept2, colorblack, thickness)
    linetheta += 15
    linept2 = (int(circlecenter[0] + circleradius*math.cos(math.radians(linetheta))), int(circlecenter[1] - circleradius*math.sin(math.radians(linetheta))))
    cv.line(origin_img, circlecenter, linept2, colorblack, thickness)
    linetheta += 15
    linept2 = (int(circlecenter[0] + circleradius*math.cos(math.radians(linetheta))), int(circlecenter[1] - circleradius*math.sin(math.radians(linetheta))))
    cv.line(origin_img, circlecenter, linept2, colorblack, thickness)
    linetheta += 15
    linept2 = (int(circlecenter[0] + circleradius*math.cos(math.radians(linetheta))), int(circlecenter[1] - circleradius*math.sin(math.radians(linetheta))))
    cv.line(origin_img, circlecenter, linept2, colorblack, thickness)
    linetheta += 15
    linept2 = (int(circlecenter[0] + circleradius*math.cos(math.radians(linetheta))), int(circlecenter[1] - circleradius*math.sin(math.radians(linetheta))))
    cv.line(origin_img, circlecenter, linept2, colorblack, thickness)

    '''
    origin_img = cv.cvtColor(origin_img, cv.COLOR_BGR2BGRA)         # 因為是 jpg，要轉換顏色為 BGRA
    gray_img = cv.cvtColor(origin_img, cv.COLOR_BGR2GRAY)           # 新增 gray 變數為轉換成灰階的圖片

    # 依序取出圖片中每個像素
    for x in range(2*circleradius):
        for y in range(circleradius):
            if gray_img[y, x]>200:
                origin_img[y, x, 3] = 255 - gray_img[y, x]
                # 如果該像素的灰階度大於 200，調整該像素的透明度
                # 使用 255 - gray[y, x] 可以將一些邊緣的像素變成半透明，避免太過鋸齒的邊緣
    cv.imshow('gray_img', gray_img)
    '''

    cv.imshow('origin_img', origin_img)
    cv.imwrite('origin_img.bmp', origin_img)    # 存檔儲存為 png

    cv.waitKey(0)


def ImageMatting():
    origin_img = cv.imread('origin_img.bmp', cv.IMREAD_UNCHANGED)
    mask_img = cv.imread('bg_origin_img.bmp')                    # 遮罩圖片
    mask = cv.cvtColor(mask_img, cv.COLOR_BGR2GRAY)    # 轉換成灰階模式
    output = cv.bitwise_and(origin_img, origin_img, mask=mask)  # 加入 mask 參數
    cv.imshow('output', output)
    cv.imwrite('output_img.bmp', output)    # 存檔儲存為 png
    cv.waitKey(0)

def GenerateRedPt():
    shape = (32, 32, 1)          # 1-channel 8bit
    pt_img = np.zeros(shape, np.uint8)
    pt_img.fill(255)

    cv.circle(pt_img, (16, 16), 16, 0, -1)

    pt_img = cv.applyColorMap(pt_img, cv.COLORMAP_AUTUMN) 

    cv.imshow('pt_img', pt_img)
    cv.imwrite('pt_img.bmp', pt_img)    # 存檔儲存為 png
    cv.waitKey(0)


if __name__ == "__main__":
    GenerateRedPt()
    #GeneratePolarCoordinate()
    #GenerateWhiteBG()
    #ImageMatting()
