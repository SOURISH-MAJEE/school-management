const API = "http://127.0.0.1:8000";

function showMsg(id, text, type) {
    const el = document.getElementById(id);
    el.innerText = text;
    el.className = "msg " + type;
    el.style.display = "block";
    setTimeout(() => el.style.display = "none", 3000);
}

async function loadStudents() {
    const students = await fetch(API + "/students/").then(r => r.json());
    const classes  = await fetch(API + "/classes/").then(r => r.json());

    const sel = document.getElementById("s-class");
    sel.innerHTML = '<option value="">Select Class</option>';
    for (let c of classes) {
        sel.innerHTML += `<option value="${c.class_id}">${c.class_name} - ${c.section}</option>`;
    }

    let rows = "";
    for (let s of students) {
        const cls = classes.find(c => c.class_id === s.class_id);
        rows += `<tr>
            <td>${s.roll_number}</td>
            <td>${s.name}</td>
            <td>${s.age}</td>
            <td>${s.gender}</td>
            <td>${s.phone || "-"}</td>
            <td>${cls ? cls.class_name + " " + cls.section : "-"}</td>
            <td><button class="btn-red" onclick="deleteStudent(${s.student_id})">Delete</button></td>
        </tr>`;
    }
    document.getElementById("s-list").innerHTML = rows;
}

async function addStudent() {
    const roll    = document.getElementById("s-roll").value;
    const name    = document.getElementById("s-name").value;
    const age     = document.getElementById("s-age").value;
    const gender  = document.getElementById("s-gender").value;
    const phone   = document.getElementById("s-phone").value;
    const classId = document.getElementById("s-class").value;

    if (!roll || !name || !age || !gender || !classId) {
        showMsg("s-msg", "Please fill all fields!", "error");
        return;
    }

    const res = await fetch(API + "/students/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            roll_number: roll,
            name: name,
            age: parseInt(age),
            gender: gender,
            phone: phone,
            class_id: parseInt(classId)
        })
    });

    if (res.ok) {
        showMsg("s-msg", "Student added!", "success");
        document.getElementById("s-roll").value = "";
        document.getElementById("s-name").value = "";
        document.getElementById("s-age").value = "";
        document.getElementById("s-gender").value = "";
        document.getElementById("s-phone").value = "";
        loadStudents();
    } else {
        showMsg("s-msg", "Error! Roll number may already exist.", "error");
    }
}

async function deleteStudent(id) {
    if (!confirm("Delete this student?")) return;
    const res = await fetch(API + "/students/" + id, { method: "DELETE" });
    if (res.ok) {
        showMsg("s-msg", "Student deleted!", "success");
        loadStudents();
    } else {
        showMsg("s-msg", "Cannot delete!", "error");
    }
}

loadStudents();