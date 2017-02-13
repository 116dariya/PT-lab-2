s = input()
i = s.index('h')
ss = s[i+1:][::-1]
ii = ss.index('h')
ii = len(s) - ii - 1
sss = s[i+1:ii]
print(s[:i+1] + sss[::-1] + s[ii:])
