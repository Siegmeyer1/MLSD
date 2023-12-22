from ultralytics import YOLO, settings


print(settings)
model = YOLO('yolov8n.yaml')
model.train(data='dataset.yaml', device='mps', epochs=3)