const API = "http://127.0.0.1:8000";

function showMsg(id, text, type) {
    const el = document.getElementById(id);
    el.innerText = text;
    el.className = "msg " + type;
    el.style.display = "block";
    setTimeout(() => el.style.display = "none", 3000);
}

async function loadTeachers() {
    const data = await fetch(API + "/teachers/").then(r => r.json());
    let rows = "";
    for (let t of data) {
        rows += `<tr>
            <td>${t.teacher_id}</td>
            <td>${t.name}</td>
            <td>${t.age}</td>
            <td>${t.gender}</td>
            <td>${t.email}</td>
            <td>${t.phone}</td>
            <td><button class="btn-red" onclick="deleteTeacher(${t.teacher_id})">Delete</button></td>
        </tr>`;
    }
    document.getElementById("t-list").innerHTML = rows;
}

async function addTeacher() {
    const name   = document.getElementById("t-name").value;
    const age    = document.getElementById("t-age").value;
    const gender = document.getElementById("t-gender").value;
    const email  = document.getElementById("t-email").value;
    const phone  = document.getElementById("t-phone").value;

    if (!name || !age || !gender || !email || !phone) {
        showMsg("t-msg", "Please fill all fields!", "error");
        return;
    }

    const res = await fetch(API + "/teachers/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            name: name,
            age: parseInt(age),
            gender: gender,
            email: email,
            phone: phone
        })
    });

    if (res.ok) {
        showMsg("t-msg", "Teacher added successfully!", "success");
        document.getElementById("t-name").value = "";
        document.getElementById("t-age").value = "";
        document.getElementById("t-gender").value = "";
        document.getElementById("t-email").value = "";
        document.getElementById("t-phone").value = "";
        loadTeachers();
    } else {
        showMsg("t-msg", "Error! Email may already exist.", "error");
    }
}

async function deleteTeacher(id) {
    if (!confirm("Delete this teacher?")) return;
    const res = await fetch(API + "/teachers/" + id, { method: "DELETE" });
    if (res.ok) {
        showMsg("t-msg", "Teacher deleted!", "success");
        loadTeachers();
    } else {
        showMsg("t-msg", "Cannot delete!", "error");
    }
}

loadTeachers();