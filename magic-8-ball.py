# TechPrep Python Project One
# Question One – Random Number Generator
# Magic 8 Ball

import random

answers = [
    # the positive responses
    'It is certain.',
    'It is decidedly so.',
    'Without a doubt.',
    'Yes, definitely.',
    'You may rely on it',
    'As I see it, yes.',
    'Most likely.',
    'Outlook good.',
    'Yes.',
    'Signs point to yes.',  
    # the non-committal responses
    'Reply hazy, try again.',
    'Ask again later.',
    'Better not tell you now.',
    'Cannot predict now.',
    'Concentrate and ask again.',
    # the negative responses
    'Don\'t count on it.',
    'My reply is no.',
    'My sources say no.',
    'Outlook not so good.',
    'Very doubtful.'
]

user_question = str(input('Ask the Magic 8 Ball a "yes-or-no" question: '))

random_no = random.randrange(len(answers))

print(answers[random_no])