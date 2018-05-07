# Document-Identifier

Save GCP key as "key.json" in the root dir

Run
	pip install -r requirements.txt
	python doc_iden.py
	export GOOGLE_APPLICATION_CREDENTIALS = "key.json"
	python -m spacy download en_core_web_lg

Incase of error while running first command, consider running terminal with Admin privilages


Tasks:
- [x] Finalize between 3 options : Image -> OCR -> ML (or) Image -> ML (YOLO/CNN) (or) Image -> Google Vision API.
- [ ] Get Keys for GCP.
- [X] Code for direct match.
- [X] Code for spacy_nlp_match.
- [ ] Collate all google API to one file
- [ ] Complete 1st master - gvision_feature_pred 
- [ ] Segregate Code into 4 masters - gvision_feature_pred, ocr_nlp_pred, cnn_pred, ocr_ml_pred.