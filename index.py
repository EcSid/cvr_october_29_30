from networkx.algorithms.bipartite.cluster import modes
from ultralytics import YOLO
import cv2
from ultralytics.utils.plotting import Annotator  # ultralytics.yolo.utils.plotting is deprecated
import math
from ultralytics import YOLO

# Загружаем предобученную модель YOLOv8
model = YOLO('C:/Users/025/Desktop/myYolo/best.pt') # Выберите размер модели: n, s, m, l, x

cap = cv2.VideoCapture(1)

cap.set(4, 640) #cap.set(3, 640)
cap.set(3, 480) #cap.set(4, 480)

boxCords = []
while True:
    _, img = cap.read()
    _, img = cap.read()

    # BGR to RGB conversion is performed under the hood
    # see: https://github.com/ultralytics/ultralytics/issues/2575
    results = model.predict(img) #сканируем изображения на модели
    for r in results:
        annotator = Annotator(img) #с помощью класс анататора и объекта анататор добавляем на картинку модели, которые распознала нейросеть
        boxes = r.boxes
        for box in boxes:
            b = box.xyxy[0]  # get box coordinates in (top, left, bottom, right) format
            c = box.cls
            boxCords.append(b)
            annotator.box_label(b, model.names[int(c)])
    cv2.imshow('YOhttps://habr.com/ru/articles/593 547/LO V8 Detection', img)
    if cv2.waitKey(1) & 0xFF == ord(' '):
        break
cap.release()
cv2.destroyAllWindows()