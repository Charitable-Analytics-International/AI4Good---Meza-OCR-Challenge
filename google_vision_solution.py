import io
import os
import glob

# YOU NEED TO SETUP YOUR API KEY BEFORE RUNNING THIS

# Imports the Google Cloud client library
from google.cloud import vision

# Detects text in the file
def detect_text(path):
   
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')

    for text in texts:
        return str('{}'.format(text.description)).strip()


def main():

	# Fetch all the cell names
	fileNames = glob.glob("cell_images/validation_set/*")

	# Open a target file
	destFile = open("cell_images/google_vision_validation_predictions.txt","w+")
	destFile.write("filename;value\n")

	targetIndex = 2
	index = 0
	for file_name in fileNames:

		index = index + 1
	
		row_name = file_name.split("/")[-1]
		row_val = detect_text(file_name)
		if(row_val is None):
			row_val = ""

		new_row = row_name + ";" + row_val + "\n"
		print(str(index) + " : " + new_row)

		destFile.write(new_row)

	destFile.close()


# Run the program
main()
