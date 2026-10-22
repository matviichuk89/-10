import string
f=open(r"C:\Users\Nazar\OneDrive\Desktop\Lab10text.txt", "r", encoding="utf-8")
a=open(r"C:\Users\Nazar\OneDrive\Desktop\digit.txt", "w", encoding="utf-8")
b=open(r"C:\Users\Nazar\OneDrive\Desktop\symbols.txt", "w", encoding="utf-8")
text=f.read()
for i in text:
    if i.isdigit():
        a.write(i)
    elif i.isalpha():
        b.write(i)
    elif i not in string.punctuation:
        b.write(i)
f.close()
a.close()
b.close()