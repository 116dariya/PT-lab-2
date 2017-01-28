s = input()
i = s.index('h')
ss = s[i+1:][::-1]
ii = ss.index('h')
ii = len(s) - ii - 1
print(s[:i] + s[ii+1:])
 