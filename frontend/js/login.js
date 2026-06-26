const API = "http://127.0.0.1:8000";

// Switch tab
function switchTab(type, btn) {
    document.getElementById("teacher-form").classList.remove("active");
    document.getElementById("student-form").classList.remove("active");
    document.querySelectorAll(".tab-btn").forEach(b => b.classList.remove("active"));
    document.getElementById(type + "-form").classList.add("active");
    btn.classList.add("active");
}

// Show message
function showMsg(id, text, type) {
    const el = document.getElementById(id);
    el.innerText = text;
    el.className = "msg " + type;
    el.style.display = "block";
}

// Teacher Login
async function teacherLogin() {
    const email    = document.getElementById("t-email").value;
    const password = document.getElementById("t-password").value;

    if (!email || !password) {
        showMsg("t-msg", "Please fill all fields!", "error");
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
            // Save to localStorage
            localStorage.setItem("user_type", "teacher");
            localStorage.setItem("user_id",   data.user_id);
            localStorage.setItem("user_name",  data.name);
            // Go to teacher dashboard
            window.location.href = "teacher_dashboard.html";
        } else {
            showMsg("t-msg", "Wrong email or password!", "error");
        }
    } catch(err) {
        showMsg("t-msg", "Server not connected!", "error");
    }
}

// Student Login
async function studentLogin() {
    const roll     = document.getElementById("s-roll").value;
    const password = document.getElementById("s-password").value;

    if (!roll || !password) {
        showMsg("s-msg", "Please fill all fields!", "error");
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
            // Save to localStorage
            localStorage.setItem("user_type", "student");
            localStorage.setItem("user_id",   data.user_id);
            localStorage.setItem("user_name",  data.name);
            // Go to student dashboard
            window.location.href = "student_dashboard.html";
        } else {
            showMsg("s-msg", "Wrong roll number or password!", "error");
        }
    } catch(err) {
        showMsg("s-msg", "Server not connected!", "error");
    }
}