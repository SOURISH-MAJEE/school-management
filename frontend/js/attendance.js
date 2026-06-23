const API = "http://127.0.0.1:8000";

function showMsg(id, text, type) {
    const el = document.getElementById(id);
    el.innerText = text;
    el.className = "msg " + type;
    el.style.display = "block";
    setTimeout(() => el.style.display = "none", 3000);
}

async function loadAttendance() {
    const classes  = await fetch(API + "/classes/").then(r => r.json());
    const subjects = await fetch(API + "/subjects/").then(r => r.json());
    const teachers = await fetch(API + "/teachers/").then(r => r.json());
    const sessions = await fetch(API + "/attendance-sessions/").then(r => r.json());
    const students = await fetch(API + "/students/").then(r => r.json());
    const records  = await fetch(API + "/attendance/").then(r => r.json());

    const classSel = document.getElementById("ses-class");
    classSel.innerHTML = '<option value="">Select Class</option>';
    for (let c of classes) {
        classSel.innerHTML += `<option value="${c.class_id}">${c.class_name} - ${c.section}</option>`;
    }

    const subSel = document.getElementById("ses-subject");
    subSel.innerHTML = '<option value="">Select Subject</option>';
    for (let s of subjects) {
        subSel.innerHTML += `<option value="${s.subject_id}">${s.subject_name}</option>`;
    }

    const teachSel = document.getElementById("ses-teacher");
    teachSel.innerHTML = '<option value="">Select Teacher</option>';
    for (let t of teachers) {
        teachSel.innerHTML += `<option value="${t.teacher_id}">${t.name}</option>`;
    }

    const sesSel = document.getElementById("att-session");
    sesSel.innerHTML = '<option value="">Select Session</option>';
    for (let s of sessions) {
        sesSel.innerHTML += `<option value="${s.session_id}">Session ${s.session_id} - ${s.date} - Period ${s.period}</option>`;
    }

    const stuSel = document.getElementById("att-student");
    stuSel.innerHTML = '<option value="">Select Student</option>';
    for (let s of students) {
        stuSel.innerHTML += `<option value="${s.student_id}">${s.roll_number} - ${s.name}</option>`;
    }

    let rows = "";
    for (let a of records) {
        const stu = students.find(s => s.student_id === a.student_id);
        const ses = sessions.find(s => s.session_id === a.session_id);
        const color = a.status === "Present" ? "green" : a.status === "Absent" ? "red" : "orange";
        rows += `<tr>
            <td>${a.attendance_id}</td>
            <td>${ses ? ses.date + " Period " + ses.period : "-"}</td>
            <td>${stu ? stu.name : "-"}</td>
            <td style="color:${color}">${a.status}</td>
            <td><button class="btn-red" onclick="deleteAttendance(${a.attendance_id})">Delete</button></td>
        </tr>`;
    }
    document.getElementById("att-list").innerHTML = rows;
}

async function addSession() {
    const classId   = document.getElementById("ses-class").value;
    const subjectId = document.getElementById("ses-subject").value;
    const teacherId = document.getElementById("ses-teacher").value;
    const date      = document.getElementById("ses-date").value;
    const period    = document.getElementById("ses-period").value;

    if (!classId || !subjectId || !teacherId || !date || !period) {
        showMsg("ses-msg", "Please fill all fields!", "error");
        return;
    }

    const res = await fetch(API + "/attendance-sessions/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            class_id: parseInt(classId),
            subject_id: parseInt(subjectId),
            teacher_id: parseInt(teacherId),
            date: date,
            period: parseInt(period)
        })
    });

    if (res.ok) {
        showMsg("ses-msg", "Session created!", "success");
        loadAttendance();
    } else {
        showMsg("ses-msg", "Error creating session!", "error");
    }
}

async function markAttendance() {
    const sessionId = document.getElementById("att-session").value;
    const studentId = document.getElementById("att-student").value;
    const status    = document.getElementById("att-status").value;

    if (!sessionId || !studentId || !status) {
        showMsg("att-msg", "Please fill all fields!", "error");
        return;
    }

    const res = await fetch(API + "/attendance/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            session_id: parseInt(sessionId),
            student_id: parseInt(studentId),
            status: status
        })
    });

    if (res.ok) {
        showMsg("att-msg", "Attendance marked!", "success");
        loadAttendance();
    } else {
        showMsg("att-msg", "Error marking attendance!", "error");
    }
}

async function deleteAttendance(id) {
    if (!confirm("Delete this record?")) return;
    const res = await fetch(API + "/attendance/" + id, { method: "DELETE" });
    if (res.ok) {
        showMsg("att-msg", "Deleted!", "success");
        loadAttendance();
    } else {
        showMsg("att-msg", "Cannot delete!", "error");
    }
}

loadAttendance();