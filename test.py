from glob import glob
from ultralytics import YOLO
from ultralytics.engine.results import Results, Probs

ID = 10

model = YOLO(f"dist/class{ID}/weights/best.pt")


cat = glob("data/Cat/*.jpg")[:10]
dog = glob("data/Dog/*.jpg")[:10]

cat_results: list[Results] = model(cat, imgsz=224, device="0")

print("Cat results:")
for result in cat_results:
    probs: Probs = result.probs
    print(f"Image: {result.path}, Class: {probs.top1:.8f}, Confidence: {probs.top1conf:.8f}")

dog_results = model(dog, imgsz=224, device="0")

print("Dog results:")
for result in dog_results:
    probs: Probs = result.probs
    print(f"Image: {result.path}, Class: {probs.top1:.8f}, Confidence: {probs.top1conf:.8f}")