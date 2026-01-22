window.addEventListener("DOMContentLoaded", () => {
  const audio = document.getElementById("bgm");
  if (!audio) {
    console.log("[BGM] audio element #bgm not found");
    return;
  }

  audio.volume = 0.25;

  const start = async () => {
    try {
      await audio.play();
      console.log("[BGM] playing");
      document.removeEventListener("click", start);
      document.removeEventListener("keydown", start);
    } catch (e) {
      console.log("[BGM] play blocked:", e);
    }
  };

  // 브라우저 정책상 “유저 액션 후”에만 재생 가능
  document.addEventListener("click", start, { once: true });
  document.addEventListener("keydown", start, { once: true });
});

