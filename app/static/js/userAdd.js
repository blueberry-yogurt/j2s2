const $ = (s) => document.querySelector(s);

const form = $(".userJoinForm");
const message = $(".checkMessage");

const pw = $(".userPw");
const pw2 = $(".userPw2");

const rule = /^(?=.*[a-zA-Z])(?=.*\d)(?=.*[!@#$%^&*?_]).{8,30}$/;

function validatePassword() {
  if (!rule.test(pw.value)) {
    pw.setCustomValidity(
      "비밀번호는 영문, 숫자, 특수문자를 포함한 8~30자여야 합니다."
    );
  } else {
    pw.setCustomValidity("");
  }

  if (pw.value !== pw2.value) {
    pw2.setCustomValidity("비밀번호가 일치하지 않습니다.");
  } else {
    pw2.setCustomValidity("");
  }
}

pw.addEventListener("input", validatePassword);
pw2.addEventListener("input", validatePassword);

$(".userJoin").addEventListener("click", async () => {
  validatePassword();

  if (!form.checkValidity()) {
    form.reportValidity();
    return;
  }

  const payload = {
    user_id: $(".userId").value,
    password: pw.value,
    name: $(".userName").value,
    phone: $(".userPhone").value,
    gender: document.querySelector("input[name='gender']:checked").value,
    email: $(".userEmail").value,
  };

  try {
    const res = await fetch("/api/v1/users", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(payload),
    });

    const data = await res.json();

    if (!res.ok) {
      throw new Error(data.detail || "회원가입 실패");
    }

    alert(data.message);
    window.location.href = "/login.html";

  } catch (err) {
    message.textContent = err.message;
  }
});
