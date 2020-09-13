password = 'a123456'
x = 3 #可輸入次數
while x > 0:
	answer = input('請輸入密碼: ')
	if answer == password:
		print('登入成功！')
		break
	else:
		x = x - 1
		if x > 0:
			print('密碼錯誤,還有', x, '次機會')
		else:
			print('帳號已鎖定')
