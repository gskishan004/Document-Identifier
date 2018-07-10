output_folder_list = ["DL", "COI", "NM", "NM", "COO", "DL", "COO", "NM", "NM", "COO","COI", "NM", "NM", "COI2", "NM", "NM"]
doc_spans_multiple_page = ["COI", "COI2"]

start_list = []
end_list = []
doc_type_list = []
COI_flag = 0

flag = 0

def supported_doc(folder):
	for doc in doc_spans_multiple_page:
		if (folder.lower() == doc.lower()):
			return 1
	return 0


for i in range (0, len(output_folder_list)):
	if (supported_doc(output_folder_list[i])):
		doc_type_list.append(output_folder_list[i])
		j = i
		while (output_folder_list[j] == "NM" or output_folder_list[j] == output_folder_list[i]):
			if (j+1 > len(output_folder_list)-1):
				j+=1
				break
			else:
				j+=1

		start_list.append (i)
		end_list.append (j-1)
		i = min (j+1, len(output_folder_list))




for i in range (0, len(doc_type_list)):
	print (" {} starts from {} and ends at {} ".format(doc_type_list[i],start_list[i], end_list[i]))
	for j in range (start_list[i], end_list[i] + 1):
		print (output_folder_list[j])