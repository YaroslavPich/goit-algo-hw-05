def parse_input(user_input: str) -> tuple:
    """Command recognition"""
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def input_error(func):
    """Error handling ValueError"""

    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Enter correct data in the format (add 'name' 'contact')"

    return inner


@input_error
def add_contact(args, contacts):
    """Adding a contact."""
    name, phone = args
    for digit in phone:
        if digit not in "+0123456789":
            return "Phone number! Please enter in the format - +380671234567"
    if name.lower() in contacts or phone in contacts.values():
        return "This contact or phone number already exists.\nPlease use the \
'Change' command to replace the existing one.\n\
Or use a different name or phone number"
    contacts[name.lower()] = phone
    return "Contact added."


def change_error(func):
    """Error handling ValueError"""

    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Enter correct data in the format (Change 'name' 'contact')"

    return inner


@change_error
def change_contact(args: list[str], contacts: str) -> str:
    """Overwriting a contact"""
    change_name, phone = args
    if change_name.lower() in contacts:
        for digit in phone:
            if digit not in "+0123456789":
                return """Phone number! Please enter in the format - +380671234567"""
        contacts[change_name.lower()] = phone
        return "Contact updated."
    else:
        return "There is no such contact in the records!"


def phone_error(func):
    """Error handling IndexError"""

    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            return "Contact not found!"

    return inner


def phone_key_error(func):
    """Error handling KeyError"""

    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found!"

    return inner


@phone_key_error
@phone_error
def show_phone(args: list[str], contacts: str) -> str:
    """Contact output by given name."""
    show_phone_of_name = args[0]
    return contacts[show_phone_of_name.lower()].capitalize()


def show_all(contacts: dict) -> str:
    """Output of all contacts."""
    output = ""
    if len(contacts) != 0:
        for name, phone in contacts.items():
            output += f"{name.capitalize()}: {phone}\n"
    else:
        output = "There are no contacts."
    return output


def main():
    """'The main program."""
    contacts = {}
    print("""Welcome to the assistant bot!""")
    while True:
        while True:
            user_input = input("Enter a command: ")
            if user_input:
                break
            else:
                print("You have not provided a command!")
        command, *args = parse_input(user_input)

        if command in ("close", "exit"):
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
