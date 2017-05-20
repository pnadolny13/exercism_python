def is_pangram(x):
    x = str.lower(x);
    sentence = set();
    count = 0;
    for i in x:
        sentence.update(x[count])
        count = count +1;
    import string
    alphabet = set(string.ascii_lowercase)
    #print (alphabet);
    #print (sentence);
    for i in alphabet:
          if i not in sentence:
              return False;
              break;
    return True;
Contact GitHub API Training Shop Blog About
© 2017 GitHub, Inc. Terms Privacy 
