def main():
    """Create dictionary of emails to corresponding names."""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        confirmation = input("Is your name {}? (Y/n) ".format(name))
        if confirmation.upper() != "Y" and confirmation != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print("{} ({})".format(name, email))
    # print(email_to_name)


def get_name_from_email(email):
    """Get name from email."""
    first_name = email.split('@')[0]
    surname = first_name.split('.')
    full_name = " ".join(surname).title()
    return full_name


main()
