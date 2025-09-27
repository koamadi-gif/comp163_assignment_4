student_name = "Kobby Amadi"
current_gpa = 3.8
study_hours = 8
social_points = 50
stress_level = 70

difficulty_choice = input()
course_credits = 0
recommendation = ""

easy_mode = "Easy: (12 credits)"
normal_mode = "Normal: (15 credits)"
hard_mode = "Hard: (18 credits)"

if difficulty_choice == easy_mode:
    print(f"Difficulty: {easy_mode}")
    course_credits = 12
    if current_gpa < 2.5:
        recommendation = "Perhaps you should take more time studying."
    else:
        recommendation = "Good GPA. Stay on stop of studies to maintain it or make it better."

elif difficulty_choice == normal_mode:
    print(f"Difficulty: {normal_mode}")
    course_credits = 15
    if 2.5 <= current_gpa < 3.5:
        recommendation = "These standard study habits are good for your GPA. Keep it up!"
    elif current_gpa >= 3.5:
        recommendation = "With your GPA you should try a better way to study but this will do for now."
    else:
        recommendation = "Your GPA is below average. Perhaps you should try a lighter credit load."

elif difficulty_choice == hard_mode:
    print(f"Difficulty: {hard_mode}")
    course_credits = 18
    if current_gpa >= 3.5:
        recommendation = "Great GPA. You should have no problem with this credit load."
    elif current_gpa >= 3.0:
        recommendation = "Your GPA is decent. But you may want to pay more attention in class this time."
    else:
        recommendation = "Your GPA is below average. This credit load is not the best option."

print(f"Current GPA: {current_gpa}")
print(f"Choose Course Load: {course_credits} credits")
print(f"Suggestion: {recommendation}")

study_options = ["Programming", "Math", "English", "History"]
study_choice = input(f"Choose a study option: {study_options}")

if study_choice in study_options:
    print(f"Study Option: {study_choice}")
elif study_choice not in study_options:
    print(f"Invalid study option. Choose from the provided study options: {study_options}.")

complex_conditions = (not (current_gpa >= 3.8)) or (social_points < 50)

if study_choice in study_options:
    print(f"Study Option: {study_choice}")
    complex_conditions = (not (current_gpa >= 3.8)) or (social_points < 50)

    if study_choice == "Programming":
        if complex_conditions:
            print("Your GPA isn't great and your social life isn't either. Perhaps do less partying and more studying.")
            study_hours += 2
        else:
            print("Your status is balanced. Now focus on improving your skills.")

    elif study_choice == "Math":
        if study_choice == "Math" and current_gpa >= 3.8 and social_points >= 50:
            print("Good choice! Consider teach others your knowledge.")
        else:
            print("College math is way different from high school. Take time to actually study the material.")

    elif study_choice == "English":
        if not (stress_level >= 50):
            print("Great choice to balance your schedule. Remember to be creative.")
        else:
            print("Your putting too much stress on yourself.")

    elif study_choice == "History":
        if current_gpa < 3.8 or study_hours < 8:
            print("You need to read a lot more often. Try scheduling a reading time.")
        else:
            print("This class will give you good information. Try to be active in discussions.")

print(f"Updated Student Status:")
print(f"Study Hours: {study_hours}")
print(f"Complex Condition Check: {complex_conditions}")

print("\n=================================")
print("         FINAL ANALYSIS")
print("=================================")

if type(course_credits) is int:
    credit_check = "PASS: Required credits are met."
elif type(course_credits is not int):
    credit_check = "FAIL: Not enough required credits."

print(f"Data Integrity Check: {credit_check}")

print(f"Final Study Hours: {study_hours} hrs/week")
print(f"Final Social Points: {social_points} pts")
print(f"Final Stress Level: {stress_level}%")
print(f"Complex Condition Met: {complex_conditions}")



