is_happy = True
and_you_know_it = True 
if is_happy and and_you_know_it:
    print("clap your hands")
else:
    print("I am not fulfilled")
#output: clap your hands

on_vacation = True
go_to_beach = True
is_hungry = True
if on_vacation and go_to_beach:
    print("I wear my swimsuit")
elif on_vacation and not go_to_beach:
    print("I wear my casual clothes")
elif on_vacation and is_hungry:
    print("I go to the restaurant")