# Document-Identifier
Document Identifier is a software which harnesses the power of GCP API's along with Machine learning to sort documents into folders. 

Legal documents can include passports, driving licences etc. of any country. Machine learning is implemented using tensorflow.


Currently the program supports jpg images and docx files.

## Setup

* clone this repo

* Save GCP key as "key.json" in resources folder

* clone tensorflow repo from  https://github.com/tensorflow/models 

* copy models dir to ml folder

* download faster_rcnn_inception_v2_coco_2018_01_28 http://download.tensorflow.org/models/object_detection/faster_rcnn_inception_v2_coco_2018_01_28.tar.gz

* Extract the faster_rcnn_inception_v2_coco_2018_01_28 folder to the ml\models\research\object_detection folder


Run the following :
* pip install -r requirements.txt

* python -m spacy download en_core_web_lg

* conda install -c anaconda protobuf

Change directories to the \ml\models\research directory and run the following:
* protoc --python_out=. .\object_detection\protos\anchor_generator.proto .\object_detection\protos\argmax_matcher.proto .\object_detection\protos\bipartite_matcher.proto .\object_detection\protos\box_coder.proto .\object_detection\protos\box_predictor.proto .\object_detection\protos\eval.proto .\object_detection\protos\faster_rcnn.proto .\object_detection\protos\faster_rcnn_box_coder.proto .\object_detection\protos\grid_anchor_generator.proto .\object_detection\protos\hyperparams.proto .\object_detection\protos\image_resizer.proto .\object_detection\protos\input_reader.proto .\object_detection\protos\losses.proto .\object_detection\protos\matcher.proto .\object_detection\protos\mean_stddev_box_coder.proto .\object_detection\protos\model.proto .\object_detection\protos\optimizer.proto .\object_detection\protos\pipeline.proto .\object_detection\protos\post_processing.proto .\object_detection\protos\preprocessor.proto .\object_detection\protos\region_similarity_calculator.proto .\object_detection\protos\square_box_coder.proto .\object_detection\protos\ssd.proto .\object_detection\protos\ssd_anchor_generator.proto .\object_detection\protos\string_int_label_map.proto .\object_detection\protos\train.proto .\object_detection\protos\keypoint_box_coder.proto .\object_detection\protos\multiscale_anchor_generator.proto .\object_detection\protos\graph_rewriter.proto


Delete all checkpoints in the training folder

Incase of error while running first command, consider running terminal with Admin privilages

## Running the code

* python main.py

### Optional flags:

-m : predict only using ML 

-t : train the model

* After the model is trained press Ctrl + C and run the following command from object_detection dir (where XXXX is highest checkpoint number)
* python export_inference_graph.py --input_type image_tensor --pipeline_config_path training/faster_rcnn_inception_v2_pets.config --trained_checkpoint_prefix training/model.ckpt-XXXX --output_directory inference_graph

-i : use another dir for input (By default input dir is taken as input)


# Tasks:

## On Going:

- [ ] remove dependency on user for running export_inference_graph
- [ ] Get Keys for GCP 
- [ ] Create global config file with paths to path_labels etc in predict.py
- [ ] Segregate various docs from an image (As google vision API does a bad job at this, we will use our custom trained models)
- [ ] Create script to form more complex training data form exiting training data.

## Done:
- [x] Developed a fairly stable version of document identifier
- [x] Remove darknet dependencies (function for converting the data to YOLO format etc..) 
- [x] PPT stating the reson for choosing TF or darknet
- [X] fix predictor
- [X] Program reads all the files from dir 
- [X] Integrate prediction code with main.py
- [x] Code to simplify training by removing manual steps involved
- [X] Integrate trainig code with main.py
- [X] remove dependency on user for running set pythonpath