const API = "http://127.0.0.1:8000";

function switchUser(type, btn) {
    document.getElementById("teacher-section").style.display = "none";
    document.getElementById("student-section").style.display = "none";
    document.querySelectorAll(".user-tab").forEach(b => b.classList.remove("active"));
    document.getElementById(type + "-section").style.display = "block";
    btn.classList.add("active");

    // Load classes for student signup
    if (type === "student") loadClasses();
}

function switchAction(user, action, btn) {
    document.getElementById(user + "-login").classList.remove("active");
    document.getElementById(user + "-signup").classList.remove("active");
    btn.parentElement.querySelectorAll(".action-tab")
        .forEach(b => b.classList.remove("active"));
    document.getElementById(user + "-" + action).classList.add("active");
    btn.classList.add("active");
}

function showMsg(id, text, type) {
    const el = document.getElementById(id);
    el.innerText = text;
    el.className = "msg " + type;
    el.style.display = "block";
    setTimeout(() => el.style.display = "none", 3000);
}

async function loadClasses() {
    const classes = await fetch(API + "/classes/").then(r => r.json());
    const sel = document.getElementById("ss-class");
    sel.innerHTML = '<option value="">Select Class</option>';
    for (let c of classes) {
        sel.innerHTML += `<option value="${c.class_id}">
            ${c.class_name} - ${c.section}
        </option>`;
    }
}

async function teacherLogin() {
    const email    = document.getElementById("tl-email").value;
    const password = document.getElementById("tl-password").value;

    if (!email || !password) {
        showMsg("t-login-msg", "Please fill all fields!", "error");
        return;
    }

    try {
        const res = await fetch(API + "/auth/teacher-login", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ email, password })
        });

        if (res.ok) {
            const data = await res.json();
            localStorage.setItem("user_type", "teacher");
            localStorage.setItem("user_id",   data.user_id);
            localStorage.setItem("user_name",  data.name);
            window.location.href = "teacher_dashboard.html";
        } else {
            showMsg("t-login-msg", "Wrong email or password!", "error");
        }
    } catch(err) {
        showMsg("t-login-msg", "Server not connected!", "error");
    }
}
async function teacherSignup() {
    const name     = document.getElementById("ts-name").value;
    const age      = document.getElementById("ts-age").value;
    const gender   = document.getElementById("ts-gender").value;
    const email    = document.getElementById("ts-email").value;
    const phone    = document.getElementById("ts-phone").value;
    const password = document.getElementById("ts-password").value;
    const confirm  = document.getElementById("ts-confirm").value;

    // Check all fields
    if (!name || !age || !gender || !email || !phone || !password) {
        showMsg("t-signup-msg", "Please fill all fields!", "error");
        return;
    }

    // Check passwords match
    if (password !== confirm) {
        showMsg("t-signup-msg", "Passwords do not match!", "error");
        return;
    }

    try {
        const res = await fetch(API + "/teachers/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                name     : name,
                age      : parseInt(age),
                gender   : gender,
                email    : email,
                phone    : phone,
                password : password
            })
        });

        if (res.ok) {
            const data = await res.json();
            showMsg("t-signup-msg",
                "Account created! Please login.", "success");

            // Clear form
            document.getElementById("ts-name").value     = "";
            document.getElementById("ts-age").value      = "";
            document.getElementById("ts-gender").value   = "";
            document.getElementById("ts-email").value    = "";
            document.getElementById("ts-phone").value    = "";
            document.getElementById("ts-password").value = "";
            document.getElementById("ts-confirm").value  = "";

            // Switch to login tab after 2 seconds
            setTimeout(() => {
                switchAction("teacher", "login",
                    document.querySelector("#teacher-section .action-tab"));
            }, 2000);

        } else {
            showMsg("t-signup-msg",
                "Error! Email may already exist.", "error");
        }
    } catch(err) {
        showMsg("t-signup-msg", "Server not connected!", "error");
    }
}

// STUDENT LOGIN 
async function studentLogin() {
    const roll     = document.getElementById("sl-roll").value;
    const password = document.getElementById("sl-password").value;

    if (!roll || !password) {
        showMsg("s-login-msg", "Please fill all fields!", "error");
        return;
    }

    try {
        const res = await fetch(API + "/auth/student-login", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ roll_number: roll, password })
        });

        if (res.ok) {
            const data = await res.json();
            localStorage.setItem("user_type", "student");
            localStorage.setItem("user_id",   data.user_id);
            localStorage.setItem("user_name",  data.name);
            window.location.href = "student_dashboard.html";
        } else {
            showMsg("s-login-msg",
                "Wrong roll number or password!", "error");
        }
    } catch(err) {
        showMsg("s-login-msg", "Server not connected!", "error");
    }
}

// ─── STUDENT SIGN UP ───
async function studentSignup() {
    const roll     = document.getElementById("ss-roll").value;
    const name     = document.getElementById("ss-name").value;
    const age      = document.getElementById("ss-age").value;
    const gender   = document.getElementById("ss-gender").value;
    const phone    = document.getElementById("ss-phone").value;
    const classId  = document.getElementById("ss-class").value;
    const password = document.getElementById("ss-password").value;
    const confirm  = document.getElementById("ss-confirm").value;

    // Check all fields
    if (!roll || !name || !age || !gender || !classId || !password) {
        showMsg("s-signup-msg", "Please fill all fields!", "error");
        return;
    }

    // Check passwords match
    if (password !== confirm) {
        showMsg("s-signup-msg", "Passwords do not match!", "error");
        return;
    }

    try {
        const res = await fetch(API + "/students/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                roll_number : roll,
                name        : name,
                age         : parseInt(age),
                gender      : gender,
                phone       : phone,
                class_id    : parseInt(classId),
                password    : password
            })
        });

        if (res.ok) {
            showMsg("s-signup-msg",
                "Account created! Please login.", "success");

            // Clear form
            document.getElementById("ss-roll").value     = "";
            document.getElementById("ss-name").value     = "";
            document.getElementById("ss-age").value      = "";
            document.getElementById("ss-gender").value   = "";
            document.getElementById("ss-phone").value    = "";
            document.getElementById("ss-class").value    = "";
            document.getElementById("ss-password").value = "";
            document.getElementById("ss-confirm").value  = "";

            // Switch to login tab after 2 seconds
            setTimeout(() => {
                switchAction("student", "login",
                    document.querySelector("#student-section .action-tab"));
            }, 2000);

        } else {
            showMsg("s-signup-msg",
                "Error! Roll number may already exist.", "error");
        }
    } catch(err) {
        showMsg("s-signup-msg", "Server not connected!", "error");
    }
}

// Load classes on page load
loadClasses();