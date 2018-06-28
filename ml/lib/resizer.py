# resize only the images which are > 200KB or their resolution is more than 720x1280 

import numpy as np
import cv2
import os
from PIL import Image



def resize():
	CWD_PATH = os.getcwd()
	dir_path = os.path.join(CWD_PATH,'ml','data')

	for filename in os.listdir(dir_path):
		# If the images are not .JPG images, change the line below to match the image type.
		if filename.endswith(".jpg") or filename.endswith(".jpeg"):

			imageloc = dir_path + "/" + filename 

			im = Image.open(imageloc)
			width, height 	= im.size

			file_size 		= os.path.getsize(imageloc) / 1000

			if (min(width,height)>900) or file_size>1000:
				print ("\nImage is resized")
				print ("Filename 				: ", filename)
				print ("Dimensions of Image are : ", im.size)
				print ("Size of the file is 	: ", file_size)
				image = cv2.imread(imageloc)
				resized = cv2.resize(image,None,fx=0.125, fy=0.125, interpolation=cv2.INTER_AREA)
				cv2.imwrite(imageloc,resized)