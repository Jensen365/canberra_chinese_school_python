print("welcome to use the grade calculater!")

coursework_score = float(input("Enter your coursework score: "))
final_exam_score = float(input("Enter your exam score: "))

final_grade = 0.4 * coursework_score + 0.6 * final_exam_score

print("Your final grade is ", final_grade) 