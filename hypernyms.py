from nltk.corpus import wordnet as wn

word1 = 'vibration'
word2 = 'marriage'
delimeter = '->'

synset1 = wn.synsets(word1)
synset2 = wn.synsets(word2)
extracted_hypernyms = []
extracted_common_hypernyms = []

for synonym in synset1:
    hypernyms = synonym.hypernyms()
    for hypernym in hypernyms:
        hypernym_name = hypernym.name().split('.')[0]
        if hypernym_name not in extracted_hypernyms:
            extracted_hypernyms.append(hypernym_name)

for syn1 in synset1:
    for syn2 in synset2:
        common_hypernym_set = syn1.lowest_common_hypernyms(syn2)
        for common_hypernym in common_hypernym_set:
            common_hypernym_name = common_hypernym.name().split('.')[0]
            if common_hypernym_name not in extracted_common_hypernyms:
                extracted_common_hypernyms.append(common_hypernym_name)

print('hypernym of ', word1,': ', delimeter.join(extracted_hypernyms))
print('common hypernyms of ', word1,'-', word2,': ', delimeter.join(extracted_common_hypernyms))

