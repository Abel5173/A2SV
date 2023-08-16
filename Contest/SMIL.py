s = input()
for i in range(len(s)):
    if s[i] == ':' or s[i] == ';':
        if i+1 < len(s) and s[i+1] == ')':
            print(i)
            continue
        elif i+2 < len(s) and s[i+1] == '-' and s[i+2] == ')':
            print(i)
            continue
