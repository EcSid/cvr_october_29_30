from ultralytics import YOLO
# Загружаем предобученную модель YOLOv8
model = YOLO('yolov8n.pt') # Выберите размер модели: n, s, m, l, x
# Запускаем обучение
model.train(data='config.yaml', epochs=20, batch=10, imgsz=640)

results = model.predict(source='C:/Users/025/Desktop/robots/robot.jpg', conf=0.5)
results.show()