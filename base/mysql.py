import pymysql

jxxt_path = {
	'host': '192.168.1.247',
	'port': 20086,
	'user': 'wangbizhou',
	'password': '1miwbzh'
}


def select(sql):
	conn = pymysql.Connect(
		host='192.168.1.247',
		port=20086,
		user='wangbizhou',
		password='1miwbzh'
	)

	cursor = conn.cursor()
	cursor.execute(sql)
	datas = cursor.fetchall()
	cursor.close()
	conn.close()

	data_dict = []
	for field in cursor.description:
		data_dict.append(field[0])

	end = []

	for data in datas:
		k = {}
		for i, j in zip(data_dict, data):
			k[i] = j
		end.append(k)
	print(end)
	return end


if __name__ == '__main__':
	jxxtsql('')
