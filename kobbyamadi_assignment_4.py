# USED GOOGLE GEMINI TO HELP ME OUT FOR THIS ASSIGNMENT
student_name = "Kobby Amadi"
current_gpa = 3.8
study_hours = 8
social_points = 50
stress_level = 70

difficulty_choice = input()
course_credits = 0
recommendation = ""

easy_mode = ("Easy: (12 credits)")
normal_mode = ("Normal: (15 credits)")
hard_mode = ("Hard: (18 credits)")

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







