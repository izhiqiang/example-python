import cv2

def faceSpot(imgpath):
    """
    opencv find face
    :imgpath: path
    """
    # 读取图片
    img = cv2.imread(imgpath)
    # 转换灰色
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # OpenCV人脸识别分类器
    classifier = cv2.CascadeClassifier(
        "opencv/data/haarcascades/haarcascade_frontalface_default.xml"
    )
    # 调用识别人脸
    faceRects = classifier.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4, minSize=(10, 10))
    print(faceRects)
    for (x, y, w, h) in faceRects:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 绘制矩形框
    cv2.imshow("image", img)  # 显示图像
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    imgpath = "images/1.jpg"
    faceSpot(imgpath)

