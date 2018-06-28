# Import packages
import os
import cv2
import numpy as np
import tensorflow as tf
import sys


# Import utilites
from utils import label_map_util
from utils import visualization_utils as vis_util


def find_category(categories, classInt):
	for category in categories:
		if category['id'] == classInt:
			return category['name']

def predict(img_name):

	# This is needed since the notebook is stored in the object_detection folder.
	sys.path.append("..")


	# Name of the directory containing the object detection module we're using
	MODEL_NAME = 'inference_graph'
	IMAGE_NAME = str(img_name)

	# Grab path to current working directory
	CWD_PATH = os.getcwd()

	# Path to frozen detection graph .pb file, which contains the model that is used
	# for object detection.

	PATH_TO_CKPT = os.path.join(CWD_PATH,'ml','models','research','object_detection',MODEL_NAME,'frozen_inference_graph.pb')

	# Path to label map file
	PATH_TO_LABELS = os.path.join(CWD_PATH,'ml','models','research','object_detection','training','labelmap.pbtxt')

	# Path to image
	PATH_TO_IMAGE = os.path.join(CWD_PATH,IMAGE_NAME)

	# Number of classes the object detector can identify
	NUM_CLASSES = 3

	# Load the label map.
	# Label maps map indices to category names, so that when our convolution
	# network predicts `5`, we know that this corresponds to `king`.
	# Here we use internal utility functions, but anything that returns a
	# dictionary mapping integers to appropriate string labels would be fine
	label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
	categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
	category_index = label_map_util.create_category_index(categories)



	# Load the Tensorflow model into memory.
	detection_graph = tf.Graph()
	with detection_graph.as_default():
	    od_graph_def = tf.GraphDef()
	    with tf.gfile.GFile(PATH_TO_CKPT, 'rb')  as fid:
	        serialized_graph = fid.read()
	        od_graph_def.ParseFromString(serialized_graph)
	        tf.import_graph_def(od_graph_def, name='')

	    sess = tf.Session(graph=detection_graph)

	# Define input and output tensors (i.e. data) for the object detection classifier

	# Input tensor is the image
	image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')

	# Output tensors are the detection boxes, scores, and classes
	# Each box represents a part of the image where a particular object was detected
	detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')

	# Each score represents level of confidence for each of the objects.
	# The score is shown on the result image, together with the class label.
	detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
	detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')



	# Number of objects detected
	num_detections = detection_graph.get_tensor_by_name('num_detections:0')

	# Load image using OpenCV and
	# expand image dimensions to have shape: [1, None, None, 3]
	# i.e. a single-column array, where each item in the column has the pixel RGB value
	image = cv2.imread(PATH_TO_IMAGE)
	image_expanded = np.expand_dims(image, axis=0)

	# Perform the actual detection by running the model with the image as input
	(boxes, scores, classes, num) = sess.run(
	    [detection_boxes, detection_scores, detection_classes, num_detections],
	    feed_dict={image_tensor: image_expanded})

	# Draw the results of the detection (aka 'visulaize the results')

	print ("Number of detections :", num_detections)

	i               = 0 
	classNo         = []

	maxConfidence   = max(scores[0])

	for score in scores[0]:
	    
	    if score == maxConfidence:
	        print ("\nConfidence : ",score*100,
	               "\nClass      : ",find_category(categories, classes[0][i]),
	               "\nBox Coordn : ",boxes[0][i])
	        classNo = i
	    i+=1

	return (find_category(categories, classes[0][classNo]), scores[0][classNo]*100)
