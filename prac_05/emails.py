"""
Word Occurrences
Estimate: 20 minutes
Actual:   32 minutes
"""

emails_to_names = {}
email = input("Email: ")
while email != "":
    email_name = email.split('@')[0]
    name_list = email_name.split('.')
    name = ' '.join(name_list).title()
    is_correct = input(f"Is your name {name}? (Y/n) ").lower()
    if is_correct != "y":
        name = input("Name: ")
    emails_to_names[email] = name
    email = input("Email: ")

print("\nStored emails and names:")
for email, name in emails_to_names.items():
    print(f"{name} ({email})")
