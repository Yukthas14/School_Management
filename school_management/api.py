# import frappe


# @frappe.whitelist()
# def create_student(student_name, age, grade, address):

#     student = frappe.new_doc("Student")

#     student.student_name = student_name
#     student.age = age
#     student.grade = grade
#     student.address = address

#     student.insert()

#     frappe.db.commit()

#     return student.name

# @frappe.whitelist()
# def get_student(student_id):

#     student = frappe.get_doc(
#         "Student",
#         student_id
#     )

#     return {
#         "name": student.student_name,
#         "age": student.age,
#         "grade": student.grade,
#         "address": student.address
#     }

# # @frappe.whitelist()
# # def get_student_grade(student_id):

# #     grade = frappe.db.get_value(
# #         "Student",
# #         student_id,
# #         "grade"
# #     )

# #     return grade
# @frappe.whitelist()
# def update_student_grade(student_id):
#     frappe.db.set_value(
#         "Student",
#         student_id,
#         "grade",
#         "11th"
#     )

#     return "Grade Updated"

#  @frappe.whitelist()
# def update_student_grade(student_id):
#     frappe.db.set_value(
#         "Student",
#         student_id,
#         "grade",
#         "11th"
#     )

#     return "Grade Updated"


import frappe

@frappe.whitelist()
def update_student_grade(student_id):
    frappe.db.set_value(
        "Student",
        student_id,
        "grade",
        "11th"
    )
    frappe.db.commit()

    return "Grade Updated"