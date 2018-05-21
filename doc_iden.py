from lib.gvision_extract_features 	import extract_features
from lib.direct_matcher 			import direct_match
from lib.spacy_nlp 					import spacy_nlp_match
from lib.doc_category               import find_best_doc_category
from lib.training_data				import save_for_training

import sys
import os

#file_name = raw_input("Input File : ")
#file_name = 'test_images/1.jpg'

if (len(sys.argv) < 2):
	print ("Provide image name as command line argument")
	sys.exit(0)

file_name = 'test_images/' + sys.argv[1] + '.jpg'

#***************************************************
#           PHASE -- I (Doc Identifier)
#***************************************************

features 			 = extract_features(file_name)
gvision_direct_match = direct_match    (features)
gvision_nlp_match    = spacy_nlp_match (features)

predictions 		 = gvision_direct_match + gvision_nlp_match

# print ("Featues 				: ", features)
# print ("gvision_direct_match	: ", gvision_direct_match)
# print ("gvision_nlp_match		: ", gvision_nlp_match)


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

result 				= find_best_doc_category(predictions)

if result:
	print('Document identified as : {} with {:.2f}% confidence'.format(result[0], result[1]*100))
else :
	print('Document not matched with any predefined categories')

is_pred_correct = input ("Press Y if the prediction is correct, otherwise press N : ")

if (is_pred_correct.upper() == 'Y'):
	save_for_training(image_name = sys.argv[1], category = result)

elif (is_pred_correct.upper() == 'N'):
	correct_pred = input ("Please enter the correct label")
	save_for_training(image_name = sys.argv[1], category = correct_pred)

else:
	print('Incorrect input, image discared')
