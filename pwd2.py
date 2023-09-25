#密碼重試程式

d_pwd = 'aaa'
retry = 3

while retry > 0 : 
	pwd = input('Please enter password :')
	if pwd == d_pwd :
		print('登入成功')
		break
	else :
		retry = retry - 1
		print('密碼錯誤')
		if retry > 0 :
			print('剩餘', retry, '次機會')
		else :
			print('無嘗試機會')



