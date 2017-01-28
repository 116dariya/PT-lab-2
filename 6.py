s = input()
if 'f' in s:
	i = s.index('f')
	ss = s[i+1:]
	if 'f' in ss:
		j = ss.index('f')+1
		print(j+i)
	else:
		print(-1)
else:
	print(-2)