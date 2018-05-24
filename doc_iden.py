from lib.gvision_extract_features 	import extract_features
from lib.direct_matcher 			import direct_match
from lib.spacy_nlp 					import spacy_nlp_match
from lib.doc_category               import find_best_doc_category
from lib.training_data				import save_for_training

import sys
import os
import platform

if (len(sys.argv) < 2):
	print ("Provide image name as command line argument")
	sys.exit(0)

if (platform.system() == "Windows"):
	os.system('cls')
else:
	os.system('clear')

file_name = 'test_images/' + sys.argv[1] + '.jpg'

#***************************************************
#           PHASE -- I (Doc Identifier)
#***************************************************

features 			 = extract_features(file_name)
gvision_direct_match = direct_match    (features)
gvision_nlp_match    = spacy_nlp_match (features)

predictions 		 = gvision_direct_match + gvision_nlp_match


#***************************************************
#         PLACEHOLDER for Future funtions
#***************************************************

# ocr_nlp_match()
# cnn_match()
# ocr_ml_match()


result 				= find_best_doc_category(predictions)

if result:
	print('\nDocument identified as : {} with {:.2f}% confidence\n'.format(result[0], result[1]*100))
else :
	print('\nDocument not matched with any predefined categories\n')

is_pred_correct = input ("Press Y if the prediction is correct, otherwise press N : ")

if (is_pred_correct.upper() == 'Y'):
	save_for_training(image_name = sys.argv[1], category = result[0])

elif (is_pred_correct.upper() == 'N'):
	correct_pred = input ("Please enter the correct label")
	save_for_training(image_name = sys.argv[1], category = correct_pred)

else:
	print('Incorrect input, image discared')



