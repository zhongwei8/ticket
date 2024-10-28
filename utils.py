import os
import cv2
from pathlib import Path


class COLORS:
    colors = [
        (255, 0, 0),    # 红色
        (0, 255, 0),    # 绿色
        (0, 0, 255),    # 蓝色
        (255, 255, 0),  # 青色
        (255, 0, 255),  # 品红色
        (0, 255, 255),  # 黄色
        (128, 0, 128),  # 紫色
        (255, 165, 0),  # 橙色
        (192, 192, 192),# 银色
        (0, 0, 0),      # 黑色
    ]

def get_image_path(src_dir: str) -> list:
    return [f for f in os.listdir(src_dir) if f.endswith(('.jpg', '.png'))]

def add_circle(img, ps = ps):
    for p in ps:
        cv2.circle(img, p, 10, (0, 0, 255), 4)
        print(f"p = {p}")



def get_image_files(src_dir: Path, recursion = False):
    src_dir = Path(src_dir)
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']

    if rescursion:
        image_files = [file for file in directory.rglob('*') if file.suffix.lower() in image_extensions]
    else:
        image_files = [file for file in directory.glob('*') if file.suffix.lower() in image_extensions]

    image_files = [str(file.absolute()) for file in image_files]

    return image_files

