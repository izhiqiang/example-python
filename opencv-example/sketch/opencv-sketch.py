import cv2

if __name__ == '__main__':
    # 读取图片
    img_rgb = cv2.imread("demo.jpg")
    # 转化灰度图
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
    # 高斯滤波进行图片模糊化
    img_blur = cv2.GaussianBlur(img_gray, ksize=(21, 21),sigmaX=0, sigmaY=0)
    # 原图和模糊图像进行融合
    img_edge = cv2.divide(img_gray, img_blur, scale=255)
    # 保存图片
    cv2.imwrite('4.jpg', img_edge)
