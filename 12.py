s = '5' * 247
while '222' in s or '555' in s:
    if '222' in s:
        s = s.replace('222', '5')
    else:
        s = s.replace('555', '2')
print(s)
