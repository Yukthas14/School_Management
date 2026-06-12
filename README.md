# School Management

A custom Frappe application developed to manage basic school operations such as student management, course enrollment, reporting, and admission workflows.

## Features

### Student Management

* Create and manage Student records.
* Store student details such as:

  * Student Name
  * Age
  * Grade
  * Address
  * Department

### Course Enrollment

* Manage student course enrollments.
* Maintain relationships between students and courses.

### Student APIs

Implemented server-side APIs using Frappe framework functions:

* `frappe.new_doc()` – Create new Student records.
* `frappe.get_doc()` – Fetch complete Student details.
* `frappe.db.get_value()` – Retrieve specific field values.
* `frappe.db.set_value()` – Update field values directly in the database.

### Reports

Implemented Query Reports including:

* **Student List Report**

  * Displays student details such as name, age, grade, and address.

* **Course Enrollment Report**

  * Displays information about student enrollments.

* **Department-wise Student Count Report**

  * Shows the number of students in each department using SQL aggregation.

### Workflow and Permissions

Implemented a Student Admission Workflow with role-based approvals.

Workflow States:

Admission Applied
↓
Teacher Verification
↓
Principal Approval
↓
Admission Confirmed

Roles Used:

* Teacher
* Principal
* Administrator

The workflow demonstrates how different users can perform specific actions based on assigned roles and permissions.


## Installation

Clone the repository inside your Frappe Bench:

```bash
cd ~/frappe-bench/apps
git clone https://github.com/Yukthas14/school_management.git
```

Install the app:

```bash
cd ~/frappe-bench
bench --site <site-name> install-app school_management
```

Run migrations:

```bash
bench migrate
```

Start the server:

```bash
bench start
```



