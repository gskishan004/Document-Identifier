# Document-Identifier
Document Identifier is a software which harnesses the power of various API in GCP along with Machine learning to sort legal documents. 
Legal documents can include passports, driving licences etc. of any country.
Machine learning is implemented using tensorflow.




Currently the program supports images in jpeg format

## Setup

* Save GCP key as "key.json" in resources folder

* Clone this repo

* clone tensorflow repo from  https://github.com/tensorflow/models 

* copy models dir indide ml dir

* download faster_rcnn_inception_v2_coco_2018_01_28 http://download.tensorflow.org/models/object_detection/faster_rcnn_inception_v2_coco_2018_01_28.tar.gz

* Extract the faster_rcnn_inception_v2_coco_2018_01_28 folder to the models\research\object_detection folder

* set PYTHONPATH = < * REPLACE THIS WITH REPO LOCATION * >\ml\models;< * REPLACE THIS WITH REPO LOCATION * >\ml\models\research;< * REPLACE THIS WITH REPO LOCATION * >\ml\models\research\slim;< * REPLACE THIS WITH REPO LOCATION * >\ml\models\research\object_detection


Run the following :
* pip install -r requirements.txt

* conda install -c anaconda protobuf

Change directories to the \models\research directory and run the following:
* protoc --python_out=. .\object_detection\protos\anchor_generator.proto .\object_detection\protos\argmax_matcher.proto .\object_detection\protos\bipartite_matcher.proto .\object_detection\protos\box_coder.proto .\object_detection\protos\box_predictor.proto .\object_detection\protos\eval.proto .\object_detection\protos\faster_rcnn.proto .\object_detection\protos\faster_rcnn_box_coder.proto .\object_detection\protos\grid_anchor_generator.proto .\object_detection\protos\hyperparams.proto .\object_detection\protos\image_resizer.proto .\object_detection\protos\input_reader.proto .\object_detection\protos\losses.proto .\object_detection\protos\matcher.proto .\object_detection\protos\mean_stddev_box_coder.proto .\object_detection\protos\model.proto .\object_detection\protos\optimizer.proto .\object_detection\protos\pipeline.proto .\object_detection\protos\post_processing.proto .\object_detection\protos\preprocessor.proto .\object_detection\protos\region_similarity_calculator.proto .\object_detection\protos\square_box_coder.proto .\object_detection\protos\ssd.proto .\object_detection\protos\ssd_anchor_generator.proto .\object_detection\protos\string_int_label_map.proto .\object_detection\protos\train.proto .\object_detection\protos\keypoint_box_coder.proto .\object_detection\protos\multiscale_anchor_generator.proto .\object_detection\protos\graph_rewriter.proto

* python -m spacy download en_core_web_lg

* Delete all checkpoints in the training folder *
Incase of error while running first command, consider running terminal with Admin privilages

## Running the code

* python main.py

### Optional flags:

-m : predict only using ML 
-t : train the model
-i : use another dir for input (By default input dir is taken as input)


# Tasks:

## On Going:
- [ ] Train flag for ML
- [ ] Get Keys for GCP 
- [ ] Code to simplify training by removing manual steps involved

## Done:
- [x] Developed a fairly stable version of document identifier
- [x] Remove darknet dependencies (function for converting the data to YOLO format etc..) 
- [x] PPT stating the reson for choosing TF or darknet
- [X] fix predictor
- [X] Program reads all the files from dir 
- [X] Predict flag for ML

