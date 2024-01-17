from ultralytics import YOLO
import sys

model = YOLO("best.pt")

if __name__ == "__main__":
    print(sys.argv)
    results = model(sys.argv[1:])
    for r in results:
        r.save_txt("results.txt")