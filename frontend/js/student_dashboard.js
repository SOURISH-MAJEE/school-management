const API = "http://127.0.0.1:8000";

// Check login
const userType = localStorage.getItem("user_type");
const userId   = parseInt(localStorage.getItem("user_id"));
const userName = localStorage.getItem("user_name");

if (!userType || userType !== "student") {
    alert("Please login as student first!");
    window.location.href = "login.html";
}

// Show name
document.getElementById("student-name").innerText = userName;

// Logout
function logout() {
    localStorage.clear();
    window.location.href = "login.html";
}

async function loadProfile() {
    const res     = await fetch(API + "/students/" + userId);
    const student = await res.json();

    // Get class info
    const classRes  = await fetch(API + "/classes/" + student.class_id);
    const classData = await classRes.json();

    document.getElementById("student-roll").innerText =
        "Roll Number: " + student.roll_number;

    document.getElementById("student-profile").innerHTML = `<tr>
        <td>${student.roll_number}</td>
        <td>${student.name}</td>
        <td>${student.age}</td>
        <td>${student.gender}</td>
        <td>${student.phone || "-"}</td>
        <td>${classData.class_name} - ${classData.section}</td>
    </tr>`;
}

async function loadAttendance() {
    const records  = await fetch(API + "/attendance/student/" + userId).then(r => r.json());
    const sessions = await fetch(API + "/attendance-sessions/").then(r => r.json());
    const subjects = await fetch(API + "/subjects/").then(r => r.json());

    // Count attendance
    let present = 0;
    let absent  = 0;
    let late    = 0;

    let rows = "";
    for (let a of records) {
        // Get session details
        const session = sessions.find(s => s.session_id === a.session_id);
        const subject = session
            ? subjects.find(sub => sub.subject_id === session.subject_id)
            : null;

        // Count
        if (a.status === "Present") present++;
        if (a.status === "Absent")  absent++;
        if (a.status === "Late")    late++;

        // Color for status
        const color = a.status === "Present" ? "green" :
                      a.status === "Absent"  ? "red"   : "orange";

        rows += `<tr>
            <td>${session ? session.date   : "-"}</td>
            <td>${subject ? subject.subject_name : "-"}</td>
            <td>${session ? "Period " + session.period : "-"}</td>
            <td style="color:${color}; font-weight:bold">
                ${a.status}
            </td>
        </tr>`;
    }

    // Update summary counts
    document.getElementById("present-count").innerText = present;
    document.getElementById("absent-count").innerText  = absent;
    document.getElementById("late-count").innerText    = late;
    document.getElementById("total-count").innerText   = records.length;

    // Update table
    document.getElementById("attendance-records").innerHTML =
        rows || "<tr><td colspan='4'>No attendance records yet</td></tr>";
}

// Load everything
loadProfile();
loadAttendance();