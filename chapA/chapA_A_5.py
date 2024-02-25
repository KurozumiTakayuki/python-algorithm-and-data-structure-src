def sample_generator():
    yield 'おはよう'
    yield 'こんにちは'
    yield 'こんばんは'


gen_obj = sample_generator()
for text in gen_obj:
    print(text)
