names = input("What's your name? ")

nouns = ['jingle', 'ball', 'cat', 'dog', 'elephant',
         'fish', 'goat', 'house', 'sneaker', 'jackal',
         'king', 'llama', 'monkey', 'nurse', 'mouse',
         'pie', 'queen', 'robot', 'snake', 'tofu',
         'unicorn', 'cat', 'wumpus', 'x-ray', 'yak',
         'mouth']

verbs = ['ate', 'bit', 'caught', 'dropped', 'explained',
         'fed', 'grabbed', 'hacked', 'inked', 'jumped',
         'knitted', 'loved', 'made', 'nosed', 'oiled',
         'puffed', 'quit', 'rushed', 'stung', 'trapped',
         'uplifted', 'valued', 'wanted']

templates = [
        '{{name}}! I found a {{noun}} in my {{noun}}!',
        '{{name}}, the {{noun}} {{verb}} the {{noun}}.',
        '{{name}}, If you {{verb}} the {{noun}} ',
        '{{name}}, the {{noun}} will get you.',
        "{{name}}, Let's go: the {{noun}} is {{verb}}.",
        '{{name}}, Colorless green {{noun}}s {{verb}} furiously.']