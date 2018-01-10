from nltk.corpus import wordnet as wn

word = input("Enter a word: ")
syns = wn.synsets(word)

for sense in syns:
    file = open('{}.txt'.format(sense.name()) , "w")
    lemmaList = sense.lemmas()
    definition = sense.definition()
    examples = sense.examples()
    word = wn.synset(sense.name())
    hyponyms = word.hyponyms()
    ##Printing Lemmas
    file.write("Lemmas:\t")
    for lemma in lemmaList:
        file.write(lemma.name())
        file.write(" ")
    file.write("\n\n")
    ##Printing Definition
    file.write("Definition: ")
    file.write(definition)
    file.write("\n\n")
    ##Printing Examples
    file.write("Examples: ")
    for ex in examples:
        file.write(ex)
        file.write(". ")
    file.write("\n\n")
    ##Printing Hyponyms
    file.write("Hyponyms:\n\n")
    for hynms in hyponyms:
        file.write(hynms.lemmas()[0].name())
        file.write(" - ")
        file.write(hynms.definition())
        file.write("\n\n")
    file.write("\n\n")
    
    file.close()
    



    
