import subprocess
from lib.resizer 			import resize
from lib.divide_data 		import divide
from lib.xml_to_csv			import main_xml_to_csv
from lib.generate_tfrecord 	import main_tfrecords
from lib.train 				import main_train

# resize the pic which are larger than 200KB each or their resolution is more than 720x1280
resize()

# split the data into training and test dir
divide()

# run labelImg.exe
returnValue = subprocess.call(["labelImg.exe"])
if (returnValue == 0):
	print ("Success")
else :
	print ("Unexpected termination while labeling the data")

# run python xml_to_csv.py
main_xml_to_csv()

# replace the  code in generate_record.py below line 30

# generate train tfrecords 

train_csv_input 	= "models\\research\\object_detection\\images\\train_labels.csv"
train_image_dir 	= "models\\research\\object_detection\\images\\train"
train_output_path 	= "models\\research\\object_detection\\train.record"

main_tfrecords(train_csv_input, train_image_dir, train_output_path)


# generate test tfrecords 

test_csv_input 		= "models\\research\\object_detection\\images\\test_labels.csv"
test_image_dir 		= "models\\research\\object_detection\\images\\test"
test_output_path 	= "models\\research\\object_detection\\test.record"

main_tfrecords(test_csv_input, test_image_dir, test_output_path)


# create labelmap.pbtxt in training folder

# make the following changes in \training\faster_rcnn_inception_v2_pets.config file
# line 9 	num_classes : 3
# Line 110	fine_tune_checkpoint : "C:/tensorflow1/models/research/object_detection/faster_rcnn_inception_v2_coco_2018_01_28/model.ckpt
# Line 126	input_path : "C:/tensorflow1/models/research/object_detection/train.record"
# Line 128	label_map_path: "C:/tensorflow1/models/research/object_detection/training/labelmap.pbtxt"
# Line 132	Change num_examples to number of images in test dir
# Line 140 	input_path : "C:/tensorflow1/models/research/object_detection/test.record"
# Line 142	label_map_path: "C:/tensorflow1/models/research/object_detection/training/labelmap.pbtxt"


#set PYTHONPATH=C:\Users\Lenovo\Desktop\Document_Identifier\ml\models;C:\Users\Lenovo\Desktop\Document_Identifier\ml\models\research;C:\Users\Lenovo\Desktop\Document_Identifier\ml\models\research\slim;C:\Users\Lenovo\Desktop\Document_Identifier\ml\models\research\object_detection


# start the training
train_dir 			="models/research/object_detection/training/"
pipeline_config_path="models/research/object_detection/training/faster_rcnn_inception_v2_pets.config"

main_train(train_dir, pipeline_config_path)

#python export_inference_graph.py --input_type image_tensor --pipeline_config_path object_detection/training/faster_rcnn_inception_v2_pets.config --trained_checkpoint_prefix object_detection/training/model.ckpt-XXXX --output_directory object_detection/inference_graph




