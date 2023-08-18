text = input()
text1 = text.split()
gol = ['a', 'e', 'i', 'o', 'u', 'A', 'E','I','O','U']

for w in text1:
    index = text1.index(w)
    for i in gol:
        if i in w:
            new_w = w.replace(i, '#')
            text1[index] = new_w
print(text1)
print(" ".join(map(str,text1)))