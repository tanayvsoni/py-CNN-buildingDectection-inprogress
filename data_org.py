
import os
import zipfile

def org_files():
    data_directory = './data'
    
    with open(data_directory + '/output_zip_info/image_data.csv','r') as csvfile:
        file = csvfile.read().splitlines()
        last_imgID = int(file[-1].split(',')[0][:-4])
        
          
    img_names = os.listdir(data_directory+'/input_image')
    
    for img in img_names:
        last_imgID += 1
        new_name = f'{last_imgID}.png'
        os.rename(data_directory+f'/input_image/{img}',data_directory+f'/input_image/{new_name}')
    
        while True:
            try:
                print(f'\nFor image {img} please enter relevent info:')
                country_name = input('Enter name of country present in image: ').lower()
                date = input('Enter date image was taken (DD/MM/YY): ')
                [latitude, longitude] = input('Enter the lat,long coordinates of image: ').split(',')
                num_building = input('Enter number of buildings present in image: ')
                break
            except: print('Invalid input. Try again')
            
        with open(data_directory + '/output_zip_info/image_data.csv','a') as csvfile:
            csvfile.write(f'{new_name},{num_building},{country_name},{date},{latitude},{longitude}\n')
        
        with zipfile.ZipFile(data_directory + '/output_zip_info/output.zip','a') as zipf:
            zipf.write(data_directory+f'/input_image/{new_name}',f'{new_name}')

        os.remove(data_directory+f'/input_image/{new_name}')

        
            
def main():
    org_files()

if __name__ == '__main__':
    main()
    
    