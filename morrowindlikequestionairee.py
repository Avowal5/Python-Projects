given_name = input("What is your name? " )
age = int(input("How old are you? "))
geographic_origin = input("From which region do you hail? ")
racial_origin = input("What is your race? ")
ian = "ian"
the = "the"
birthsign = input("And what sign were you born under? ")

print(f"Right then. You are a {age} year old {racial_origin} by the name of {given_name} hailing from the region of {geographic_origin} who was born under the sign of {birthsign}, ")

correctness = input("Was the following information correct? ").lower()


if correctness in ['yes', 'y']:
    print(f"Very well then, now before you are released you have the choice of where to settle, currently we have two towns with work allotments but currently only one of them has free housing, Seyda Neen, the town you are currently in has a spare shack, and the work allotment is for you to be a fisherman, Balmora on the otherhand, has no free housing avaliable at this time, however the work is more fitting of someone with higher intelligence and personality, so the bar will be higher and there is no guarantee that you will get the job, so please decide carefully. ")
    area_allotment = input("Have you decided where to live? ").lower()
    if area_allotment in ['Seyda Neen', 'seyda neen']:
        print(f"Excellent choice, Seyda Neen is a great place to get on your feet.")
    elif area_allotment in ['Balmora', 'balmora']:
        print(f"Well then, I wish you safe travels on your journey to Balmora, it is quite the ways away from Seyda Neen.")
elif correctness in ['no', 'n']:
    print("Then please start over with another form.")


