driving = input('請問你有開過車嗎？')
if driving != '有' and driving != '沒有':
	print('請輸入 有/沒有')
	raise SystemExit
	
age = int(input('請問你的年齡是？'))

if driving == '有':
	if age >= 18:
		print('你通過測驗了')
	else:
		print('你還未成年 怎麼開車')
elif driving == '沒有':
	if age >= 18:
		print('你可以考駕照了')
	else:
		print('等18歲之後就可以考駕照了')
else:
	print('請輸入 有/沒有')
