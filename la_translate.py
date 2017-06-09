def la_translate(msg):
    '''
    if you had your eng keyboard on and you were typing in ukrainian or
    vice versa, this program will correct your msg

    >>> la_translate('Руддщб Ш фь пщштп ещ нщг тщц')
    hello, i am going to you now
    >>> la_translate('ghbdsn z nhj[b pfnhbvf.cz')
    привіт я трохи затримаюся
    '''
    msg = list(msg.lower())
    ukr = "йцукенгшщзхїфівапролджєячсмитьбю"
    eng = "qwertyuiop[]asdfghjkl;'zxcvbnm,."
    lg = input('Please, enter a language in which the msg will be la_translated: eng or ukr ')
    if lg == 'eng':
        for i in range(len(msg)):
            if msg[i] not in ukr:
                continue
            else:
                ind = ukr.index(msg[i])
                msg[i] = eng[ind]
    elif lg == 'ukr':
        for i in range(len(msg)):
            if msg[i] not in eng:
                continue
            else:
                ind = eng.index(msg[i])
                msg[i] = ukr[ind]
    print(''.join(msg))
