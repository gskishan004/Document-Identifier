from PIL import Image
import os

folder = 'data'

def create_xml(image_name, category):

	cwd = os.getcwd()
	image_loc = cwd+ "\\data\\"+image_name+".jpg"
	txt_path  = "data/"+image_name

	width, height = 0, 0

	with Image.open(image_loc) as im:
		width, height = im.size

	xmin   	= 2
	ymin   	= 2
	xmax	= width - 2
	ymax	= height - 2

	
	
	txt_file = open(txt_path, "w")
	l1  = "<annotation>\n"
	l2  = "  <folder>"+folder+"</folder>\n"
	l3  = "  <filename>"+image_name+"</filename>\n"
	l4  = "  <path>"+image_loc+"</path>\n"
	l5  = "  <source>\n"
	l6  = "    <database>Unknown</database>\n"
	l7  = "  </source>\n"
	l8  = "  <size>\n"
	l9  = "    <width>"+str(width)+"</width>\n"
	l10 = "    <height>"+str(height)+"</height>\n"
	l11 = "    <depth>3</depth>\n"
	l12 = "  </size>\n"
	l13 = "  <segmented>0</segmented>\n"
	l14 = "  <object>\n"
	l15 = "    <name>"+category+"</name>\n"
	l16 = "    <pose>Unspecified</pose>\n"
	l17 = "    <truncated>0</truncated>\n"
	l18 = "    <difficult>0</difficult>\n"
	l19 = "    <bndbox>\n"
	l20 = "      <xmin>"+str(xmin)+"</xmin>\n"
	l21 = "      <ymin>"+str(ymin)+"</ymin>\n"
	l22 = "      <xmax>"+str(xmax)+"</xmax>\n"
	l23 = "      <ymax>"+str(ymax)+"</ymax>\n"
	l24 = "    </bndbox>\n"
	l25 = "  </object>\n"
	l26 = "</annotation>"

	txt_file.writelines([l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,l16,l17,l18,l19,l20,l21,l22,l23,l24,l25,l26])

for i in range (1,12):
	create_xml("0_"+str(i), "passport")