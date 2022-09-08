import shutil

src_path = '/content/drive/MyDrive/Kyopro/kyopro/'
dst_path = '/content/drive/MyDrive/Competitions/DFL/output/'
for i in range(4):
    file = f'validation_data_3c993bd2_{i+1}.zip'
    print(f'{src_path}/{file} -> {dst_path}/{file}')
    shutil.copy(f'{src_path}/{file}', f'{dst_path}/{file}')

print('done')