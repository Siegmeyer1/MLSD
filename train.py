from ultralytics import YOLO, settings


print(settings)
model = YOLO('runs/detect/train/weights/best.pt')
model.train(data='dataset.yaml', device='mps', epochs=30)