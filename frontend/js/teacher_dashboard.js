const API = "http://127.0.0.1:8000";

// Check login
const userType = localStorage.getItem("user_type");
const userId   = parseInt(localStorage.getItem("user_id"));
const userName = localStorage.getItem("user_name");

if (!userType || userType !== "teacher") {
    alert("Please login as teacher first!");
    window.location.href = "login.html";
}

// Show name
document.getElementById("teacher-name").innerText = userName;

// Show message
function showMsg(id, text, type) {
    const el = document.getElementById(id);
    el.innerText = text;
    el.className = "msg " + type;
    el.style.display = "block";
    setTimeout(() => el.style.display = "none", 3000);
}

// Show/hide sections
function showSection(section) {
    if (section === 'subjects')         loadMySubjects();
    if (section === 'create-session')   loadCreateSession();
    if (section === 'mark-attendance')  loadMarkAttendance();
}

// Logout
function logout() {
    localStorage.clear();
    window.location.href = "login.html";
}

// ─── LOAD PROFILE ───
async function loadProfile() {
    const res  = await fetch(API + "/teachers/" + userId);
    const data = await res.json();

    document.getElementById("teacher-email").innerText = "Email: " + data.email;
    document.getElementById("teacher-profile").innerHTML = `<tr>
        <td>${data.name}</td>
        <td>${data.age}</td>
        <td>${data.gender}</td>
        <td>${data.email}</td>
        <td>${data.phone}</td>
    </tr>`;
}

// ─── LOAD MY SUBJECTS ───
async function loadMySubjects() {
    const res  = await fetch(API + "/subjects/teacher/" + userId);
    const data = await res.json();

    let rows = "";
    for (let s of data) {
        rows += `<tr>
            <td>${s.subject_id}</td>
            <td>${s.subject_name}</td>
        </tr>`;
    }
    document.getElementById("teacher-subjects").innerHTML =
        rows || "<tr><td colspan='2'>No subjects assigned yet</td></tr>";
}

// ─── LOAD CREATE SESSION PAGE ───
async function loadCreateSession() {
    const classes  = await fetch(API + "/classes/").then(r => r.json());
    const subjects = await fetch(API + "/subjects/teacher/" + userId).then(r => r.json());
    const sessions = await fetch(API + "/attendance-sessions/").then(r => r.json());

    // Fill class dropdown
    const classSel = document.getElementById("ses-class");
    classSel.innerHTML = '<option value="">Select Class</option>';
    for (let c of classes) {
        classSel.innerHTML += `<option value="${c.class_id}">
            ${c.class_name} - ${c.section}
        </option>`;
    }

    // Fill subject dropdown with MY subjects only
    const subSel = document.getElementById("ses-subject");
    subSel.innerHTML = '<option value="">Select Subject</option>';
    for (let s of subjects) {
        subSel.innerHTML += `<option value="${s.subject_id}">
            ${s.subject_name}
        </option>`;
    }

    // Show MY sessions only
    const mySessions = sessions.filter(s => s.teacher_id === userId);
    let rows = "";
    for (let s of mySessions) {
        const cls = classes.find(c => c.class_id === s.class_id);
        const sub = subjects.find(sub => sub.subject_id === s.subject_id);
        rows += `<tr>
            <td>${s.session_id}</td>
            <td>${cls ? cls.class_name + " " + cls.section : s.class_id}</td>
            <td>${sub ? sub.subject_name : s.subject_id}</td>
            <td>${s.date}</td>
            <td>${s.period}</td>
        </tr>`;
    }
    document.getElementById("my-sessions").innerHTML =
        rows || "<tr><td colspan='5'>No sessions created yet</td></tr>";
}

// ─── CREATE SESSION ───
async function createSession() {
    const classId   = document.getElementById("ses-class").value;
    const subjectId = document.getElementById("ses-subject").value;
    const date      = document.getElementById("ses-date").value;
    const period    = document.getElementById("ses-period").value;

    if (!classId || !subjectId || !date || !period) {
        showMsg("session-msg", "Please fill all fields!", "error");
        return;
    }

    const res = await fetch(API + "/attendance-sessions/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            class_id   : parseInt(classId),
            subject_id : parseInt(subjectId),
            teacher_id : userId,
            date       : date,
            period     : parseInt(period)
        })
    });

    if (res.ok) {
        showMsg("session-msg", "✅ Session created!", "success");
        loadCreateSession();
    } else {
        showMsg("session-msg", "❌ Error creating session!", "error");
    }
}

// ─── LOAD MARK ATTENDANCE ───
async function loadMarkAttendance() {
    const sessions = await fetch(API + "/attendance-sessions/").then(r => r.json());

    // Show MY sessions only
    const mySessions = sessions.filter(s => s.teacher_id === userId);

    const sesSel = document.getElementById("att-session");
    sesSel.innerHTML = '<option value="">Select Session</option>';
    for (let s of mySessions) {
        sesSel.innerHTML += `<option value="${s.session_id}">
            Session ${s.session_id} - ${s.date} - Period ${s.period}
        </option>`;
    }
}

// ─── LOAD STUDENTS FOR SESSION ───
async function loadStudentsForSession() {
    const sessionId = document.getElementById("att-session").value;
    if (!sessionId) return;

    // Get session details
    const session  = await fetch(API + "/attendance-sessions/" + sessionId).then(r => r.json());

    // Get students in that class
    const students = await fetch(API + "/students/class/" + session.class_id).then(r => r.json());

    // Get existing attendance for this session
    const existing = await fetch(API + "/attendance/session/" + sessionId).then(r => r.json());

    let rows = "";
    for (let s of students) {
        // Check if attendance already marked
        const alreadyMarked = existing.find(a => a.student_id === s.student_id);
        const status = alreadyMarked ? alreadyMarked.status : "";

        rows += `<tr>
            <td>${s.roll_number}</td>
            <td>${s.name}</td>
            <td>
                <select id="status-${s.student_id}">
                    <option value="">Select</option>
                    <option value="Present" ${status === "Present" ? "selected" : ""}>✅ Present</option>
                    <option value="Absent"  ${status === "Absent"  ? "selected" : ""}>❌ Absent</option>
                    <option value="Late"    ${status === "Late"    ? "selected" : ""}>⏰ Late</option>
                </select>
            </td>
        </tr>`;
    }

    document.getElementById("students-to-mark").innerHTML = rows;
    document.getElementById("student-att-table").style.display = "table";
    document.getElementById("submit-att-btn").style.display   = "block";

    // Store students list for submission
    window.currentStudents = students;
    window.currentSessionId = sessionId;
}

// ─── SUBMIT ATTENDANCE ───
async function submitAttendance() {
    const sessionId = window.currentSessionId;
    const students  = window.currentStudents;

    let successCount = 0;
    let errorCount   = 0;

    for (let s of students) {
        const status = document.getElementById("status-" + s.student_id).value;
        if (!status) continue;

        const res = await fetch(API + "/attendance/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                session_id : parseInt(sessionId),
                student_id : s.student_id,
                status     : status
            })
        });

        if (res.ok) {
            successCount++;
        } else {
            errorCount++;
        }
    }

    if (successCount > 0) {
        showMsg("att-msg",
            `✅ Attendance marked for ${successCount} students!`, "success");
    }
    if (errorCount > 0) {
        showMsg("att-msg",
            `⚠️ ${errorCount} records already exist!`, "error");
    }
}

// Load profile on start
loadProfile();
loadMySubjects();