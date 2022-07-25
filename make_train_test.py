import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
import os

x_test = []
x_train = []
all_file = []
file_ads = './../data/Flickr8k/audio/wavs'

img_names = os.listdir(file_ads)
i = 0
for img_name in sorted(img_names):
    img_name = img_name.split('.')[0]
    img_path = os.path.join(file_ads,img_name) 
    #all_file.append(img_name)
    if img_name[-2:] == '_4':
        #print(img_name[:-2])
        x_test.append(img_name)
    else:
        #print(img_name[:-2])
        x_train.append(img_name)

#x_train, x_test = train_test_split(all_file)


#train_df = pd.DataFrame(x_train)
#test_df = pd.DataFrame(x_test)
print(len(x_train), len(x_test))

with open('./../data/Flickr8k/train/filenames.pickle', 'wb') as f:
    pickle.dump(x_train, f)

with open('./../data/Flickr8k/test/filenames.pickle', 'wb') as f:
    pickle.dump(x_test, f)