def find_best_doc_category(predictions):
	if (predictions):
		return max(predictions,key=lambda item:item[1])
