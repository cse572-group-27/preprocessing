import argparse
import os
from model import predict, BertClassifier
from transformers import BertTokenizer
import torch
parser = argparse.ArgumentParser("Prelabel Configurations")
parser.add_argument("-ifp","--input_file_path",help="Folder contain segments")
parser.add_argument("-ofp","--output_file_path",help="Folder to output segment with prediction")
args = parser.parse_args()
input_folder = args.input_file_path
output_folder = args.output_file_path
os.makedirs(output_folder,exist_ok=True)

tokenizer = BertTokenizer.from_pretrained('bert-base-cased')
model1 = BertClassifier()
model2 = BertClassifier()
model1.load_state_dict(torch.load("first512_updated.pth"))
model2.load_state_dict(torch.load("last512_updated.pth"))

for segment_file in os.listdir(input_folder):
    if segment_file.split(".")[-1] != 'txt':
        continue
    outfile_name = segment_file.replace("segment","prelabel")
    input_file = os.path.join(input_folder,segment_file)
    output_file = os.path.join(output_folder,outfile_name)
    segments = open(input_file,"r").read().splitlines()
    with open(output_file,"w") as fw:
        for segment in segments:
            ad_pred = predict(model1,model2,segment,tokenizer)
            fw.write(ad_pred.__str__())
            fw.write("\n")
            fw.write(segment+"\n"+"\n")
