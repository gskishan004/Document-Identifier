reference 
https://github.com/EdjeElectronics/TensorFlow-Object-Detection-API-Tutorial-Train-Multiple-Objects-Windows-10

Steps:

* Clone tf models repo in a folder https://github.com/tensorflow/models


* Download the model http://download.tensorflow.org/models/object_detection/faster_rcnn_inception_v2_coco_2018_01_28.tar.gz and copy its contents to ..models\research\object_detection folder

* Download the repo https://github.com/EdjeElectronics/TensorFlow-Object-Detection-API-Tutorial-Train-Multiple-Objects-Windows-10

* Delete the following files (do not delete the folders):

All files in \object_detection\images\train and \object_detection\images\test
The “test_labels.csv” and “train_labels.csv” files in \object_detection\images
All files in \object_detection\training
All files in \object_detection\inference_graph


* install all the necessary packages using pip install -r requirements.txt

* set python path
set PYTHONPATH=C:\Users\Lenovo\Desktop\Document_Identifier\ml_using_tf\models;C:\Users\Lenovo\Desktop\Document_Identifier\ml_using_tf\models\research;C:\Users\Lenovo\Desktop\Document_Identifier\ml_using_tf\models\research\slim

* run
protoc --python_out=. .\object_detection\protos\anchor_generator.proto .\object_detection\protos\argmax_matcher.proto .\object_detection\protos\bipartite_matcher.proto .\object_detection\protos\box_coder.proto .\object_detection\protos\box_predictor.proto .\object_detection\protos\eval.proto .\object_detection\protos\faster_rcnn.proto .\object_detection\protos\faster_rcnn_box_coder.proto .\object_detection\protos\grid_anchor_generator.proto .\object_detection\protos\hyperparams.proto .\object_detection\protos\image_resizer.proto .\object_detection\protos\input_reader.proto .\object_detection\protos\losses.proto .\object_detection\protos\matcher.proto .\object_detection\protos\mean_stddev_box_coder.proto .\object_detection\protos\model.proto .\object_detection\protos\optimizer.proto .\object_detection\protos\pipeline.proto .\object_detection\protos\post_processing.proto .\object_detection\protos\preprocessor.proto .\object_detection\protos\region_similarity_calculator.proto .\object_detection\protos\square_box_coder.proto .\object_detection\protos\ssd.proto .\object_detection\protos\ssd_anchor_generator.proto .\object_detection\protos\string_int_label_map.proto .\object_detection\protos\train.proto .\object_detection\protos\keypoint_box_coder.proto .\object_detection\protos\multiscale_anchor_generator.proto .\object_detection\protos\graph_rewriter.proto





**** after setup.py delete all the folders except object detector and move that to the outermost dir


* convert all the images to jpg:
https://sourceforge.net/projects/bulkimageconver/