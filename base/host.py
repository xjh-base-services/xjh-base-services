hostpath = 'C:\\Windows\\System32\\drivers\\etc\\hosts'


def hostcheck():
	"""
	校验当前环境
	:return: 返回：prof（当前是生产环境），stage（当前是预发布环境）
	"""
	file = open(hostpath, 'r', encoding='utf-8')
	filedata = file.read()
	if '121.43.114.158' in filedata:
		return 'prod'
	elif '47.100.131.92' in filedata:
		return 'stage'


def hostup(text=''):
	"""
	修改系统host文件
	:param text: 要修改的数据
	:return: 无
	"""
	try:
		file = open(hostpath, 'w', encoding='utf-8')
		file.write(text)
	except PermissionError:
		print('没有管理员权限')


if __name__ == '__main__':
	hostup('1')
