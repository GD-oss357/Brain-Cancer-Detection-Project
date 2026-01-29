#!/usr/bin/python3

import jetson_inference
import jetson_utils

import argparse

import os

count = 0

parser = argparse.ArgumentParser()
parser.add_argument("directory", type=str, help="directory of the image to process")
parser.add_argument("--network", type=str, default="googlenet", help="model to use, can be:  googlenet, resnet-18, ect. (see --help for others)")
opt = parser.parse_args()

files= os.listdir(opt.directory)

net = jetson_inference.imageNet(model="resnet18.onnx", labels="labels.txt", input_blob="input_0", output_blob="output_0")

for i in range(len(files)):
    img = jetson_utils.loadImage(os.path.join(opt.directory,files[i]))
    class_idx, confidence = net.Classify(img)
    class_desc = net.GetClassDesc(class_idx)
    if class_desc == opt.directory:
        count += 1

average = (count/len(files))*100

print (opt.directory, average)


