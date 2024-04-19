import translate_phrase_func


back_dict = {v: k for k, v in translate_phrase_func.letters_to_morse.items()}


def back_translate(phrase):
    phrase = phrase.split('       ')
    answer = ''
    for word in phrase:
        word = word.strip().split('  ')
        for char in word:
            answer += back_dict[char]
        answer += ' '
    return answer
