const $ = (s) => document.querySelector(s);

const form = $(".loginForm");
const message = $(".message");

$(".loginBtn").addEventListener("click", async () => {
  if (!form.checkValidity()) {
    form.reportValidity();
    return;
  }

  const payload = {
    user_id: $(".userId").value,
    password: $(".userPw").value,
  };

  try {
    // 👉 FastAPI 로그인 API 연결 예정
    // const res = await fetch("/api/v1/auth/login", {
    //   method: "POST",
    //   headers: { "Content-Type": "application/json" },
    //   body: JSON.stringify(payload),
    // });

    // 임시 성공 처리
    console.log(payload);
    alert("로그인 성공!");
    window.location.href = "main.html";

  } catch (err) {
    message.textContent = "아이디 또는 비밀번호가 올바르지 않습니다.";
  }
});
