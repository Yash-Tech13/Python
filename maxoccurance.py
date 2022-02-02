x = input("Enter the string: ")

freq = [0] * 26

for i in x:
    freq[ord(i) - 97] += 1

y = freq.index(max(freq))
y += 97

print(chr(y))
