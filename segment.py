import argparse
from ast import arg
from nltk.tokenize import TextTilingTokenizer
from argparse import ArgumentParser
import os

parser = ArgumentParser("textiling arguments")
parser.add_argument("-ifp","--input-file-path",help="Path to folder contains txt files. The path should contain no spaces.")
parser.add_argument("-ofp","--output-file-path",help="Path to folder contains output.")
args = parser.parse_args()
input_folder = args.input_file_path
output_folder = args.output_file_path
os.makedirs(output_folder,exist_ok=True)
tokenizer = TextTilingTokenizer()
for filename in os.listdir(input_folder):
    #only allows txt files
    if filename.split(".")[-1] != "txt":
        continue
    input_path = os.path.join(input_folder,filename)
    output_path = os.path.join(output_folder,"segment_"+filename)
    text = open(input_path,"r").read()
    text = text.replace(".",".\n\n") #make paragraphs
    tokens = tokenizer.tokenize(text)
    with open(output_path,"w") as fw:
        for token in tokens:
            paragraph = token.replace("\n"," ")
            fw.write(paragraph+"\n")
