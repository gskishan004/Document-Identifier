# Document-Identifier

* Save GCP key as "key.json" in resources folder.
* download https://pjreddie.com/media/files/darknet19_448.conv.23

* follow steps in http://www.horstmann.com/ccc/help/cygwin/install.html to install cygwin
* open cygwin to navigate to darknet dir and run "make" cmd


Run
* pip install -r requirements.txt
* python -m spacy download en_core_web_lg
* python doc_iden.py < name of the image >


ML related commands - refer readme inside ml_using_tf dir

# * Delete all checkpoints in the training folder *

run ML using 
python main_ml.py



Incase of error while running first command, consider running terminal with Admin privilages


# Tasks:

## Done:
- [x] Finalize between 3 options : Image -> OCR -> ML (or) Image -> ML (YOLO/CNN) (or) Image -> Google Vision API.
- [X] Code for direct match.
- [X] Code for spacy_nlp_match
- [X] Complete 1st master - gvision_feature_pred 
- [X] Segregate Code into 4 masters - gvision_feature_pred, ocr_nlp_pred, cnn_pred, ocr_ml_pred
- [X] Fix multiple lines in doc_type bug
- [X] Code for OCR in gvision_extract_features
- [X] Complete 2nd module 
- [X] Clean origional dir after converting the data - [FIXED by not opening the file in append model
- [X] Make baisc pipeline for training 
- [X] Convert function to get data ready for YOLO
- [X] Category function to dynamically assign category to a numeric value
- [X] Modify the convert function to read one file at a time
- [X] Integrate YOLO v2 model (CLOSED)

## On Going:

- [ ] Remove darknet dependencies (function for converting the data to YOLO format etc..) 
- [ ] Integrate Tensorflow model
- [ ] PPT stating the reson for choosing TF or darknet
- [ ] Annotate all the images
- [ ] fix predictor.py
- [ ] Get Keys for GCP 
- [ ] Collate all google API to one file



## * Replacing Darknet YOLO model with Tensorflow - objection detection model *


