print('welcome to the computer hardware quiz game!')

playing = input('Do you want to play? ')

if playing.lower() != 'yes':
    quit()
    
print('Okay! lets begin ')
score = 0

answer = input('What does CPU stand for? ')
if answer.lower() == 'central processing unit':
    print('That is correct! ')
    score += 1
else:
    print('incorrect!')
    

answer = input('What does GPU stand for? ')
if answer.lower() == 'graphic processing unit' or 'graphics processing unit':
    print('That is correct! ')
    score += 1
else:
    print('incorrect!')
    

answer = input('What does RAM stand for? ')
if answer.lower() == 'random access memory':
    print('That is correct! ')
    score += 1
else:
    print('incorrect!')
    

answer = input('what does PSU stand for? ')
if answer.lower() == 'power supply unit':
    print('That is correct! ')
    score += 1
else:
    print('incorrect!')

print('You got ' + str(score) + ' questions correct!')
print('You got ' + str((score / 4) * 100)  + '%.')


