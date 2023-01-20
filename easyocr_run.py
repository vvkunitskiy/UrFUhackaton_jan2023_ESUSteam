import easyocr

import os
import os.path
from pathlib import Path

input_directory = input('Input directory is:\n')
if not os.path.exists(input_directory):
	print('Wrong path!')
	exit()
if input_directory != '' and input_directory[-1] != '/':
	input_directory += '/'
 
output_directory = input('Output directory is:\n')
if not os.path.exists(output_directory):
	print('Wrong path!')
	exit()
if output_directory != '' and output_directory[-1] != '/':
	output_directory += '/'
	
#print(easyocr.__all__)

for root, dirs, files in os.walk(input_directory):  
	for filename in files: 
		
		file_path = root+filename
		record_to_file = ''
		file_path_to_save = output_directory+filename
		
		reader = easyocr.Reader(["en"])
		try:
			image_predict = reader.readtext(file_path)
		except:
			print(file_path,'is WRONG file!')
			continue
			
		
		try:
			mediafile_extension = Path(file_path_to_save).suffixes[-1]
		except:
			mediafile_extension = ''
			
		file_path_to_save = file_path_to_save.removesuffix(mediafile_extension)
			
		for line in image_predict:
			coordinates = str(line[0])
			text_box = line[1]

			coordinates = coordinates.replace('[','')
			coordinates = coordinates.replace(' ','')
			coordinates = coordinates.replace(']','')

			record_to_file += coordinates + ',' + text_box + '\n'
		
		recording_file = open(file_path_to_save+'-1.txt', 'w+')
		recording_file.write(record_to_file)
		recording_file.close()
