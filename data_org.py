
import os
from PIL import Image

def get_photos_buildings():
    data_directory = './data'
    
    with open(data_directory + '/output_zip_info/image_data.csv','r') as csvfile:
        file = csvfile.read().splitlines()
        last_imgID = int(file[-1].split(',')[0][:-4])
        
          
    img_names = os.listdir(data_directory+'/input_image')
    
    for img in img_names:
        last_imgID += 1
        while True:
            try:
                print(f'\nFor image {img} please enter relevent info:')
                country_name = input('Enter name of country present in image: ').lower()
                date = input('Enter date image was taken (DD/MM/YY): ')
                [latitude, longitude] = input('Enter the lat,long coordinates of image: ').split(',')
                num_building = int(input('Enter number of buildings present in image: '))
                break
            except: print('Invalid input. Try again')
            
        with open(data_directory + '/output_zip_info/image_data.csv','a') as csvfile:
            csvfile.write(f'{last_imgID}.png,f{num_building},{country_name},{date},{latitude},{longitude}\n')
            
def main():
    get_photos_buildings()

if __name__ == '__main__':
    main()
    
    