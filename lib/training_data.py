from PIL 			import Image
from lib.convert	import yolo_format_convert

import os
import sys

def save_for_training(image_name,category):

	category_id 	= get_category(category)


	image_loc		= "test_images/" 		+ image_name + ".jpg"
	train_img_name  = "data/yolo_format/" 	+ image_name + ".jpg"
	doc_file 		= "data/original/"		+ image_name + ".txt"

	with Image.open(image_loc) as im:

		width, height = im.size
		width  		  = width  - 5
		height		  = height - 5

		bbox = "0 "+str(height)+" "+str(width)+" 0" 
	
		with open(doc_file, 'w') as f:
			f.write(category_id+"\n"+bbox)

		im.save(train_img_name)

	print ("Saving data for training")

	yolo_format_convert(category_id, doc_file, image_name)

	print ("Converted and saved data to YOLO format")


def get_category(category):
	


	doc_file = os.path.abspath(os.curdir) + "\\resources\\doc_types.txt"

	with open(doc_file) as f:
		category_id = 0 
		for line in f:
			# replace function removes hidden \n from the line
			if (line.lower().replace("\n","") in category.lower()):
				return str(category_id)
			category_id += 1

	print ("No category found for the document")
	sys.exit(0)