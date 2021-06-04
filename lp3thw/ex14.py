from sys import argv
script , name = argv
prompt='>'
print(f'Hey {name} how are you doing? ')
print(f'You are currently executing script {script}')
print('Are you enjoying this ?')
ans = input(prompt)
print('alright you said {}'.format(ans))


