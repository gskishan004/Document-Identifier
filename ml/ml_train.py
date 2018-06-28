import subprocess
from ml.lib.resizer 			import resize
from ml.lib.divide_data 		import divide
from ml.lib.xml_to_csv			import main_xml_to_csv
from ml.lib.generate_tfrecord 	import main_tfrecords
from ml.lib.train 				import main_train
from ml.lib.configure    		import main_configure

def train():
	# resize the pic which are larger than 200KB each or their resolution is more than 720x1280
	resize()

	# split the data into training and test dir
	divide()

	# run labelImg.exe
	returnValue = subprocess.call(["ml\\labelImg.exe"])
	if (returnValue == 0):
		print ("Success")
	else :
		print ("Unexpected termination while labeling the data")

	# run python xml_to_csv.py
	main_xml_to_csv()

	# replace the  code in generate_record.py below line 30

	# generate train tfrecords 

	train_csv_input 	= "ml\\models\\research\\object_detection\\images\\train_labels.csv"
	train_image_dir 	= "ml\\models\\research\\object_detection\\images\\train"
	train_output_path 	= "ml\\models\\research\\object_detection\\train.record"

	main_tfrecords(train_csv_input, train_image_dir, train_output_path)


	# generate test tfrecords 

	test_csv_input 		= "ml\\models\\research\\object_detection\\images\\test_labels.csv"
	test_image_dir 		= "ml\\models\\research\\object_detection\\images\\test"
	test_output_path 	= "ml\\models\\research\\object_detection\\test.record"

	main_tfrecords(test_csv_input, test_image_dir, test_output_path)


	# create labelmap.pbtxt in training folder

	# configure file in \training\faster_rcnn_inception_v2_pets.config file
	main_configure(num_classes=3, num_examples=10)


	#set PYTHONPATH=C:\Users\Lenovo\Desktop\Document_Identifier\ml\models;C:\Users\Lenovo\Desktop\Document_Identifier\ml\models\research;C:\Users\Lenovo\Desktop\Document_Identifier\ml\models\research\slim;C:\Users\Lenovo\Desktop\Document_Identifier\ml\models\research\object_detection


	# start the training
	train_dir 			="ml/models/research/object_detection/training/"
	pipeline_config_path="ml/models/research/object_detection/training/faster_rcnn_inception_v2_pets.config"

	main_train(train_dir, pipeline_config_path)