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

def get_document_text_detection():




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
    label_annotations       = client.label_detection(image=image).label_annotations
    web_detection           = client.web_detection(image=image).web_detection
    document_text_detection = client.document_text_detection(image=image).full_text_annotation

    labels = get_label_annotations(label_annotations)
    webs   = get_web_annotations(web_detection)
    ocr    = get_document_text_detection(document_text_detection)



    features = labels + webs 

    return features

def get_document_bounds(image_file, feature):
    """Returns document bounds given an image."""
    client = vision.ImageAnnotatorClient()

    bounds = []

    with io.open(image_file, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    response = client.document_text_detection(image=image)
    document = response.full_text_annotation

    # Collect specified feature bounds by enumerating all document features
    for page in document.pages:
        for block in page.blocks:
            for paragraph in block.paragraphs:
                for word in paragraph.words:
                    for symbol in word.symbols:
                        if (feature == FeatureType.SYMBOL):
                            bounds.append(symbol.bounding_box)

                    if (feature == FeatureType.WORD):
                        bounds.append(word.bounding_box)

                if (feature == FeatureType.PARA):
                    bounds.append(paragraph.bounding_box)

            if (feature == FeatureType.BLOCK):
                bounds.append(block.bounding_box)

        if (feature == FeatureType.PAGE):
            bounds.append(block.bounding_box)

    # The list `bounds` contains the coordinates of the bounding boxes.
    return bounds

def render_doc_text(filein, fileout):
    image = Image.open(filein)
    bounds = get_document_bounds(filein, FeatureType.PAGE)
    draw_boxes(image, bounds, 'blue')
    bounds = get_document_bounds(filein, FeatureType.PARA)
    draw_boxes(image, bounds, 'red')
    bounds = get_document_bounds(filein, FeatureType.WORD)
    draw_boxes(image, bounds, 'yellow')

    if fileout is not 0:
        image.save(fileout)
    else:
        image.show()