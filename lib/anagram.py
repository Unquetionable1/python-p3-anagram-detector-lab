# your code goes here!
class Anagram:
    def __init__(self, word):
        self.letters = sorted([letter for letter in word])

    def match(self, words_list):
        matched = []
        for word in words_list:
            if sorted([letter for letter in word]) == self.letters:
                matched.append(word)
        return matched


