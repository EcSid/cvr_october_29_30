import cv2
import math
cap = cv2.VideoCapture(0)


while True:
    ret, frame =  cap.read()
    key = cv2.waitKey(1)
    print(len(frame[0])) #размер изображения(матрицы)
    print(frame[0])
    height, width, _ = frame.shape
    lengthY= math.ceil(height * 0.52)
    #длина массива frame равна высоте экрана в пикселях (и каждый элемент этого массива - это массив x координат)
    x_center = width // 2
    y_center = height // 2
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #преобразуем из rgb в hsv
    # frame --- массив с каждым пикелем и цветом этого пикселя(можно разместить черный квадрат используя срезу (с 1 по 100 пиксель чёрный, то есть равен [0, 0, 0] по rgb
    for x in frame[y_center-(lengthY // 2):y_center+(lengthY//2)]:
        x[x_center-(lengthY // 2):x_center+(lengthY // 2)] = [0, 0, 0] #первый параметр - y, второй x
    cv2.imshow('камера', frame)
    if key == ord(' '):
        break
    print(key)
    #print(ret)
    #print(frame)

cv2.destroyAllWindows() #закрываем все окна
cap.release() #отключаем доступ к камере