import csv


FILE_NAME = "contacts.csv"


def save_contacts():
    """Save all contacts to CSV file."""
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["name", "phone", "email"]
        )

        writer.writeheader()
        writer.writerows(contacts)


def load_contacts():
    """Load contacts from CSV file."""
    try:
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.DictReader(file)
            return list(reader)

    except FileNotFoundError:
        return []


def add_contact():
    """Add a new contact."""

    name = input("Enter contact name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()

    if not name or not phone or not email:
        print("All fields are required.")
        return

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    save_contacts()

    print("Contact added successfully!")


def view_contacts():
    """Display all contacts."""

    if not contacts:
        print("No contacts found.")
        return

    print("\n===== ALL CONTACTS =====")

    for number, contact in enumerate(contacts, start=1):
        print(f"\nContact {number}")
        print("Name:", contact["name"])
        print("Phone:", contact["phone"])
        print("Email:", contact["email"])
        print("------------------------")


def search_contact():
    """Search contact by full or partial name."""

    search_name = input("Enter name to search: ").strip()

    if not search_name:
        print("Please enter a name.")
        return

    found = False

    for contact in contacts:
        if search_name.lower() in contact["name"].lower():
            print("\nContact Found!")
            print("Name:", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            print("------------------------")

            found = True

    if not found:
        print("Contact not found.")


def update_contact():
    """Update an existing contact."""

    update_name = input(
        "Enter name of contact to update: "
    ).strip()

    for contact in contacts:

        if contact["name"].lower() == update_name.lower():

            print("\nContact found!")

            new_name = input(
                "Enter new name: "
            ).strip()

            new_phone = input(
                "Enter new phone number: "
            ).strip()

            new_email = input(
                "Enter new email: "
            ).strip()

            if not new_name or not new_phone or not new_email:
                print("All fields are required.")
                return

            contact["name"] = new_name
            contact["phone"] = new_phone
            contact["email"] = new_email

            save_contacts()

            print("Contact updated successfully!")
            return

    print("Contact not found.")


def delete_contact():
    """Delete an existing contact."""

    delete_name = input(
        "Enter name of contact to delete: "
    ).strip()

    for contact in contacts:

        if contact["name"].lower() == delete_name.lower():

            contacts.remove(contact)
            save_contacts()

            print("Contact deleted successfully!")
            return

    print("Contact not found.")


def show_menu():
    """Display the main menu."""

    print("\n==============================")
    print("       CONTACT BOOK")
    print("==============================")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Save & Exit")
    print("==============================")


# Load existing contacts when program starts
contacts = load_contacts()


# Main program
while True:

    show_menu()

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        update_contact()

    elif choice == "5":
        delete_contact()

    elif choice == "6":
        save_contacts()
        print("Contacts saved successfully.")
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 6.")