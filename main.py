# coding=utf-8

#
# 160060 Gabriel Acosta Belchior
#
# Coloque uma imagem chamada watermark.png no mesmo diretório deste script
# A pasta de imagens pode ser qualquer uma, você poderá informá-la ao rodar o programa
#

import cv2
import os

watermark = cv2.imread("watermark.png")
watermark = cv2.resize(watermark, (64, 64), interpolation=cv2.INTER_AREA)

imgDir = input("Diretório para procurar imagens: ")
images = os.listdir(imgDir)
imgLen = len(images)

print("Imagens contidas no diretório:")
print("\n".join(images))

def imreadProcessed(imgName):
    img = cv2.imread(imgDir + "\\" + imgName)
    img = cv2.resize(img, (512, 512), interpolation=cv2.INTER_AREA)
    cv2.line(img, (0, 0), (512, 0), (255,255,255), thickness=40)
    cv2.line(img, (0, 0), (0, 512), (255,255,255), thickness=10)
    cv2.line(img, (0, 512), (512, 512), (255,255,255), thickness=10)
    cv2.line(img, (512, 512), (512, 0), (255,255,255), thickness=10)

    img[438:438+64, 438:438+64] = img[438:438+64, 438:438+64] * 0.5 + watermark * 0.5
    cv2.putText(img, imgName, (10, 15), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), thickness=1)

    return img

def fadeIn(img1, img2):
    for i in range(0, 100, 3):
        r = cv2.addWeighted(img2, i / 100.0, img1, 1 - (i / 100.0), 0)
        cv2.imshow('Img', r)
        key = cv2.waitKey(5)
        if (key == 81 | key == 113):
            cv2.destroyAllWindows()
            exit()
        elif (key > 0):
            break

    cv2.imshow('Img', img2)

def main():

    curIdx = -1
    lastKeyPressed = -1

    while True:
        if lastKeyPressed == 81 | lastKeyPressed == 113:
            cv2.destroyAllWindows()
            exit()

        if lastKeyPressed != 2424832:
            curIdx = curIdx + 1 if curIdx + 1 < imgLen else 0
            img1 = imreadProcessed(images[curIdx])
            img2 = imreadProcessed(images[curIdx + 1 if curIdx + 1 < imgLen else 0])
        else:
            curIdx = curIdx - 1 if curIdx - 1 >= 0 else imgLen - 1
            img1 = imreadProcessed(images[curIdx + 1 if curIdx + 1 < imgLen else 0])
            img2 = imreadProcessed(images[curIdx])

        fadeIn(img1, img2)
        lastKeyPressed = cv2.waitKeyEx(5000)
        

main()