def psychologist():
    print('tell something')
    while True:
        answer = (yield)
        if answer is not None:
            if answer.endswith('?'):
                print("Don't ask why")
            elif 'good' in answer:
                print('Good')
            elif 'bad' in answer:
                print('Bad')


if __name__ == '__main__':
    free = psychologist()
    next(free)
    # free.send('why are you so handsome?')
    # free.send('you are a good man')
    next(free)
