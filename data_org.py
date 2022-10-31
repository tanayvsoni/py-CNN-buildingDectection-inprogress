import os
import zipfile

def org_files():
    data_directory = './data'
    
    with open(f'{data_directory}/output_zip_info/image_data.csv','r') as csvfile:
        file = csvfile.read().splitlines()
        last_imgID = int(file[-1].split(',')[0][:-4])
        
          
    img_names = os.listdir(f'{data_directory}/input_image')
    
    for img in img_names:
        last_imgID += 1
        new_name = f'{last_imgID}.png'
        os.rename(f'{data_directory}/input_image/{img}',f'{data_directory}/input_image/{new_name}')
    
        while True:
            try:
                print(f'\nFor image {img} please enter relevent info:\n')
                
                country_name = input('Enter name of country present in image: ').lower()
                date = input('Enter date image was taken (DD/MM/YY): ')
                [latitude, longitude] = input('Enter the coordinates of image (lat,long): ').split(',')
                num_building = input('Enter number of buildings present in image: ')
                
                if input('\nWould you like to edit inputs (y/n): ').lower() == 'y': raise
                break
            
            except: pass
            
        with open(f'{data_directory}/output_zip_info/image_data.csv','a') as csvfile:
            csvfile.write(f'{new_name},{num_building},{country_name},{date},{latitude},{longitude}\n')
        
        with zipfile.ZipFile(f'{data_directory}/output_zip_info/output.zip','a') as zipf:
            zipf.write(f'{data_directory}/input_image/{new_name}',f'{new_name}')
            
        os.remove(f'{data_directory}/input_image/{new_name}')
                       
def main():
    while True:
        org_files()
        if input('\nAll files have been stored, would you like to input again (y/n): ').lower() == 'n': break

if __name__ == '__main__':
    main()
    
    