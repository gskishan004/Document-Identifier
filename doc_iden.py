from lib.gvision_extract_features 	import extract_features
from lib.direct_matcher 			import direct_match
from lib.spacy_nlp 					import spacy_nlp_match

#file_name = raw_input("Input File : ")

file_name = 'test_images/1.jpg'

#***************************************************
#                PHASE -- I
#***************************************************

# User Input for file name UI ??

# Google Vision API to extract features from Image

features 			 = extract_features(file_name)

gvision_direct_match = direct_match    (features)
gvision_nlp_match    = spacy_nlp_match (features)


#***************************************************
#         PLACEHOLDER for Future funtions
#***************************************************

# ocr_nlp_match()
# cnn_match()
# ocr_ml_match()

# Suggest closest match with confidence percentage

# Incase of discrepency ask the user to provide inputs

# Save the image with correct foder as its label name 

# Start the training in differnt thread as doc no reaches threshold

#***************************************************
#                PHASE -- II
#***************************************************

# extract_date(file_name)
