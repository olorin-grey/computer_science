my_baby_bool = "true"
type(my_baby_bool)

print(type(my_baby_bool))
# <class 'str'>


my_baby_bool_two = True
type(my_baby_bool_two)

print(type(my_baby_bool_two))
# <class 'bool'>



# Using AND as the operator
def graduation_reqs(gpa, credits):
  if gpa >= 2.0 and credits >= 120:
    return "You meet the requirements to graduate!"


# Using OR as the operator
def graduation_mailer(gpa, credits):
  if gpa >= 2.0 or credits >= 120:
    return True



def graduation_reqs(gpa, credits):
	if (gpa >= 2.0) and (credits >= 120):
		return "You meet the requirements to graduate!"
	if (gpa >= 2.0) and not (credits >= 120):
		return "You do not have enough credits to graduate."
	if not (gpa >= 2.0) and (credits >= 120):
		return "Your GPA is not high enough to graduate."
	if not (gpa >= 2.0) and not (credits >= 120):
		return "You do not meet either requirement to graduate."

print(graduation_reqs(4.0, 36))

