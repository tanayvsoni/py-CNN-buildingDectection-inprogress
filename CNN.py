import os
import torch
import torchvision

from zipfile import ZipFile
from PIL import Image
from torchvision import transforms

def get_data(data_directory):
    data_directory += '/output'
    
    with ZipFile(data_directory+'/output.zip','r') as zip:
        zip.extractall(path = data_directory+'/images')
        
    images = os.listdir(data_directory+'/images')
    
    with open(data_directory+'/image_data.csv') as csvfile:
        cf = csvfile.read().splitlines()
        
        labels = []

        for i in range(1,len(cf)): 
            cf[i] = cf[i].split(',')
            labels.append(cf[i][1])
     
    convert_tensor = transforms.ToTensor()
    dataset = []      
      
    for i in range(len(images)):
        img = Image.open(f'{data_directory}/images/{images[i]}')

        dataset.append([convert_tensor(img), labels[i]])

    tensor_img, label = dataset[0]
    
    print(tensor_img.shape)
    
    return dataset

def main():
    dataset = get_data('./data')

if __name__ == '__main__':
    main()