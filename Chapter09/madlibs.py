with open("text", newline="") as file:
    with open('text2', 'w') as f:
        for line in file:
            words = line.split()
            for word in words:
                if word == 'ADJECTIVE':
                    adjective = input("Enter adjective: ")
                    f.write(adjective)
                elif word == 'NOUN':
                    noun = input("Enter noun: ")
                    f.write(noun)
                elif 'VERB' in word:
                    verb = input("Enter verb: ")
                    f.write(verb)
                elif 'ADVERB' in word:
                    adverb = input("Enter adverb: ")
                    f.write(adverb) 
                else:
                    f.write(word + ' ')
                    continue

                if word[-1] == '.':
                        f.write('.')
                f.write(' ')
                

with open('text2') as f:
    data = f.read()
    print(data)


