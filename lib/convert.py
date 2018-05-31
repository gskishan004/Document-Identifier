# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 14:55:43 2015

This script is to convert the txt annotation files to appropriate format needed by YOLO 

@author: Guanghan Ning
Email: gnxr9@mail.missouri.edu
"""

import os
from os import walk, getcwd
from PIL import Image


def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)
    
    
def yolo_format_convert(category, txt_path, image_name):
    """-------------------------------------------------------------------""" 

    """ Configure Paths"""   
    mypath  = "data/original/"
    outpath = "data/yolo_format/"

    print("Input file     : " + txt_path)
    txt_file = open(txt_path, "r")
    lines = txt_file.read().split('\n')   #for ubuntu, use "\r\n" instead of "\n"
    
    """ Open output text files """
    txt_outpath = outpath + image_name + ".txt"
    print("Output file    : " + txt_outpath)
    txt_outfile = open(txt_outpath, "w")
    
    
    """ Convert the data to YOLO format """
    ct = 0
    for line in lines:
        #print('lenth of line is: ')
        #print(len(line))
        #print('\n')
        if(len(line) >= 2):
            ct = ct + 1
            elems = line.split(' ')
            print("Input data     :",elems)
            xmin = elems[0]
            xmax = elems[2]
            ymin = elems[1]
            ymax = elems[3]
            #
            img_path = str('data/yolo_format/'+ image_name +'.jpg')
            #t = magic.from_file(img_path)
            #wh= re.search('(\d+) x (\d+)', t).groups()
            im=Image.open(img_path)
            w= int(im.size[0])
            h= int(im.size[1])
            #w = int(xmax) - int(xmin)
            #h = int(ymax) - int(ymin)
            # print(xmin)
            b = (float(xmin), float(xmax), float(ymin), float(ymax))
            bb = convert((w,h), b)
            print("Converted data :",bb)
            txt_outfile.write(str(category) + " " + " ".join([str(a) for a in bb]) + '\n')

    

    return 0   