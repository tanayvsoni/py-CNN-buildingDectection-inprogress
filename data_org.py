import os
import zipfile

def org_files(data_directory):
    """Prompts user to input image data and moves said image into zip file and stores
    relevent data into image_data.csv file.

    Args:
        data_directory (string): location of data
    """
    
    # Get last image ID that was used from csv file
    with open(f'{data_directory}/output/image_data.csv','r') as csvfile:
        file = csvfile.read().splitlines()
        last_imgID = int(file[-1].split(',')[0][:-4])
        
    # Get all input images (should be only 1 image ideally)      
    img_names = os.listdir(f'{data_directory}/input')
    
    for img in img_names:
        # Create new image name by adding 1 to previous ID number
        last_imgID += 1
        new_name = f'{last_imgID}.png'
        
        # Rename Image
        os.rename(f'{data_directory}/input/{img}',f'{data_directory}/input/{new_name}')
    
        while True:
            # Get relevent data
            print(f'\nFor image {img} please enter relevent info:\n')
                
            country_name = input('Enter name of country present in image: ').lower()
            date = input('Enter date image was taken (DD/MM/YYYY): ')
            [latitude, longitude] = input('Enter the coordinates of image (lat,long): ').split(',')
            num_building = input('Enter number of buildings present in image: ')
            comments = input('Any extra comments? Leave blank if none: ')
                
            if input('\nWould you like to edit inputs (y/n): ').lower() == 'n': break
        
        # Write data input csv file    
        with open(f'{data_directory}/output/image_data.csv','a') as csvfile:
            csvfile.write(f'{new_name},{num_building},{country_name},{date},{latitude},{longitude},{comments}\n')
        
        # Copy image into zip file
        with zipfile.ZipFile(f'{data_directory}/output/output.zip','a') as zipf:
            zipf.write(f'{data_directory}/input/{new_name}',f'{new_name}')
        
        # Remove image from input folder    
        os.remove(f'{data_directory}/input/{new_name}')
                       
if __name__ == '__main__':
    while True:
        org_files('./data')
        if input('\nAll files have been stored, would you like to input again (y/n): ').lower() == 'n': break
    
    