from survey import AnonymousSurvey

question = 'What language did you first learn to speak?'
survey = AnonymousSurvey(question)

survey.show_question()
while True:
    answer = input('Input your answer: \n')
    if answer == 'q':
        break
    else:
        survey.store_response(answer)

print('Thank you for your attendation.\n')
print('Here is your answer.\n')
survey.show_response()
