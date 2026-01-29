# Brain-Cancer-Detection-Project
This script is able to sort through various MRIs of brain cancer tumors and classify them into one of four categories (pituitary, meningioma, glioma, healthy). If this script were to be adapted by healthcare systems, it would be able to efficiently cut down the workload of healthcare workers as well as the time it would take to return to patients. I decided to make this project as I am interested in the various applications of machine learning in healthcare and its ability to improve to the health and safety of society. 

![Identified meningioma brain cancer](test.jpg)

## The Algorithm

The data used in this project was taken from https://www.kaggle.com/datasets/rm1000/brain-tumor-mri-scans?select=meningioma

The data was then imported into the development environment where it was then split into three groups, testing, training, and validation. In the training process, the resnet.18 model was used and retrained with the new categories, being glioma, meningioma, pituitary, and healthy. By doing so, the model learns to recognize the distinct features of each form of cancer, and be able to classify the MRI to its associated type. To test the model, the percent accuracy was taken by comparing the amount of photos correctly identified to the total number of images in the dataset. The results have been listed below:

* glioma 39.88%
* pituitary 85.80%
* meningioma 67.88%
* healthy 94.50%

The results prove that the model is fairly accurate in identifying the types of brain cancer. 
## Running this project

1. Install Jetson Inference
2. Download the project repository
3. Change directories into the project respository

To process a folder, follow the steps listed below:
1.  Run the command in the terminal: `./pythonnet.py [FOLDERNAME]`

To process a photo, follow the steps listed below:
1. Run the command in the termainl: `imagenet --model=resnet18.onnx --labels=labels.txt --input_blob=input_0 --output_blob=output_0 [IMAGE NAME] test.jpg`

[View a video explanation here](video link)

