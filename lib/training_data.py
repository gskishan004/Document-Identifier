from PIL 			import Image
from lib.convert	import yolo_format_convert
import os

def save_for_training(image_name,category):

	category_id 	= get_category(category)


	image_loc		= "test_images/" 		+ image_name + ".jpg"
	train_img_name  = "data/yolo_format/" 	+ image_name + ".jpg"
	doc_file 		= "data/original/"		+ image_name + ".txt"

	im = Image.open(image_loc)
	

	width, height = im.size
	width  		  = width  - 5
	height		  = height - 5

	bbox = "0 "+str(height)+" "+str(width)+" 0" 

	

	mode = 'a' if os.path.exists(doc_file) else 'w'
	with open(doc_file, mode) as f:
		f.write(category_id+"\n"+bbox)


	im.save(train_img_name)
	

	print ("Image saved for training in data folder")

	yolo_format_convert(category_id)

	print ("Image converted to YOLO format")


def get_category(category):
	
	cat_id = "0"
	
	return cat_id