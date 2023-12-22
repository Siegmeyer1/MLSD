import os
from sklearn.model_selection import train_test_split

X = [i for i in range(1075)]
y = [i for i in range(1075)]

images_home_folder = '/Users/siniavskijand/Documents/study/MLDS/raw_dataset'
labels_home_folder = '/Users/siniavskijand/Documents/study/MLDS/labels'
result_dest_folder = '/Users/siniavskijand/Documents/study/MLDS/datasets/dataset'

images_set = set()
labels_set = set()
folder = os.fsencode(images_home_folder)
for file in os.listdir(folder):
	images_set.add(os.fsdecode(file).split('.')[0])
folder = os.fsencode(labels_home_folder)
for file in os.listdir(folder):
	labels_set.add(os.fsdecode(file))

filenames = list(images_set & labels_set)

filenames_train, filenames_vt = train_test_split(filenames, test_size = 0.2, random_state = 1)
filenames_val, filenames_test = train_test_split(filenames_vt, test_size = 0.5, random_state = 1)

train = set(filenames_train)
validation = set(filenames_val)
test = set(filenames_test)

folder = os.fsencode(labels_home_folder)
for file in os.listdir(folder):
	filename = os.fsdecode(file)
	if filename in train:
		split_group = 'train'
	elif filename in validation:
		split_group = 'validation'
	elif filename in test:
		split_group = 'test'
	else:
		continue
	os.system(f'cp {images_home_folder}/{filename}.jpg {result_dest_folder}/images/{split_group}')
	os.system(f'cp {labels_home_folder}/{filename} {result_dest_folder}/labels/{split_group}/{filename}.txt')




