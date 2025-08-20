email = 'anil.kumar@gmail.com'
print(email.find('@'))
print(email.find('gmail'))


print(email.find('.'))


email = 'anil.kumar@gmail.com'
at_index = email.find('@')
dot_index = email.find('.', at_index + 1)

print(email.find('p'))

if at_index > -1 and dot_index > -1:
    print("Valid email address:", email)

