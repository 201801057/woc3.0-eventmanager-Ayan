# Contact Manager -- Python
import collections

d = {}

while 1:
    print("Enter\n1 : Insert\n2 : Manage\n3 : Retrive\n0 : End")
    print('Enter Your Choice: ')

    choice = int(input())

    if choice == 1:
        name = input('Enter Your Name:')
        contact = input('Enter Your Contact Number:')
        d[name] = contact
    elif choice == 2:
        d1 = collections.OrderedDict(sorted(d.items()))
        print(d1)
    elif choice == 3:
        keywords = input('Enter the keyword for Search Name:')

        for k, q in d.items():
            if k.find(keywords) >= 0:
                print(k, q)

    else:
        print('End')
        break
