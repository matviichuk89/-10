import os
files=os.listdir(r"C:\Users\Nazar\OneDrive\Desktop\QUESTIONS")
tiff=open(r"C:\Users\Nazar\OneDrive\Desktop\tiff.txt", "w", encoding="utf-8")
count = 0
for i in files:
    if i.endswith(".png"):
        count += 1
    elif i.endswith((".jpg", ".jpeg")):
        print(i)
    elif i.endswith(".tiff"):
        tiff.write(i)
print("Кількість файлів формату пнг:", count)
