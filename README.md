# Document-Identifier

Save GCP key as "key.json" in the root dir

Run
	pip install -r requirements.txt
	python doc_iden.py
	python -m spacy download en_core_web_lg

Incase of error while running first command, consider running terminal with Admin privilages


# Tasks:

## Done:
- [x] Finalize between 3 options : Image -> OCR -> ML (or) Image -> ML (YOLO/CNN) (or) Image -> Google Vision API.
- [X] Code for direct match.
- [X] Code for spacy_nlp_match
- [X] Complete 1st master - gvision_feature_pred 
- [X] Segregate Code into 4 masters - gvision_feature_pred, ocr_nlp_pred, cnn_pred, ocr_ml_pred.
- [X] Fix multiple lines in doc_type bug

## On Going:
- [ ] Code for OCR in gvision_extract_features
- [ ] Get Keys for GCP.
- [ ] Collate all google API to one file