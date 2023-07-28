class Text:
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text

    def brkWords(self, words):
        x = self.text.split()
        y = x.count(words)
        return f"The number of '{words}' is: {y}"
    def mostCommonWords(self):
      textSet = list(set(self.text.split(" ")))
      highest = textSet.pop(0)
      for word in textSet:
        if self.text.count(word) > self.text.count(highest):
          highest = word
      return highest

if __name__ == "__main__":
    mytext = Text('“A good book would sometimes cost as much as a good house.”')
    result = mytext.brkWords("book")
    print(result)
    mytext.mostCommonWords()
    print(mytext)
