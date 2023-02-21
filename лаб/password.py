a=input()
b=input()
if len(a)<6:
    print('пароль слишком маленький')
    quit()
if a==b:
    print('пароль совпадает')
else:
    print('пароль не совпадает')