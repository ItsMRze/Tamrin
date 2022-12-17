b_list = ['Mehdi Rezaei','Amir Zare','Negar Mohammadi','Ali Barzegar','Kian Rostamin','Sara Alipoor']

def add_b (name):
    b_list.append(name)
    print('{} is add to list'.format(name))
    print('Your List Is Now : ',b_list)

def search_b(name):
    T_F_list = []

    #Cheking b_list

    for i in b_list:
        if i == name:
            T_F_list.append('True')
            break
        else:
            T_F_list.append('False')

    # Cheking True Or False List Last Index

    a = len(T_F_list)-1
    if T_F_list[a] == 'True':
        print('True')
        return True

    else:
        print('False')
        return False


def del_b (name):
    if search_b(name) == True:
        b_list.remove(name)
        print('Your List Is Now : ',b_list)
    else:
        print('There Is No One With {} Name'.format(name))

x = str(input('Do You Want To Start Program ? (Y or Yes / N or NO) : '))

while x == 'Y' or x == 'Yes' or x == 'y' or x == 'yes':
    z = int(input('''
1.Jahat Add Kardan Esm Bimar Be List Adad 1
2.Search Ems Bimar Dar Data base Adad 2
3.Hazf Kardan Name Bimar Adad 3
Adad Ra Vared Konid : '''))
    esm = str(input('Esm Bimar Mored Nazar Ra Vared Konid (Manande : Mehdi Rezaei) : '))
    if z == 1:
        add_b(esm)
    if z == 2:
        search_b(esm)
    if z == 3:
        del_b(esm)

    x = str(input('Do You Want To Countineu ? (Y or Yes / N or NO) : '))

















































