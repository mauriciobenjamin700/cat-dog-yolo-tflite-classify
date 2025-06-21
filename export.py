from ultralytics import YOLO

ID = 10

model = YOLO(f"dist/class{ID}/weights/best.pt")

model.export(format="onnx")

print(f"Model exported to ONNX format for class {ID}.")