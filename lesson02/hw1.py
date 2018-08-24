people = {'Alice':{'phone':'2341','addr':'Foo drive 23'},
          'Beth':{'phone':'9102','addr':'Bar street 42'},
          'Cecil':{'phone':'3158','addr':'Baz avenue 90'}，
          'David Cai':{'phone':'8848','addr':'Forbidden Palace'}}

labels = {'phone':'phone number','addr':'address'}

while True:
    name = input("Name: ")
    while name not in people:
        print("Name not in Database")
        name = input("Name: ")

    request = input('Phone number (p) or address (a)?')
    while request not in ['a','p']:
        print("Invalid input")
        request = input('Phone number (p) or address (a)?')

    if(request == 'p'):
        key = 'phone'

    if(request == 'a'):
        key = 'addr'

    print("%s's %s is %s" % (name, labels[key], people[name][key]))

    opt = input("press q to quit or any key to continue\n")
    if opt == 'q':
        break
