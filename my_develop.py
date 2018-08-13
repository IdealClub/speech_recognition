from collections import Counter
import scipy.io.wavfile as wav
from python_speech_features import mfcc
import matplotlib.pyplot as plt

def dict_test():
	all_word = []
	label = []
	# python字典生成方法，没有语音，只有汉字对应了序号
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
    # 获取mfcc数值
	orig_inputs = mfcc(audio, samplerate=fs, numcep=26)
	plt.plot(orig_inputs)
	plt.show()


def main():
	readwav('./wav/test.wav')
	

if __name__ == '__main__':
	main()