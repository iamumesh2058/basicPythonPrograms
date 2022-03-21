# simple multiple choice questions

questions = [
  'What is the color of black ink? \na. Black \nb. Blue \nc. Red \nd. Pink',
  'What is the color of sky? \na. Black \nb. Blue \nc. Red \nd. Pink',
  'What is the color of human blood? \na. Black \nb. Blue \nc. Red \nd. Pink',
  'What is the color of pink rose? \na. Black \nb. Blue \nc. Red \nd. Pink'
]

questions_with_answer = [
  [questions[0], 'a'],
  [questions[1], 'b'],
  [questions[2], 'c'],
  [questions[3], 'd']
]

score = 0
print('You have to enter answer as a, b, c or d')
for i in range(0, len(questions)):
  print(questions[i])
  your_answer = input("Enter answer : ").lower()
  if your_answer not in ['a', 'b', 'c', 'd']:
    your_answer = input("Please enter answer according to suggestion : ").lower()
    
  if your_answer == questions_with_answer[i][1]:
    score += 1
    
print(f"You have answered {score} out of {len(questions)} correctly.")
  