def word_count(phrase):
    dictionary = {};
    for letter in phrase:
        if letter.isalpha() != True:
            if letter.isdigit() != True:
                phrase = phrase.replace(letter, " ");
    word_list = (str.lower(phrase)).split();
    for word in word_list:
        if dictionary.get(word) != None:
            dictionary[word] += 1
        else:
            dictionary[word] = 1;
    return dictionary;
