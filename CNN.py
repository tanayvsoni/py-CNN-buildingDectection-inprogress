import os
import torch
import torchvision
import matplotlib


from zipfile import ZipFile
from PIL import Image
from torchvision import transforms
from torch.utils.data import random_split
from matplotlib import pyplot as plt

def get_data(data_directory):
    data_directory += '/output'
    
    # Checks if there is any need to extract zip file
    if os.listdir(data_directory+'/images') == []:  
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

        dataset.append([convert_tensor(img)[:3,:,:], labels[i]])
    
    return dataset

def view_example(img,label):
    print(f'Label: {label}')
    plt.imshow(img.permute(1,2,0))
    plt.show()

def split_data(test_size,random_seed,dataset):
    
    torch.manual_seed(random_seed)
    train_size = len(dataset) - test_size
    
    train_ds, test_ds = random_split(dataset, [train_size, test_size])
    
    return train_ds,test_ds

def main():
    dataset = get_data('./data')
    
    train_ds,test_ds = split_data(1000,69,dataset)
    
    print(len(train_ds), len(test_ds))
    

if __name__ == '__main__':
    main()