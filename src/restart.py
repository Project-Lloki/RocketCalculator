import excel as e


def restart():
    back = input('\nWould you like to go to another calculator? y/n ')
    if back == 'y':
        print('Aight, bringing you back!')
        import app
        app.run()
    elif back == 'n':
        if e.used:
            e.wb.save('Rocket Parameters.xls')
        print('OK!')
    else:
        print('Invalid! Try Again')
        restart()
