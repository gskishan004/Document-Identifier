import os 

def direct_match(features):

	doc_file = os.path.abspath(os.curdir) + "\\resources\\doc_types.txt"

	matches = []

	with open(doc_file) as f:
		for line in f:
			for feature in features:
				if (feature.lower() == line.lower()):
					matches.append(feature.lower())

	return matches