import transformers
from transformers import BertTokenizer, TFBertForSequenceClassification
from transformers import InputExample, InputFeatures
import tensorflow as tf
import pandas as pd

model = TFBertForSequenceClassification.from_pretrained('bert-base-uncased')
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

# model.summary()
# Now that we have our model, let us create our input sequences from the IMDB reviews dataset.
# IMDB reviews dataset is  a large movie review dataset collected and prepared by Andrew.

URL = "https://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz"

dataset = tf.keras.utils.get_file(fname="aclImdb_v1.tar.gz", 
                                  origin=URL,
                                  untar=True,
                                  cache_dir='.',
                                  cache_subdir='')
# Removing the unlabeled reviews

import os
import shutil
import numpy as np

# Create main directory path ("/aclImdb")
main_dir = os.path.join(os.path.dirname(dataset), 'aclImdb')

# Create sub directory path ("/aclImdb/train")
train_dir = os.path.join(main_dir, 'train')

# Remove unsup folder since this is a supervised learning task
remove_dir = os.path.join(train_dir, 'unsup')
shutil.rmtree(remove_dir)

# View the final train folder
print(os.listdir(train_dir))

# Train and Test Split 
train = tf.keras.preprocessing.text_dataset_from_directory('aclImdb/train',\
    batch_size=30000,validation_split=0.2, subset='training', seed = 123)
test = tf.keras.preprocessing.text_dataset_from_directory('aclImdb/train',
    batch_size=30000, validation_split=0.2, subset='validation', seed = 123)

for i in train.take(1):
  train_feat = i[0].numpy()
  train_lab = i[1].numpy()

train = pd.DataFrame([train_feat, train_lab]).T
train.columns = ['DATA_COLUMN', 'LABEL_COLUMN']
train['DATA_COLUMN'] = train['DATA_COLUMN'].str.decode("utf-8")
print(train.head())
