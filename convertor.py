import os
from PIL import Image
from tqdm import tqdm


def resize_and_crop(img, target_size):
    # Вычисляем соотношение
    target_ratio = target_size[0] / target_size[1]
    img_ratio = img.width / img.height

    if img_ratio > target_ratio:
        # изображение шире → обрезаем по ширине
        new_width = int(img.height * target_ratio)
        left = (img.width - new_width) // 2
        img = img.crop((left, 0, left + new_width, img.height))
    else:
        # изображение выше → обрезаем по высоте
        new_height = int(img.width / target_ratio)
        top = (img.height - new_height) // 2
        img = img.crop((0, top, img.width, top + new_height))

    return img.resize(target_size, Image.Resampling.LANCZOS)

def convertor(images, current_dir, size):
    for image_path in tqdm( images, desc="Converting ", unit="image", unit_scale=False, colour="#44ff88", dynamic_ncols=True, miniters=1, leave=True):
        filename = os.path.basename(image_path)
        name_without_ext = os.path.splitext(filename)[0]
        output_name = name_without_ext + ".webp"
        output_path = os.path.join(current_dir, output_name)
        if not size:
            try:
                with Image.open(image_path) as img:
                    img.save(output_path, "WEBP", quality=90, method=6)
                    tqdm.write(f"{filename} → {output_name}")
                    os.remove(image_path)
            except Exception as e:
                tqdm.write(f"Conversion error {filename}: {e}")
        else:
            try:
                with Image.open(image_path) as img:
                    resized_img = resize_and_crop(img, size)
                    resized_img.save(output_path, "WEBP", quality=90, method=6)
                    tqdm.write(f"{filename} → {output_name}")
                    os.remove(image_path)
            except Exception as e:
                tqdm.write(f"Conversion error {filename}: {e}")

