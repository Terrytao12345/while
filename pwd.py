#密碼重試程式

'''
default_pwd = 'a123456'
pwd = input('Please enter password :')

if pwd != 'a123456' :
	retry = 2
	retry = int(retry)
	while retry > 0 :
		print('密碼錯誤,請再重新輸入,剩餘', retry, '次機會')
		pwd = input('Please enter password :')
		retry = retry -1
		if retry == 0 :
			print('Account block')
			break
else :
	print('login success')
'''

pwd = "aaa"
retry = 3

while True :
	user_pwd = input()
	retry = retry - 1
	if user_pwd == pwd :
		print('Login success')
		break
	else :
		retry = retry - 1
		print('Please retry again', 'left:', retry, 'times' )
		if retry == 0 :
			break