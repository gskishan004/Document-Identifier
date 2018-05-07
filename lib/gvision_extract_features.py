#Using google vision api to identify the doc 
import io
import os


# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types
from google.oauth2 import service_account


def print_label_annotations(annotations):
	print('Labels:')

	if annotations:
		for label in annotations:
			print(label.description)


def print_web_annotations(annotations):
    print('Web:')

    if annotations.pages_with_matching_images:
        print('\n{} Pages with matching images retrieved'.format(
            len(annotations.pages_with_matching_images)))

        for page in annotations.pages_with_matching_images:
            print('Url   : {}'.format(page.url))

    if annotations.full_matching_images:
        print ('\n{} Full Matches found: '.format(
               len(annotations.full_matching_images)))

        for image in annotations.full_matching_images:
            print('Url  : {}'.format(image.url))

    if annotations.partial_matching_images:
        print ('\n{} Partial Matches found: '.format(
               len(annotations.partial_matching_images)))

        for image in annotations.partial_matching_images:
            print('Url  : {}'.format(image.url))


    if annotations.web_entities:
        print ('\n{} Web entities found: '.format(
            len(annotations.web_entities)))

        for entity in annotations.web_entities:
            print('Score      : {}'.format(entity.score))
            print('Description: {}'.format(entity.description))

def extract_features(file_name):

    # Get the keyfile
    key_file = os.path.abspath(os.curdir) + "\\resources\\key.json"

    credentials = service_account.Credentials.from_service_account_file(key_file)


    # Instantiates a client
    client = vision.ImageAnnotatorClient(credentials = credentials)


    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    # Performs label detection on the image file
    label_annotations   = client.label_detection(image=image).label_annotations
    web_detection       = client.web_detection(image=image).web_detection

    print_label_annotations(label_annotations)
    print_web_annotations(web_detection)