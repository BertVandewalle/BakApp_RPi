from PIL import Image
from PIL.ImageQt import ImageQt

def crop_center(pil_img:Image, crop_width, crop_height):
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_width) // 2,
                         (img_height - crop_height) // 2,
                         (img_width + crop_width) // 2,
                         (img_height + crop_height) // 2))

def crop_max_square(img_path):
    pil_img = Image.open(img_path)
    im = crop_center(pil_img, min(pil_img.size), min(pil_img.size))
    return im