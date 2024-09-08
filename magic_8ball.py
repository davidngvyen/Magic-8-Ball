import random
import turtle as t

ques_ans = open('ask_ans.txt', 'w')


def colored(r, g, b, text):
    return f"\033[38;2;{r};{g};{b}m{text}\033[0m"


def ball_8(reply=1):
    """prints out 8ball and ask first question"""
    t.hideturtle()
    t.speed(0)
    t.fillcolor('black')
    t.begin_fill()
    t.circle(175)
    t.end_fill()
    t.fillcolor('white')
    t.begin_fill()
    t.penup()
    t.sety(87.5)
    t.pendown()
    t.circle(100, 360)
    t.end_fill()
    t.color('black')
    t.circle(50)
    t.penup()
    t.sety(187.5)
    t.pendown()
    t.circle(50)
    if reply == 1:
        v = t.textinput('8 ball', 'Enter Question For 8 Ball to answer')
        ques_ans.write('Question: ')
        ques_ans.write(v)
        ques_ans.write('\n')
        return v
    if reply == 0:
        v = t.textinput('8 ball', 'Enter a Yes or No question for 8 Ball to answer')
        ques_ans.write('Question: ')
        ques_ans.write(v)
        ques_ans.write('\n')
        return v


def magic():
    """displays output background"""
    t.speed(0)
    t.ht()
    t.color('white')
    t.fillcolor('black')
    t.begin_fill()
    t.circle(175)
    t.end_fill()
    random_choose = random.randint(0, 5)
    color_list = ['dark blue', 'purple', 'dark green', 'maroon', 'red', 'grey']
    color = color_list[random_choose]
    t.fillcolor(f'{color}')
    t.begin_fill()
    t.circle(175, 360, 3)
    t.penup()
    t.end_fill()


def questionys(ask):
    ''' This will determine if the question is a yes or no'''
    check = ask.lower().split()
    test_list = ['should', 'can', 'will', 'could', 'may', 'might', 'shall', 'must', 'do', 'does', 'have', 'has', 'am',
                 'is', 'are']
    total = 0
    for i in range(len(check)):
        for j in range(len(test_list)):
            if check[0] == test_list[j]:
                total += 1
    if total >= 1:
        return 1
    else:
        return 0


def yes_no(x):
    """if input is Yes starts the game"""
    y = 1
    while y != 0:
        if x == 'Yes' or x == 'yes':
            y == 0
            return True
        elif x == 'No' or x == 'no':
            y == 0
            return False
            print(colored(255, 255, 255, 'Bye comeback soon'))
        else:
            x = input(colored(255, 255, 255, 'Bad input! Try again: '))


def answer():
    """randomizes answer to questions"""
    x = random.randint(0, 15)
    if x == 0:
        z = 55
        ans = 'It is certain'
    if x == 1:
        z = 75
        ans = 'It is decidedly so'
    if x == 2:
        z = 75
        ans = 'Without a doubt'
    if x == 3:
        z = 90
        ans = 'Reply hazy, try again'
    if x == 4:
        z = 75
        ans = 'Ask again later'
    if x == 5:
        z = 95
        ans = 'Better not tell you now'
    if x == 6:
        z = 75
        ans = 'Don’t count on it'
    if x == 7:
        z = 75
        ans = 'My reply is no'
    if x == 8:
        z = 90
        ans = 'My sources say no'
    if x == 9:
        z = 85
        ans = 'Outlook not so good'
    if x == 10:
        z = 75
        ans = 'As I see it, yes'
    if x == 11:
        z = 85
        ans = 'Signs point to yes'
    if x == 12:
        z = 75
        ans = 'Very doubtful'
    if x == 13:
        z = 75
        ans = 'Outlook good'
    if x == 14:
        z = 85
        ans = 'Cannot predict now'
    if x == 15:
        z = 84
        ans = 'Better ask a peer'

    magic()
    t.setposition(-z, 175)
    t.write(ans, font=("normal", 15, "normal"))
    ques_ans.write('Answer: ')
    ques_ans.write(ans)
    ques_ans.write('\n')


print(colored(255, 255, 255, 'Welcome to Magic 8 Ball'))
user_input = input(colored(255, 255, 255, 'Would you like to play (Yes/No): '))
play = yes_no(user_input)
# until user enters no they keep asking 8ball questions
while play:
    asked = ball_8()
    test = questionys(asked)
    t.clearscreen()
    if test == 1:
        t.clearscreen()
        answer()
        again = t.textinput('8 Ball', 'Would you like to play again')
        t.clearscreen()
        again = again.lower()
        if again == 'yes':
            play = True
            y = 0
        elif again == 'no':
            play = False
            y = 0
        else:
            again = t.textinput('8 Ball', 'Bad Input, Try again')
    else:
        asked = ball_8(0)
        test = questionys(asked)
        t.clearscreen()
        if test == 1:
            t.clearscreen()
            answer()
            again = t.textinput('8 Ball', 'Would you like to play again')
            t.clearscreen()
            again = again.lower()
            if again == 'yes':
                play = True
                y = 0
            elif again == 'no':
                play = False
                y = 0
            else:
                again = t.textinput('8 Ball', 'Bad Input, Try again')
print(colored(255, 255, 255, 'Thank you for playing'))