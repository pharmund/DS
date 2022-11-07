import sys

def first_list_minus_second_list(list1, list2):
    new_list = [x for x in list1 if x not in list2]
    return new_list

def get_emails():
    clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com', 
    'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com', 'elon@paypal.com', 
    'jessica@gmail.com']
    participants = ['walter@heisenberg.com', 'vasily@mail.ru', 'pinkman@yo.org', 
    'jessica@gmail.com', 'elon@paypal.com', 'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
    recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']

    contact_list = clients + participants
    contact_list = list(set(contact_list))

    if sys.argv[1] == 'call_center':
        lst = first_list_minus_second_list(clients, recipients)
        lst.append('jessica@gmail.com')
        print('clients =', lst)
    if sys.argv[1] == 'potential_clients':
        print('participants =', first_list_minus_second_list(participants, clients))
    if sys.argv[1] == 'loyalty_program':
        print('recipients =', first_list_minus_second_list(clients, participants))


if __name__ == '__main__':
    if len (sys.argv) != 2 or (sys.argv[1] != 'call_center' and sys.argv[1] != 'potential_clients' and sys.argv[1] != 'loyalty_program'):
        raise Exception("Error argument")
    get_emails()
