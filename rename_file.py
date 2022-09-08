import os
import glob
import re

path = f'{OUTPUT_PATH}'
files = glob.glob(f'{path}/*')
prefix = 'validation_data_3c993bd2'

for file in files:
    if (prefix in file) and (not os.path.isdir(file)):
        name = file.split('-')[-1].split('.')[0]
        name = re.sub('0','',name)
        print(name)
        filepath = os.path.dirname(file)
        dst_name = f'{filepath}/validation_data_3c993bd2_{name}.zip'
        print(f'{file} -> {dst_name}')
        os.rename(file, dst_name)