word = input("Write a word!")
reversed_word = ""
for i in range(1, len(word)+1):
  reversed_word += word[-i]
print(reversed_word)
