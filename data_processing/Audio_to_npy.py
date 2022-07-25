import numpy as np
import librosa
import os

path = '/Users/yimingxu/wk_space/S2I/data/flowers/Oxford-102/Ocfords_102_audio'
clss_names = os.listdir(path)
save_root = '/Users/yimingxu/wk_space/S2I/data/flowers/Oxford-102/Ocfords_102_audio/audio_npy'
i = 0
for clss_name in sorted(clss_names):
    print(clss_name)
    clss_path = os.path.join(path,clss_name)
    img_names= os.listdir(clss_path)
    for img_name in sorted(img_names):
        print(img_name)
        img_path =  os.path.join(clss_path,img_name)
        audio_names = os.listdir(img_path)
        audio = []
        for audio_name in sorted(audio_names):
            audio_path = os.path.join(img_path,audio_name)
            y,sr = librosa.load(audio_path)
            audio.append(y)
        save_path = save_root + '/'+ clss_name
        
        if not os.path.exists(save_path):
            os.makedirs(save_path)

        save_name = save_path +'/' + img_name + '.npy'
        np.save(save_name,audio)

        print("mel ", i, ' finished')
        i = i+1
        