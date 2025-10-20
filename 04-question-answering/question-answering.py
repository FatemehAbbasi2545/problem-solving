questions = [
    { 
        'question': 'Who is the best golfer in the world in 2025?',
        'answer': 'Scheffler'
    },
    { 
        'question': 'Which city is the capital of Italy?',
        'answer': 'Rome'
    },
    { 
        'question': 'What software company is headquartered in Redmond, Washington?',
        'answer': 'Microsoft'
    },
    { 
        'question': 'What is the world’s largest retailer as of 2025?',
        'answer': 'Walmart'
    },
    { 
        'question': 'What company was initially known as "Blue Ribbon Sports"?',
        'answer': 'Nike'
    }
]

for x in questions:
    user_input = input(f'{x['question']} ')
    if user_input.lower() == x['answer'].lower():
        x['result'] = True
    else:
        print('Your answer is incorrect.')
        user_input = input(f'{x['question']} ')
        x['result'] = True if user_input.lower() == x['answer'].lower() else False
        
for x in questions:
    print(f'{x["question"]}: {x["answer"]}, result: {'You succeeded. Your answer is correct.' if x['result'] == True else 'You failed. Your answer is incorrect.'}')