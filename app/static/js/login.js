const $ = (s) => document.querySelector(s);

const form = $(".loginForm");
const message = $(".message");

$(".loginBtn").addEventListener("click", async () => {
  if (!form.checkValidity()) {
    form.reportValidity();
    return;
  }

  const payload = {
    username: $(".userName").value,
    password: $(".userPw").value,
  };

  try {
    const res = await fetch("/api/v1/auth/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(payload),
    });

    if (!res.ok) {
      throw new Error("Login failed");
    }
    console.log("payload:", payload);
    const data = await res.json();

    //JWT 토큰 저장
    localStorage.setItem("access_token", data.access_token);
    alert("로그인 성공!");
    window.location.href = "main.html";

  } catch (err) {
    message.textContent = "아이디 또는 비밀번호가 올바르지 않습니다.";
  }
});
