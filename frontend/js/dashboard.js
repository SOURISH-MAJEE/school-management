const API = "http://127.0.0.1:8000";

async function loadDashboard() {
    try {
        const teachers = await fetch(API + "/teachers/").then(r => r.json());
        const students = await fetch(API + "/students/").then(r => r.json());
        const subjects = await fetch(API + "/subjects/").then(r => r.json());
        const classes  = await fetch(API + "/classes/").then(r => r.json());

        document.getElementById("t-count").innerText   = teachers.length;
        document.getElementById("s-count").innerText   = students.length;
        document.getElementById("sub-count").innerText = subjects.length;
        document.getElementById("c-count").innerText   = classes.length;

        let tRows = "";
        for (let t of teachers) {
            tRows += `<tr>
                <td>${t.name}</td>
                <td>${t.age}</td>
                <td>${t.gender}</td>
                <td>${t.email}</td>
                <td>${t.phone}</td>
            </tr>`;
        }
        document.getElementById("d-teachers").innerHTML = tRows;

        let sRows = "";
        for (let s of students) {
            sRows += `<tr>
                <td>${s.roll_number}</td>
                <td>${s.name}</td>
                <td>${s.age}</td>
                <td>${s.gender}</td>
                <td>${s.phone || "-"}</td>
            </tr>`;
        }
        document.getElementById("d-students").innerHTML = sRows;

    } catch(err) {
        alert("Cannot connect to API! Make sure server is running.");
    }
}

loadDashboard();