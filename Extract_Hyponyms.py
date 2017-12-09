from nltk.corpus import wordnet

word = input("Enter a word: ")
 
syns = wordnet.synsets(word)

#print(syns)
# --WORKING FINE 
print()
#print(syns[0].name())
#print(syns[0].lemmas()) --works well

hn_word = wordnet.synset(syns[0].name())
hyponyms = hn_word.hyponyms()

print("The set of hyponyms is as follows: ")
print()
print(hyponyms)
print()
print("Of which the hyponyms are: ")
print()

for word in hyponyms:
    print(word.lemmas()[0].name())


