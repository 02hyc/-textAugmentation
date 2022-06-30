file = open('source.txt', 'r', encoding="utf-8")
writeFile = open('dest.txt', 'a', encoding="utf-8")
text = file.readline()
while text:
    if text != "\n" and text != "\r" and text != "\r\n":
        sentence = text.split("。")
        for content in sentence:
            writeFile.write(content)
            writeFile.write('\n')
    text = file.readline()