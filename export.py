from ultralytics import YOLO

model = YOLO("dist/class5/weights/best.pt")

model.export(format="onnx", imgsz=224, device="cpu")