import os


def get_urls(page):
	urls = []

	url = "https://www.bilibili.com/video/av17174348/?p={0}".format(page)

	tmp = os.popen('youtube-dl {0}'.format(url)).readlines()

	print(tmp)


def do_moved():
	moved = os.popen('move *.flv ./completed').readlines()
	print(moved[-1])


def get_inputtxt(page):
	files = os.listdir("./")

	with open("input{0}.txt".format(page), 'w') as f:
		for file in files:
			if "flv" in file:
				f.write("file '{0}'".format(file))




get_inputtxt(1)

# for i in range(1, 80):
# 	url = "https://www.bilibili.com/video/av17174348/?p={0}".format(i)
# 	urls.append(url)



# for url in urls:
	

# 	print(url)
