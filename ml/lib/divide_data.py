import glob, os

def divide():

	path_data 	= 'data'
	destination	= 'models/research/object_detection/images'

	# Percentage of images to be used for the test set
	percentage_test = 10;

	# Create and/or truncate train.txt and test.txt

	file_train 	= open('train.txt', 'w')  
	file_test   = open('test.txt', 'w')

	# Populate train.txt and test.txt
	counter = 1  
	index_test = round(100 / percentage_test)  
	for pathAndFilename in glob.iglob(os.path.join(path_data, "*.jpg")):  
		title, ext = os.path.splitext(os.path.basename(pathAndFilename))

		if counter == index_test:
			counter = 1
			file_test.write(path_data +'/'+ title + '.jpg' + "\n")
			os.rename(path_data +'/'+title+'.jpg', destination + '/test/' + title+'.jpg')

		else:
			file_train.write(path_data +'/'+ title + '.jpg' + "\n")

			os.rename(path_data +'/'+title+'.jpg', destination + '/train/' + title+'.jpg')
			counter = counter + 1