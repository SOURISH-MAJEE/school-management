const API = "http://127.0.0.1:8000";

function showMsg(id, text, type) {
    const el = document.getElementById(id);
    el.innerText = text;
    el.className = "msg " + type;
    el.style.display = "block";
    setTimeout(() => el.style.display = "none", 3000);
}

async function loadClasses() {
    const data = await fetch(API + "/classes/").then(r => r.json());
    let rows = "";
    for (let c of data) {
        rows += `<tr>
            <td>${c.class_id}</td>
            <td>${c.class_name}</td>
            <td>${c.section}</td>
            <td><button class="btn-red" onclick="deleteClass(${c.class_id})">Delete</button></td>
        </tr>`;
    }
    document.getElementById("c-list").innerHTML = rows;
}

async function addClass() {
    const name    = document.getElementById("c-name").value;
    const section = document.getElementById("c-section").value;
    if (!name || !section) {
        showMsg("c-msg", "Please fill all fields!", "error");
        return;
    }
    const res = await fetch(API + "/classes/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ class_name: name, section: section })
    });
    if (res.ok) {
        showMsg("c-msg", "Class added!", "success");
        document.getElementById("c-name").value = "";
        document.getElementById("c-section").value = "";
        loadClasses();
    } else {
        showMsg("c-msg", "Error adding class!", "error");
    }
}

async function deleteClass(id) {
    if (!confirm("Delete this class?")) return;
    const res = await fetch(API + "/classes/" + id, { method: "DELETE" });
    if (res.ok) {
        showMsg("c-msg", "Class deleted!", "success");
        loadClasses();
    } else {
        showMsg("c-msg", "Cannot delete!", "error");
    }
}

loadClasses();