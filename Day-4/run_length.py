s = input()

if s:
    encoded = []
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            encoded.append(f"{count}{s[i - 1]}")
            count = 1
    
    encoded.append(f"{count}{s[-1]}")
    
    print("".join(encoded))