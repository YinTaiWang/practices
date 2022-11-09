def pig_latin(words):
    words = words.lower().split()
    output = []
    for word in words:
        if word[0] in 'aeiou':
            output.append(f'{word}way')
        else:
            output.append(f'{word[1:]}{word[0]}ay')
    return ' '.join(output)

def main():
    user_input = input('Please insert a vocabulary or a sentence: ')
    output = pig_latin(user_input)
    print(output)

main()