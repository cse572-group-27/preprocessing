import argparse
import os
from model import predict, BertClassifier
from transformers import BertTokenizer
import torch
import re
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
    outfile_name = segment_file.replace("segment","prelabel").replace("txt","csv")
    input_file = os.path.join(input_folder,segment_file)
    output_file = os.path.join(output_folder,outfile_name)
    segments = open(input_file,"r").read().splitlines()
    with open(output_file,"w") as fw:
        fw.write("label,text\n")
        for segment in segments:
            # because in sponsor block there are no commas, period, so i just remove it
            seg= re.sub(r'[^a-zA-Z0-9]', ' ', segment)
            
            ad_pred = predict(model1,model2,seg,tokenizer)
            if ad_pred.argmax(dim=1) == 1:
                fw.write("sponsor,")
            else:
                fw.write("non-sponsor,")
            fw.write(segment+"\n")
