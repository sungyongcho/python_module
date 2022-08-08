# Put this at the top of your kata01.py file
kata = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmusi Lerdorf',
    'PHP': 'Rasmusi Lerdorf',
    'aaa': 'Rasmusi Lerdorf',
    'bbb': 'Rasmusi Lerdorf',
    'ccc': 'Rasmusi Lerdorf',
}

for key, value in kata.items():
    print(key, "was created by", value)
