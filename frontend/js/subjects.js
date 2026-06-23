const API = "http://127.0.0.1:8000";

function showMsg(id, text, type) {
    const el = document.getElementById(id);
    el.innerText = text;
    el.className = "msg " + type;
    el.style.display = "block";
    setTimeout(() => el.style.display = "none", 3000);
}

async function loadSubjects() {
    const data = await fetch(API + "/subjects/").then(r => r.json());
    let rows = "";
    for (let s of data) {
        rows += `<tr>
            <td>${s.subject_id}</td>
            <td>${s.subject_name}</td>
            <td><button class="btn-red" onclick="deleteSubject(${s.subject_id})">Delete</button></td>
        </tr>`;
    }
    document.getElementById("sub-list").innerHTML = rows;
}

async function addSubject() {
    const name = document.getElementById("sub-name").value;
    if (!name) {
        showMsg("sub-msg", "Please enter subject name!", "error");
        return;
    }
    const res = await fetch(API + "/subjects/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ subject_name: name })
    });
    if (res.ok) {
        showMsg("sub-msg", "Subject added!", "success");
        document.getElementById("sub-name").value = "";
        loadSubjects();
    } else {
        showMsg("sub-msg", "Error adding subject!", "error");
    }
}

async function deleteSubject(id) {
    if (!confirm("Delete this subject?")) return;
    const res = await fetch(API + "/subjects/" + id, { method: "DELETE" });
    if (res.ok) {
        showMsg("sub-msg", "Subject deleted!", "success");
        loadSubjects();
    } else {
        showMsg("sub-msg", "Cannot delete!", "error");
    }
}

loadSubjects();