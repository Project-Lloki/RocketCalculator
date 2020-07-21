def restart():
    back = input('\nWould you like to go to another calculator? y/n ')
    print('\n')
    if back == 'y':
        print('Aight, bringing you back!')
        import app
        app.run()
    elif back == 'n':
        print('OK!')
    else:
        print('Invalid! Try Again')
        restart()