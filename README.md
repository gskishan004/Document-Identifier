# Document-Identifier
Document Identifier is a software with harnesses the power of various API in GCP along with Machine learning to sort various legal documents. The legal documents can include passports, driving licences etc.
Machine learning is implemented using tensorflow.




Currently the program supports images in jpeg format



* Save GCP key as "key.json" in resources folder.
* Clone this repo
* clone tensorflow repo from  https://github.com/tensorflow/models and move to ml dir
* download faster_rcnn_inception_v2_coco_2018_01_28 http://download.tensorflow.org/models/object_detection/faster_rcnn_inception_v2_coco_2018_01_28.tar.gz
* Extract the faster_rcnn_inception_v2_coco_2018_01_28 folder to the models\research\object_detection folder
* Set python path to the ablove   : set PYTHONPATH= < * REPLACE THIS WITH REPO LOCATION * >\Document_Identifier\ml\models;< * REPLACE THIS WITH REPO LOCATION * >\Document_Identifier\ml\models\research;< * REPLACE THIS WITH REPO LOCATION * >\Document_Identifier\ml\models\research\slim;< * REPLACE THIS WITH REPO LOCATION * >\Document_Identifier\ml\models\research\object_detection


Run
* pip install -r requirements.txt
* python -m spacy download en_core_web_lg
* python doc_iden.py --dir < location of dir >

optional flags:

--detectUsingML
--startTrain  



# * Delete all checkpoints in the training folder *

run ML using 
python main_ml.py



Incase of error while running first command, consider running terminal with Admin privilages


# Tasks:

## On Going:

- [ ] Program reads all the files from dir 
- [ ] Integrate train and predict flags for ML
- [ ] Integrate Tensorflow model
- [ ] Annotate all the images
- [ ] fix predictor.py
- [ ] Get Keys for GCP 
- [ ] Collate all google API to one file

## Done:
- [x] Developed a fairly stable version of document identifier
- [x] Remove darknet dependencies (function for converting the data to YOLO format etc..) 
- [x] PPT stating the reson for choosing TF or darknet

