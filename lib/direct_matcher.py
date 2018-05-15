import os 

def direct_match(features):

	doc_file = os.path.abspath(os.curdir) + "\\resources\\doc_types.txt"

	matches = []

	with open(doc_file) as f:
		for line in f:
			if (features):
				for feature in features:
					if (line.lower() in feature[0].lower()):
						matches.append(feature)

	return matches