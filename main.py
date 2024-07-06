from PIL import Image, ImageDraw, ImageOps, ImageFilter
import argparse

parser = argparse.ArgumentParser(description='')

parser.add_argument("--file_name", action="store", help="Выводит название файла", default="photo.jpg") 
parser.add_argument("--bw_photo", action="store_true")
parser.add_argument("--contrast_photo", action="store_true")
parser.add_argument("--blurry_photo", action="store_true")
parser.add_argument("--median_photo", action="store_true")
parser.add_argument("--frame_photo", action="store_true")
parser.add_argument("--sepia_photo", action="store_true")

args = parser.parse_args()

# print("Название файла:", args.output)

def make_filter_bw(image):
    filter_bw = image.convert('L')
    filter_bw.save("filters_for_photos/bw_photo.jpg")


def make_filter_contrast(image):
    filter_contrast = ImageOps.autocontrast(image, cutoff=5)
    filter_contrast.save("filters_for_photos/contrast_photo.jpg")

def make_filter_blurring(image):
    blurring_filter = image.filter(ImageFilter.GaussianBlur(radius=2))
    blurring_filter.save("filters_for_photos/blur_photo.jpg")


def make_filter_median(image):
    median_filter = image.filter(ImageFilter.MedianFilter(size=3))
    median_filter.save("filters_for_photos/median_photo.jpg")

def make_filter_frame(image):
    width = 1200
    height =  980
    width, height = image.size
    frame_image = image.transform((width + 100, height + 100), Image.EXTENT,
                        (-10, -10, width + 10, height + 10), Image.BILINEAR)
    frame_image.save("filters_for_photos/frame_image.jpg")

def make_filter_rgb(image):
    sepia_r = 112
    sepia_g = 66
    sepia_b = 20
    sepia_image = Image.new('RGB', image.size)
    for x in range(image.width):
        for y in range(image.height):
            r, g, b = image.getpixel((x,y))
            new_r = int(r * 0.393 + g * 0.769 + b * 0.189)
            new_g = int(r * 0.349 + g * 0.686 + b * 0.168)
            new_b = int(r * 0.272 + g * 0.534 + b * 0.131)
            sepia_r = min(new_r, 255)
            sepia_g = min(new_g, 255)
            sepia_b = min(new_b, 255)
            sepia_image.putpixel((x,y), (sepia_r, sepia_g, sepia_b))
    sepia_image.save("filters_for_photos/sepia_image.jpg") 


def main():
    print("Название файла:", args.file_name)
    print("Использование черно-белого фильтра:", args.bw_photo)
    print("Использование контрастного фильтра:", args.contrast_photo)
    print("Использование фильтра размытия:", args.blurry_photo)
    print("Использование медианного фильтра:", args.median_photo)
    print("Использование рамки:", args.frame_photo)
    print("Использование фильтра сепии:", args.sepia_photo)
    user_image = Image.open(f"image/{args.file_name}")
    filters = [
        make_filter_bw,
        make_filter_contrast,
        make_filter_blurring,
        make_filter_median,
        make_filter_frame,
        make_filter_rgb
    ]

    if args.bw_photo == True: 
       make_filter_bw(user_image)
    if args.contrast_photo == True:
        make_filter_contrast(user_image)
    if args.blurry_photo == True:
        make_filter_blurring(user_image)
    if args.median_photo == True:
        make_filter_median(user_image)
    if args.frame_photo == True:
        make_filter_frame(user_image)
    if args.sepia_photo == True:
        make_filter_rgb(user_image)
    # for filter in filters:
    #     filter(user_image) 

        

if __name__ == "__main__":
    main()