from PIL import Image, ImageEnhance, ImageFilter
import os


path = './images'  #folder containing images to be edited
pathOut = '/editedImages' #output folder containing edited images

for filename in os.listdir(path): #iterate through all files/images in path
    img = Image.open(f"{path}/{filename}") #this variable holds the opened image object
    
    edit = img.filter(ImageFilter.SHARPEN).convert('L').rotate(-90) #edit the image by sharpening,convert to grayscale, rotate to portrait 
    
    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit) 
    
    edit = enhancer.enhance(factor) #add more contrast to the edited image
    
    clean_name = os.path.splitext(filename)[0] #clean the image name
    
    edit.save(f'.{pathOut}/{clean_name}_edited.png') #save the edited image in pathOut folder with cleaned name
    
    
    
