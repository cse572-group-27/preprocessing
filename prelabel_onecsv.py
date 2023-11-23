import argparse
import os
from model import predict, BertClassifier
from transformers import BertTokenizer
import torch
import re
parser = argparse.ArgumentParser("Prelabel Configurations")
parser.add_argument("-ifp","--input_file_path",help="Folder contain segments")
parser.add_argument("-ofp","--output_file_path", default="prelabel.csv",help="Folder to output segment with prediction")
args = parser.parse_args()
input_folder = args.input_file_path
output_path = args.output_file_path
# os.makedirs(output_folder,exist_ok=True)

tokenizer = BertTokenizer.from_pretrained('bert-base-cased')
model1 = BertClassifier()
model2 = BertClassifier()
model1.load_state_dict(torch.load("first512_updated.pth"))
model2.load_state_dict(torch.load("last512_updated.pth"))

with open(output_path,"w") as fw:
    fw.write("file_path,label,text\n")
    for segment_file in os.listdir(input_folder):
        if segment_file.split(".")[-1] != 'txt':
            continue
        outfile_name = segment_file.replace("segment","prelabel").replace("txt","csv")
        input_file = os.path.join(input_folder,segment_file)
        segments = open(input_file,"r").read().splitlines()
        
        for segment in segments:
            # because in sponsor block there are no commas, period, so i just remove it
            seg= re.sub(r'[^a-zA-Z0-9]', ' ', segment)
            ad_pred = predict(model1,model2,seg,tokenizer)
            fw.write(input_file+",")
            if ad_pred.argmax(dim=1) == 1:
                fw.write("sponsor,")
            else:
                fw.write("non-sponsor,")
            fw.write(segment+"\n")
