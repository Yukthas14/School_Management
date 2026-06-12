// Copyright (c) 2026, Yuktha and contributors
// For license information, please see license.txt


frappe.ui.form.on('Student', {
    refresh: function(frm) {

        frm.add_custom_button('Update Grade', function() {

            frappe.call({
                method: 'school_management.api.update_student_grade',
                args: {
                    student_id: frm.doc.name
                },
                callback: function(r) {
                    frappe.msgprint(r.message);
                    frm.reload_doc();
                }
            });

        });

    }
});