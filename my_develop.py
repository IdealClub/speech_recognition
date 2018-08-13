import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
from collections import Counter
from python_speech_features import mfcc
import tensorflow as tf



def dict_test():
	all_word = []
	label = []
	# python字典生成方法，没有语音，只生成汉字对应了序号
	label = ['hello','hello','hello','hi','hi','hi','you', 'you']
	all_word += [word for word in label]
	counter = Counter(all_word)
	words = sorted(counter)
	words_size = len(words)
	word_num_map = dict(zip(words, range(words_size)))
	print('all words i use :\n',all_word)
	print('\nafter counter:\n',counter)
	print('\nafter sort:\n',words)
	print('\nthe words size: ',words_size)
	print('\nthe words num map:\n',word_num_map)


def readwav(audio_filename, n_input=26):
	# 读取音频文件
	fs, audio = wav.read(audio_filename)
    # 提取mfcc数值
	orig_inputs = mfcc(audio, samplerate=fs, numcep=26)
#	for i in range(orig_inputs.shape[0]):
#		plt.plot(orig_inputs[i])
#		plt.pause(0.01)
#		plt.close()

def train(loop):
	section = '\n{0:=^40}\n'
	print(section.format('开始训练'))

def minimum(a,b):
	y = tf.minimum(a,b)
	print(y)



def main():
	minimum(13,15)
	

if __name__ == '__main__':
	main()