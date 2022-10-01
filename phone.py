phone_nb = input("Enter a phone number: ")
if len(phone_nb) == 12 or len(phone_nb) == 14:
    if ((phone_nb[1] == '-' and phone_nb[5] == '-' and phone_nb[9] =='-') \
        or(phone_nb[3] == '-' and phone_nb[7] == '-')):
        if ((phone_nb[:3].isdigit() and phone_nb[4:7].isdigit() and \
            phone_nb[8:].isdigit())
            or (phone_nb[0] == '1' and phone_nb[2:5].isdigit() and  phone_nb[6:9].isdigit() and
            phone_nb[10:].isdigit())):
            print('Valid')

else:
    print('Invalid')
