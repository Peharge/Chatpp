import torch
import torchvision.transforms as transforms
from torchvision.models.detection import fasterrcnn_resnet50_fpn
from PIL import Image, ImageDraw
import tkinter as tk
from tkinter import filedialog
import requests

# Laden des vortrainierten Faster R-CNN-Modells
rcnn_model = fasterrcnn_resnet50_fpn(pretrained=True)
rcnn_model.eval()

# Klassebezeichnungen für COCO-Datensatz (91 Klassen)
COCO_INSTANCE_CATEGORY_NAMES = [
    '__background__', 'person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck', 'boat',
    'traffic light', 'fire hydrant', 'N/A', 'stop sign', 'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse',
    'sheep', 'cow', 'elephant', 'bear', 'zebra', 'giraffe', 'N/A', 'backpack', 'umbrella', 'N/A', 'N/A', 'handbag',
    'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball', 'kite', 'baseball bat', 'baseball glove',
    'skateboard', 'surfboard', 'tennis racket', 'bottle', 'N/A', 'wine glass', 'cup', 'fork', 'knife', 'spoon',
    'bowl', 'banana', 'apple', 'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake',
    'chair', 'couch', 'potted plant', 'bed', 'N/A', 'dining table', 'N/A', 'N/A', 'toilet', 'N/A', 'tv', 'laptop',
    'mouse', 'remote', 'keyboard', 'cell phone', 'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'N/A',
    'book', 'clock', 'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush'
]

# Funktion zur Objekterkennung und Visualisierung mit Faster R-CNN
def detect_objects(image):
    transform = transforms.Compose([transforms.ToTensor()])
    image_tensor = transform(image)

    with torch.no_grad():
        prediction = rcnn_model([image_tensor])[0]

    draw = ImageDraw.Draw(image)

    for score, label, box in zip(prediction['scores'], prediction['labels'], prediction['boxes']):
        if score > 0.5:  # Nur Objekte mit hoher Vertrauenswürdigkeit berücksichtigen
            label_name = COCO_INSTANCE_CATEGORY_NAMES[label.item()]
            draw.rectangle([(box[0], box[1]), (box[2], box[3])], outline="red", width=3)
            draw.text((box[0], box[1]), f'{label_name} {score:.2f}', fill="red")

    image.show()

# Funktion zur Auswahl eines Bildes vom Desktop
def select_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        image = Image.open(file_path)
        detect_objects(image)

# GUI erstellen
root = tk.Tk()
root.title("Object recognition")

# Pfad zum Bild
icon_path = "C:\\Users\\julia\\OneDrive - Gewerbeschule Lörrach\\Pictures\\software\\peharge-logo3.6.ico"

# Setzen des Fenster-Icons
root.iconbitmap(icon_path)
root.geometry("200x75")

button = tk.Button(root, text="choose picture", command=select_image)
button.pack(pady=20)

root.mainloop()
