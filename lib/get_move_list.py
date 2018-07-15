#output_folder_list = [("DL","abc.img"), ("COI","123.img"), ("NM","42.img"), ("NM","412.img"), ("COO","213wd.img"), ("DL","idf.img"), ("COO","dsfasd.img"), ("NM","dfsd.img"), ("NM","dfsdw.img"), ("COO","d123.img"),("COI","9584.img"), ("NM","d231.img"), ("NM","12.img"), ("COI2","dcd.img"), ("NM","df21.img"), ("NM","23156.img")]

#doc_spans_multiple_page = ["COI", "COI2","COO"]

def supported_doc(folder,doc_spans_multiple_page):
	for doc in doc_spans_multiple_page:
		if (folder.lower() == doc.lower()):
			return 1
	return 0

def check_if_not_equal(filename, files_to_remove_list):
	for i in range (0,len(files_to_remove_list)):
		if (filename == files_to_remove_list[i]):
			return 0
	return 1

def main_get_move_list(output_folder_list, doc_spans_multiple_page):
	final_move_list= []
	files_to_remove = []
	start_list = []
	end_list = []
	doc_type_list = []

	for i in range (0, len(output_folder_list)):
		if (supported_doc(output_folder_list[i][0], doc_spans_multiple_page)):
			doc_type_list.append(output_folder_list[i][0])
			j = i
			while (output_folder_list[j][0] == "No_Match" or output_folder_list[j][0] == output_folder_list[i][0]):
				if (j+1 > len(output_folder_list)-1):
					j+=1
					break
				else:
					j+=1

			start_list.append (i)
			end_list.append (j-1)
			i = min (j+1, len(output_folder_list))

	for i in range (0, len(doc_type_list)):
		folder_name = output_folder_list[start_list[i]][0] + "_" + str(i)
		for j in range (start_list[i], end_list[i] + 1):
			files_to_remove.append(output_folder_list[j][1])
			final_move_list.append((output_folder_list[j][1], folder_name))

	files_to_remove = list (set(files_to_remove))

	for i in range (0, len(output_folder_list)):
		if (check_if_not_equal (output_folder_list[i][1],files_to_remove)):
			final_move_list.append((output_folder_list[i][1], output_folder_list[i][0]))


	return final_move_list