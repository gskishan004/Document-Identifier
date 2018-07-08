import zipfile
import glob
import os

def main_word_doc_iden(path):
	file_names = []

	for file in glob.glob(path + '/*.docx'):

		print ("\nProcessing ", file)

		z = zipfile.ZipFile(file)

		#files in zip archive
		all_files = z.namelist()

		#get all files in word/media/ directory
		images = filter(lambda x: x.startswith('word/media/'), all_files)
		for image in images:

			#open each image and save it 
			image_temp = z.open(image).read()

			image_name = str(image)
			image_name = image_name.replace("word/media/","")
			image_name = file + image_name
			image_name = image_name.replace(".docx","_")

			print ("Extracting image ", image_name)
			file_names.append(image_name)

			f = open(image_name,'wb')
			f.write(image_temp)
	print ("\n")
	
	return file_names

def remove_doc_files(path):
	# Delete the word files
	for file in glob.glob(path + '/*.docx'):	
		os.remove(file)
