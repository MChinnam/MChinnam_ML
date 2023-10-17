import requests
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

import cv2

processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

#img_url = 'https://storage.googleapis.com/sfr-vision-language-research/BLIP/demo.jpg' 
img_path='/Users/fission/Desktop/b.png'
#raw_image = Image.open(requests.get(img_url, stream=True).raw).convert('RGB')

def imtext(image):


    #raw_image = Image.open(image).convert('RGB')
    raw_image = image
    #.convert('RGB')
   
    inputs = processor(raw_image, return_tensors="pt",)

    out = model.generate(**inputs)
    return (processor.decode(out[0], skip_special_tokens=True))

