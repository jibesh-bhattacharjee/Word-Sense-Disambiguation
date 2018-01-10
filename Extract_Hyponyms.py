from nltk.corpus import wordnet

word = input("Enter a word: ")
 
syns = wordnet.synsets(word)
print("The senses are as follows:")
print()

for sense in syns:
    print(sense.name(), sense.examples())



#print(syns)
# --WORKING FINE 
print()
#print(syns[0].name())
#print(syns[0].lemmas()) --works well

#Now to select any one sense from the given senses
selectedSense = int(input("Enter the index of the sense you want: "))


hn_word = wordnet.synset(syns[selectedSense].name())
hyponyms = hn_word.hyponyms()

print("The set of hyponyms is as follows: ")
print()
print(hyponyms)
print()
print("Of which the hyponyms are: ")
print()

for word in hyponyms:
    print(word.lemmas()[0].name())


