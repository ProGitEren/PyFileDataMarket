questions = {'What': 'A', 'Where': 'B', 'When': 'C', 'How': 'D'}
texts = [['A:HFF', 'B:sada', 'C:dashas', 'D:dasd'], ['A:HFF', 'B:sada', 'C:dashas', 'D:dasd'], ['A:HFF', 'B:sada', 'C:dashas', 'D:dasd'], ['A:HFF', 'B:sada', 'C:dashas', 'D:dasd']]


def check_answer(a, b, corrected):
    if a == b:
        corrected += 1
    return corrected


def question(text,options,list1):
    print(text)
    for i in options:
        print(i)
    answer=input('What is your answer: ')
    list1.append(answer)
    return list1

def main(quest):
    answerlist = []
    correct = 0
    answerkey=list(quest.values())
    for i in range(len(quest)):
        lister=list(quest.keys())
        question(lister[i],texts[i] , answerlist)
        correct = check_answer(answerkey[i], answerlist[i], correct)
    Achievement = 100*(int(correct)/len(answerkey))
    print(f'You have done {Achievement} percent of the quiz correctly!')
    print(f'You have {correct} amount of correct answers')
    print('Answerkey:')
    print(answerkey)
    print('Your answers')
    print(answerlist)
    return correct

answerkey11 = ['A', 'B', 'C', 'D']
main(questions)

