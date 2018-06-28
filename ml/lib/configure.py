import os

debug = 0


def main_configure(num_classes, num_examples):

	CWD_PATH = os.getcwd()
	fname = os.path.join(CWD_PATH,'ml','models','research','object_detection','training','faster_rcnn_inception_v2_pets.config').replace("\\", "/")
	fine_tune_checkpoint = os.path.join(CWD_PATH,'ml','models','research','object_detection','faster_rcnn_inception_v2_coco_2018_01_28','model.ckpt').replace("\\", "/")
	input_path = os.path.join(CWD_PATH,'ml','models','research','object_detection','train.record').replace("\\", "/")
	label_map_path = os.path.join(CWD_PATH,'ml','models','research','object_detection','training','labelmap.pbtxt').replace("\\", "/")
	input_path = os.path.join(CWD_PATH,'ml','models','research','object_detection','test.record').replace("\\", "/")


	with open(fname, 'r') as file:
	    # read a list of lines into data
	    data = file.readlines()

	print ("Configuring "+fname)

	if (debug):
		print ("Old lines \n")
		print (data[8])
		print (data[105])
		print (data[121])
		print (data[123])
		print (data[127])
		print (data[135])
		print (data[137])


	data[8]   = "    num_classes: "+str(num_classes)+"\n"
	data[105] = "  fine_tune_checkpoint: \""+fine_tune_checkpoint+"\""+"\n"
	data[121] = "    input_path: \""+input_path+"\""+"\n"
	data[123] = "  label_map_path: \""+label_map_path+"\""+"\n"
	data[127] = "  num_examples: "+str(num_examples)+"\n"
	data[135] = "    input_path: \""+input_path+"\""+"\n"
	data[137] = "  label_map_path: \""+label_map_path+"\""+"\n"

	if (debug):
		print ("New lines \n")
		print (data[8])
		print (data[105])
		print (data[121])
		print (data[123])
		print (data[127])
		print (data[135])
		print (data[137])



	# and write everything back
	with open(fname, 'w') as file:
	    file.writelines( data )