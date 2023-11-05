import os

import cv2 as cv
from PIL import Image, ImageOps

class DIP:
    count = 0
    name = '' 
    DELAY = 100
    resize = (128, 128)
    def __init__(self, x, y):
        if x <= 0:
            raise Exception('Error! No. of images to be generated must be non-zero')
        if len(name) == 0:
            raise Exception('Error! Name must be non-empty')
        self.count = x
        self.name = y
        
    def capture_images(self):
        cam_port = 0
        cam = cv.VideoCapture(cam_port) 
        for i in range(self.count):
          print(f'Capturing image {i}...')
          result, image = cam.read()
          if result: 
              cv.imshow(self.name, image) 
              cv.imwrite(self.name + '_' + str(i) + ".png", image) 
              cv.waitKey(self.DELAY)
              cv.destroyWindow(self.name) 
          else:
            raise Exception("Error1 No image detected. Please! try again")
        print("Done acquiring the images...")

    def resize_images(self):
        for i in range(self.count):
            print(f'Processing image {i}...')
            im = Image.open(f'{self.name}_{i}.png')
            reim = im.resize(self.resize)
            fin = ImageOps.grayscale(reim)
            fin.save(f'min_{self.name}_{i}.png')
            os.remove(f'{name}_{i}.png')
        print('Done processing captured images...')
        
        
    

if __name__ == '__main__':
    name = input("Enter name of the person: ")
    count = int(input("Enter no. of images to be captured: "))
    try:
        obj = DIP(count, name)
        obj.capture_images()
        obj.resize_images()
        print('Database of images has been successfully generated')
    except Exception as e:
        print(e)
        print("Exiting program")
    
    
