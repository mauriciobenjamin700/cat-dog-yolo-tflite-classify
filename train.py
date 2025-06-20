from glob import glob
from os.path import abspath
from ultralytics import YOLO    

cat_files = glob("data/Cat/*.jpg")
dog_files = glob("data/Dog/*.jpg")
data = abspath("data")

cat_files.sort()
dog_files.sort()

print("Number of cat images:", len(cat_files))
print("Number of dog images:", len(dog_files))

model = YOLO("yolo11n-cls.pt")

model.train(data=data, epochs=100, device=0, project="dist", name="class", batch=128, imgsz=224)

print("Training complete. Model saved in 'dist/class/weights/best.pt'.")