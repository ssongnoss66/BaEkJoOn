"""2789 유학금지"""

word = input()

for i in ["C", "A", "M", "B", "R", "I", "D", "G", "E"]:
    word = word.replace(i, "")

print(word)

# .strip() / .replace( , )