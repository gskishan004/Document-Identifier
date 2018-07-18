from   PIL 	import Image
import os
import sys


# this function now just saves the data in ml/data dir
def save_for_training(image_name):
	image_loc		= "test_images/" 		+ image_name + ".jpg"
	train_img_name  = "ml/data/" 			+ image_name + ".jpg"

	with Image.open(image_loc) as im:

		im = im.convert('RGB')
		im.save(train_img_name)