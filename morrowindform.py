given_name = input("What is your name? ")
gender = input("Are you male, or female? ")
age = int(input("How old are you? "))
geographic_origin = input("From which region do you hail? ")
racial_origin = input("What is your race? ")
birthsign = input("And what sign were you born under? ")


def _character():
    print(
        f"Right then. You are a {age} year old {gender} of {racial_origin} heritage by the name of {given_name} "
        f"hailing from the region of {geographic_origin} who was born under the sign of {birthsign}.")

    correctness = input("Was the following information correct? ").lower()

    if correctness in ['no', 'n']:
        print("Then please start over with another form.")
        return

    job_type = input("What job would you like? ")
    print(
        f"Very well then, now before you are released you have the choice of where to settle...")

    area_allotment = input("Have you decided where to live? ").lower()
    print(f"Excellent choice. {area_allotment} is a great place to get on your feet. I'm sure they will appreciate your work as a {job_type} Before you go, I humbly request that you do deliver a package for me, it is of the utmost importance so I would highly appreciate it if you do take the time out of your day to deliever it, there will be compensation and a reward for you. However I do understand if you do not have the time.")
    work_choice = input("Will you deliver the pacakge? ").lower()
    if work_choice in ['yes', 'y']:
        print("[PACKAGE ADDED TO YOUR INVENTORY] Thank you, please report back when the job is finished to collect your reward.")
    elif work_choice in ['no', 'n']:
        print("Oh well, farewell to you.")


_character()