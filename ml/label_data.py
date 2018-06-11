import subprocess

# split the data randomly into training and test dir
# resize the pic which are larger than 200KB each or their resolution is more than 720x1280
# run labelImg.exe
# run python xml_to_csv.py
# replace the  code in generate_record.py:

# generate tf records by running the following 
# python generate_tfrecord.py --csv_input=images\train_labels.csv --image_dir=images\train --output_path=train.record
# python generate_tfrecord.py --csv_input=images\test_labels.csv --image_dir=images\test --output_path=test.record

# create labelmap.pbtxt in training folder

# make the following changes in \samples\configs\faster_rcnn_inception_v2_pets.config file
# line 9 	num_classes : 3
# Line 110	fine_tune_checkpoint : "C:/tensorflow1/models/research/object_detection/faster_rcnn_inception_v2_coco_2018_01_28/model.ckpt
# Line 126	input_path : "C:/tensorflow1/models/research/object_detection/train.record"
# Line 128	label_map_path: "C:/tensorflow1/models/research/object_detection/training/labelmap.pbtxt"
# Line 132	Change num_examples to number of images in test dir
# Line 140 	input_path : "C:/tensorflow1/models/research/object_detection/test.record"
# Line 142	label_map_path: "C:/tensorflow1/models/research/object_detection/training/labelmap.pbtxt"

# run the training 
# python train.py --logtostderr --train_dir=training/ --pipeline_config_path=training/faster_rcnn_inception_v2_pets.config

returnValue = subprocess.call(["labelImg.exe"])

if (returnValue == 0):

	

else :
	print ("Unexpected termination while labeling the data")