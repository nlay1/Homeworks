di = [{'name':'Todd', 'phone':'555-1414', 'email':'todd@mail.net'}, 
{'name':'Helga', 'phone':'555-1618', 'email':'helga@mail.net'}, 
{'name':'Princess', 'phone':'555-3141', 'email':''}, 
{'name':'LJ', 'phone':'555-2718', 'email':'lj@mail.net'}]

print("Users whose phone nb ends in 8")
for user in di:
    if user['phone'][-1] == '8':
        print(user)
print("Users who don't have email")
for user in di:
    if user['email'] == '':
        print(user)
