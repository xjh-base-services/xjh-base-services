import hashlib


def getMD5(par):
	"""
	:param par: 需要md5加密的字符串
	:return: 加密后的结果
	"""
	h = hashlib.md5()
	h.update(bytes(str(par), encoding='utf-8'))
	return h.hexdigest()


if __name__ == '__main__':
	print(getMD5(1))
