from main import Translation, Judge

file = open("dest.txt", 'r', encoding="utf-8")
fileWrite = open('result.txt', 'a', encoding="utf-8")
text = file.readline()
while text:
    if text != "\n" and text != "\r" and text != "\r\n":
        result = Translation.translate(text)
        utiResult = Translation.translate(result)
        judge = Judge.get_word_vector(text, utiResult)
        fileWrite.write(text)
        fileWrite.write(utiResult)
        fileWrite.write("\n")
        fileWrite.write(str(judge))
        fileWrite.write("\n")
    text = file.readline()
