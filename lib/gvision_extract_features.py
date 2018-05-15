#Using google vision api to identify the doc 
import io
import os


# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types
from google.oauth2 import service_account


def get_label_annotations(annotations):

    labels = []

    if annotations:
        for label in annotations:
            labels.append((label.description, label.score))

    return labels

def get_web_annotations(annotations):

    webs   = []

    if annotations.web_entities:

        for entity in annotations.web_entities:
            if entity.description:
                webs.append((entity.description, entity.score))
    return webs

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

    labels = get_label_annotations(label_annotations)
    webs   = get_web_annotations(web_detection)

    features = labels + webs 

    return features