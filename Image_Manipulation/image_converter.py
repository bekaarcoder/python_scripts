import sys
import os
from PIL import Image

# grab the arguments from the command
image_folder = sys.argv[1]
output_folder = sys.argv[2]

print(image_folder, output_folder)

# check if the output folder exists
if os.path.exists(output_folder):
  print(f'{output_folder} exists')
else:
  print(f'Creating {output_folder} folder...')
  os.makedirs(output_folder)

# convert the images
for filename in os.listdir(image_folder):
  img = Image.open(f'{image_folder}{filename}')
  clean_name = os.path.splitext(filename)[0]
  img.save(f'{output_folder}{clean_name}.png', 'png')
  print(f"{filename} converted.")