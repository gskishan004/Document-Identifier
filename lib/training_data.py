from PIL import Image


def save_for_training(image_name,category):

	image_loc		= "test_images/" 	+ image_name + ".jpg"
	train_img_name  = "data/origional/" + image_name + ".jpg"
	doc_file 		= "data/origional/"	+ image_name + ".txt"

	im = Image.open(image_loc)
	category = get_category(category)
	category = str(category)

	width, height = im.size
	width  		  = width  - 5
	height		  = height - 5

	bbox = "0 "+str(height)+" "+str(width)+" 0" 

	with open(doc_file, "w+") as f:
		f.write(category+"\n"+bbox) 

	im.save(train_img_name)

	print ("Image saved for training in data folder")

def get_category(category):
	return 0