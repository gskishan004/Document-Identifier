import os
import glob
import pandas as pd
import argparse
import sys
import platform

CWD_PATH = os.getcwd()


p1 = os.path.join(CWD_PATH,'ml','models')
p2 = os.path.join(CWD_PATH,'ml','models','research')
p3 = os.path.join(CWD_PATH,'ml','models','research','slim')
p4 = os.path.join(CWD_PATH,'ml','models','research','object_detection')

sys.path.append(p1)
sys.path.append(p2)
sys.path.append(p3)
sys.path.append(p4)

from   doc_iden                 import main_doc_iden
from   ml.ml_predict            import predict
from   ml.ml_train              import train
from   ml.ml_predict_multiple   import predict_multiple

def sort_doc(path,ml_flag):


    doc_list = []
    for file in glob.glob(path + '/*.jpg'):
        

        if(ml_flag):
            print ("Using cutom ML model to process ",file)
            output_folder, confidence = predict(file)

        else:
            print ("Using GCP APIs to process ", file)
            output_folder, confidence = main_doc_iden(file) 
            
        move_file(file, output_folder)    

def move_file(input_path, output_path):

    output_path    = os.path.join(os.getcwd(), ("output/"+output_path))
    file_name = input_path.rsplit('\\', 1)[1]
    print ("File name ", file_name) 

    if not os.path.exists(output_path):
        os.makedirs(output_path)


    os.rename(input_path, output_path+"\\"+file_name)


if (platform.system() == "Windows"):
    os.system('cls')
else:
    os.system('clear')


parser = argparse.ArgumentParser(description='Sort the identification docs into output folder')
parser.add_argument('-i', '--input' , default="input",
					dest='i', 
					help='define the input dir')
parser.add_argument('-m', '--useML'	, action='store_true', default=False,
                    dest='m_arg',
                    help='Use ML for docuemnt prediction')
parser.add_argument('-t', '--train' , action='store_true', default=False,
                    dest='t_arg',
                    help='Train the model')
parser.add_argument('-s', '--segregate' , action='store_true', default=False,
                    dest='s_arg',
                    help='Segregate multiple docs from a image')

args = parser.parse_args()

if args.i == 'input':
    parser.print_help()
    print ("\nUsing default dir for input")

folder     = args.i
ml_flag    = args.m_arg
train_flag = args.t_arg
seg_flag   = args.s_arg

image_dir  = os.path.join(os.getcwd(), (folder))

if(train_flag):
    print ("Training the model")
    train()

elif(seg_flag):
    print ("Segregating the doc")
    predict_multiple(image_dir+"\\test.jpg")

else:
    sort_doc(image_dir,ml_flag)