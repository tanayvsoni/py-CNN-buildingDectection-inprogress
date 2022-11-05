import os
import torch
import torchvision
import matplotlib


from zipfile import ZipFile
from PIL import Image

from torchvision import transforms
from torch.utils.data import random_split
from torch.utils.data.dataloader import DataLoader
from torchvision.utils import make_grid

from matplotlib import pyplot as plt

def get_data(data_directory):
    """Gets image data from zip file and stores it with the associated label

    Args:
        data_directory (string): location of data directory

    Returns:
        [tensor,string]: image tensor with it's associated label value
    """
    data_directory += '/output'
    
    # Checks if there is any need to extract zip file
    if os.listdir(data_directory+'/images') == []:  
        with ZipFile(data_directory+'/output.zip','r') as zip:
            zip.extractall(path = data_directory+'/images')
           
    images = os.listdir(data_directory+'/images')
    
    # Gets labels (amount of buildings) from the csv file and stores them in a list    
    with open(data_directory+'/image_data.csv') as csvfile:
        cf = csvfile.read().splitlines()
        
        labels = []

        for i in range(1,len(cf)): 
            cf[i] = cf[i].split(',')
            labels.append(cf[i][1])

    # Converts all the images to PyTorch tensors and stores the tensor img
    # and the label assoicated with it in a list
    dataset = []      

    for i in range(len(images)):
        img = Image.open(f'{data_directory}/images/{images[i]}')

        dataset.append([transforms.ToTensor(img)[:3,:,:], labels[i]])  # Removes alpha channel to make total channel 3
    
    return dataset

def view_img(img,label):
    """Allows you to view a image from a dataset

    Args:
        img (tensor): tensor for the pixels in image
        label (string): label associated with image
    """
    
    print(f'Label: {label}')
    plt.imshow(img.permute(1,2,0))
    plt.show()

def split_data(test_size,seed,dataset):
    """Splits a dataset up to training images and testing images

    Args:
        test_size (int): Size of test image set
        seed (int): seed to set the pytorch's random number gen to
        dataset (tensor): the dataset you want to split

    Returns:
        tensor, tensor: 2 new tensor datasets for training and testing
    """
    torch.manual_seed(seed)
    train_size = len(dataset) - test_size
    
    train_ds, test_ds = random_split(dataset, [train_size, test_size])
    
    return train_ds,test_ds

def show_batch(dl):
    for images, labels in dl:
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.set_xticks([]); ax.set_yticks([])
        ax.imshow(make_grid(images, nrow=16).permute(1, 2, 0))
        plt.show()
        break

def main():
    dataset = get_data('./data')
    
    train_ds,test_ds = split_data(1000,69,dataset)
    
    print(len(train_ds), len(test_ds))
    batch_size = 128
    
    train_dl = DataLoader(train_ds, batch_size, shuffle=True, num_workers=4, pin_memory=True)
    val_dl = DataLoader(test_ds, batch_size*2, num_workers=4, pin_memory=True)
    
    show_batch(train_dl)
    

if __name__ == '__main__':
    main()