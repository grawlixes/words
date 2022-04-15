B = "⬛️"
G = "🟩"
m = {'B': B, 'G': G}

def toBlocks(s):
    return ''.join(m.get(ch, ch) for ch in s)

f = open("textBank.txt", 'r')
textBankLines = [el.strip() for el in f.readlines()]
f.close()
blockMap = {}
i = 0
while i < len(textBankLines):
    char = textBankLines[i]
    i += 1
    lines = []
    while i < len(textBankLines) and len(textBankLines[i]) != 1:
        lines.append(textBankLines[i])
        i += 1
    blockMap[char] = '\n'.join(lines)

letterSpace = ''.join(B for _ in range(5))
blockMap[' '] = letterSpace

print("This program supports A-Z, 0-9, commas, periods, exclamation marks, and question marks.")
print("You can add your own characters in textBank.txt if you want.")
text = input("Enter your text to translate: ").strip().upper()
ret = []
for ch in text:
    print(toBlocks(blockMap[ch]))
    print(letterSpace)
