from torch import nn
import torch
from transformers import BertModel

class BertClassifier(nn.Module):
    def __init__(self, dropout=0.5):

        super(BertClassifier, self).__init__()

        self.bert = BertModel.from_pretrained('bert-base-cased')
        self.dropout = nn.Dropout(dropout)
        self.linear = nn.Linear(768, 2)
        self.relu = nn.ReLU()

    def forward(self, input_id, mask):

        _, pooled_output = self.bert(input_ids= input_id, attention_mask=mask,return_dict=False)
        dropout_output = self.dropout(pooled_output)
        linear_output = self.linear(dropout_output)
        final_layer = self.relu(linear_output)
        return final_layer

def predict(model1, model2,test_sentence,tokenizer):
  # model1: BERT model for first 512 tokens
  # model2: BERT model for last 512 tokens
  device='cuda' if torch.cuda.is_available() else "cpu"
  model1.to(device)
  model2.to(device)
  model1.eval()
  model2.eval()
  processed_sentence_first = tokenizer(test_sentence,padding='max_length', max_length = 512, truncation=True,return_tensors="pt")
  processed_sentence_last = tokenizer(" ".join(test_sentence.split()[-512:]),padding='max_length',max_length=512,truncation=True,return_tensors="pt")
  predict = model1(processed_sentence_first["input_ids"].squeeze(1).to(device), processed_sentence_first["attention_mask"].to(device)) +\
            model2(processed_sentence_last["input_ids"].squeeze(1).to(device), processed_sentence_last["attention_mask"].to(device))
  return predict
