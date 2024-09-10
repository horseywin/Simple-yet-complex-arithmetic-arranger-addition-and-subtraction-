def arithmetic_arranger(problems, show_answers=False):
    stage = 0
    question = 0
    temp = ''
    x = []
    y = []
    s = []
    if len(problems) > 5:
        return 'Error: Too many problems.'
    for problem in problems:
        question += 1
        stage = 0

        problem = problem + ' '

        for char in problem:

            if char != ' ':
                temp += char

            else:

                if stage == 0:
                    x.append(temp)
                elif stage == 1:
                    s.append(temp)

                elif stage == 2:
                    y.append(temp)

                temp = ''

                stage += 1
 
    question = -1
    #Space
    whitespace = "    "
    #Answers
    aoutput = []
    #Lines
    loutput = []
    #First value
    xoutput = []
    #answer
    answer = []
    #Second value
    youtput = []
    for problem in problems:
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        for letter in letters:
            if not problem.find(letter) == -1:
                return 'Error: Numbers must only contain digits.'
        question += 1
        loutput.append(((max(len(str(x[question])), len(str(y[question])))) + 2) * '-')
        xoutput.append(f'{(len(loutput[question]) - len(str(x[question]))) * " "}{x[question]}')
        youtput.append(f'{s[question]}{(len(loutput[question]) - (len(str(y[question]))) - 1) * " "}{y[question]}')
        
        if s[question] == '+':
            answer.append(int(x[question]) + int(y[question]))
            aoutput.append(f'{(len(loutput[question]) - len(str(answer[question]))) * " "}{answer[question]}')


        elif s[question] == '-':
            answer.append(int(x[question]) - int(y[question]))
            aoutput.append(f'{(len(loutput[question]) - len(str(answer[question]))) * " "}{answer[question]}')

 
        else:
            return "Error: Operator must be '+' or '-'."

    for expression in x:
        if len(expression) > 4:
            return 'Error: Numbers cannot be more than four digits.'

    for expression in y:
        if len(expression) > 4:
            return 'Error: Numbers cannot be more than four digits.'

    final = []
    final.append(whitespace.join(xoutput))
    final.append(whitespace.join(youtput))
    final.append(whitespace.join(loutput))
    if show_answers:
        final.append(whitespace.join(aoutput))

    final = '\n'.join(final)
    
    return final

print(arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True)) 