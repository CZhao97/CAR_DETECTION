import glob

path = '/Users/isaaczhang/desktop/darknet/'

def generate_train_and_trst(image_path, txt_file):
	with open(txt_file, 'w') as tf:
		for jpg_file in glob.glob(image_path + '*.jpg'):
			tf.write(jpg_file + '\n')


generate_train_and_trst(path + 'train/', path + 'train.txt')
generate_train_and_trst(path + 'test/', path + 'test.txt')