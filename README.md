# Handwritten clinical records for Optical Character Recognition 

![Screenshot](CAI-logo.png)

The United Nations World Food Program (WFP) has tasked Charitable Analytics
International (CAI) to develop a solution to it's digitization problem. WFP operates in
over 80 countries, where they deliver much needed supplies to health clinics, schools,
refugee camps, etc.

The areas where they operate often lack access to electricity, internet and cellphone coverage, and staff with
computer knowledge. These constraints make recording on paper the only form of bookkeeping possible. 
Lacking effective tools to digitize logbooks, WFP’s only option is to transport them back to a large 
city where every page is input manually. This process is tedious, expensive and prone to errors.

CAI is developing a software stack which would allow field workers to send photographs of their logbooks to a WhatsApp
phone number. The receiving WhatsApp account pushes the pictures to an image processing and visualization server.
One of the programs running on the server finds the spreadsheet in the images and cuts out every individual cell.

Our challenge for the AI4Good Hackathon is to develop a program able to convert the handwritten characters 
contained in the cell images into typed text. The provided training set contains labeled cell images of 
handwritten numerical values. They come from health clinics in the Republic of Congo. 
Use it to build your model and submit your validation set to our web server to see how you have done!

- [Validation Web Server](http://mezademo.charitableanalytics.org:8080)


As a reference Google Vision gives a score of 35.63%


## Quantitative Description of the Dataset

Training/Test Set = 7,497 labeled cells

Validation Set = 522 unlabeled cells

Format : Grayscale images of varying width and height

The images contain values expressed by this regex,
    
    ^[\-]?[0-9]*[\.\,]?[0-9]*$


The repository is organized with the following structure :
 
	cell_images/
		|
		|-> training_set_values.txt
		|		|
		|		|-> filename;value
		|		|-> 1.jpg;97
		|		|-> 2.jpg;18
		|		|-> ...;...
		|
		|-> training_set/
		|		|
		|		|-> 1.jpg
		|		|-> 2.jpg
		|		|-> ...
		|
		|
		|
		|-> validation_set_values.txt
		|		|
		|		|-> filename;value
		|		|-> 1.jpg;
		|		|-> 2.jpg;
		|		|-> ...;...
		|
		|-> validation_set/
		|		|
		|		|-> 1.jpg
		|		|-> 2.jpg
		|		|-> ...
		|
		|
		|
		|-> google_vision_validation_predictions.txt


## Demo of Meza

- [Meza Promo Video](https://youtu.be/G8NNF9lyKhA) - A video explanation of the Meza software stack
- [Meza Interactive Map](http://mezademo.charitableanalytics.org) - A demo of our web app


## Meza API

This API will be open for the duration of the hackathon. All the raw images, the processing images, the cell images and a csv containing the relationship between directory name and the sender phone number are available at :

	http://mezademo.charitableanalytics.org/imgs/


Use the interactive map to explore the data :

	1. Click on a clinic
	2. Click on one of the entry in the news feed
	3. Right click on the image and open in a new tab
	4. Play with the url to dive in the subdirectory


## Description of Charitable Analytics International

CAI helps organizations understand their data through concrete insights. We offer
unique and customized solutions to empower leaders doing social good. We focus on
tackling pressing real-world issues that have the biggest impact, with partners such as
the United Nations World Food Program and the National Democratic Institute. Our
core belief is that data technology can and should be a key tool in the mission to make
the world a better place.


## Basics

If this is your first time at a hackathon, it's probably best that you learn some concepts that'll help ramp you up before!

- [Learn Git Branching](https://learngitbranching.js.org/) - Interactive tutorial to learn Git, the most popular version control system for collaborative programming.
- [What's an API?](https://medium.freecodecamp.org/what-is-an-api-in-english-please-b880a3214a82) - Learn how to use external services in your projects.
- [A Beginner’s Guide to HTTP and REST](https://code.tutsplus.com/tutorials/a-beginners-guide-to-http-and-rest--net-16340) - A more in-depth guide on how to use REST APIs.
- [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/) - An in-depth series of tutorials to learn how to code in Python. If you don't know what language to use, Python is a good start!
- [Google Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course/ml-intro) - If you want to ramp up quick on machine learning.
- [MNIST Dataset](https://towardsdatascience.com/image-classification-in-10-minutes-with-mnist-dataset-54c35b77a38d) - A beginner-friendly image classification challenge. 

## Recommended Software

These are some recommended tools for general hackathon success:

- [Visual Studio Code](https://code.visualstudio.com/) - Your favorite programmer's favorite text editor.
- [GitHub Desktop](https://desktop.github.com/) - Easy-to-use Git GUI interface so you don't need to use the command line.
- [Jupyter Notebooks](http://jupyter.org/install) - Powerful Python tool hosted as a web app useful for writing and organizing Machine Learning code. Very visually appealing and great for running code snippets.
- [Postman](https://www.getpostman.com/) - REST API testing tool.


## Useful Libraries and Frameworks

Here are a few libraries that might prove to be useful during the competition! If the official library isn't written in your favorite language, try finding wrappers/bindings for it online!

- [Tesseract](https://github.com/tesseract-ocr/)
- [pytesseract](https://pypi.org/project/pytesseract/)
- [Kraken](http://kraken.re/)
- [OpenCV](https://pypi.org/project/opencv-python/)
- [brain.js](https://github.com/BrainJS/brain.js)
- [Keras](https://keras.io/)
- [PyTorch](https://pytorch.org/)
- [scikit-learn](http://scikit-learn.org/stable/)
- [Tensorflow](https://www.tensorflow.org/tutorials/)
- [Tensorflow JS](https://js.tensorflow.org/)
- [Numpy](http://www.numpy.org/)


## Informative Videos

- [What is OCR?](https://www.youtube.com/watch?v=ZNrteLp_SvY) - OCR isn't just about scanning documents and digitizing old books. Explaining how it can work in a practical setting is Professor Steve Simske.
- [Benford's Law](https://www.youtube.com/watch?v=XXjlR2OK1kM) - Why so many cells begin with the number 1! 


## Useful Plug and Play APIs

Here are a few APIs that might prove to be useful during the competition! These are a software engineer's best friend. These will do the heavy lifting for you, so you can focus on working on your product.

- [Google Cloud Vision](https://cloud.google.com/vision/docs/ocr)
- [Amazon Textract](https://aws.amazon.com/textract/)
- [Microsoft Azure Cognitive Services](https://azure.microsoft.com/en-ca/services/cognitive-services/directory/vision/)


## Data Set Resources

Need more data? Here are some resources you can use to quickly find data sets!

- [Stanford House Numbers Dataset](http://ufldl.stanford.edu/housenumbers/)
- [Kaggle Datasets](https://www.kaggle.com/datasets)
- [Google Data Set Search](https://toolbox.google.com/datasetsearch)

If you want to avoid training your own models, you can also find pretrained models online!

- [Model Depot](https://modeldepot.io/)
- [Model Zoo](https://modelzoo.co/)


## Cloud Computing

Cloud computing is especially useful when you need to do heavy computations (read: Machine Learning). There are a few providers. If this is your first time using them, they usually provide a bunch of free credits for students.

- [Amazon Web Services](https://aws.amazon.com/machine-learning/)
- [Google Colab](https://colab.research.google.com/notebooks/welcome.ipynb)
- [Google Cloud Platform](https://cloud.google.com/products/ai/)
- [IBM Watson](https://www.ibm.com/analytics/machine-learning)
- [Microsoft Azure](https://azure.microsoft.com/en-ca/overview/machine-learning/)
