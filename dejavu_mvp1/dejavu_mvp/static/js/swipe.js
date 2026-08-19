(function () {
  const stage = document.getElementById("swipe-stage");
  if (!stage) return;

  const roomCode = stage.dataset.roomCode;
  const member = stage.dataset.member;

  function vote(placeId, liked) {
    const formData = new URLSearchParams();
    formData.append("member", member);
    formData.append("place_id", placeId);
    formData.append("liked", liked ? "1" : "0");

    fetch(`/swipe/${roomCode}/vote`, {
      method: "POST",
      headers: { "Content-Type": "application/x-www-form-urlencoded" },
      body: formData.toString(),
    })
      .then((res) => res.json())
      .then((data) => {
        const url = new URL(window.location.href);
        url.searchParams.set("member", member);
        window.location.href = url.toString();
      })
      .catch(() => {
        // fail gracefully: reload to re-sync state
        window.location.reload();
      });
  }

  function bindCard() {
    const card = document.getElementById("active-card");
    const btnLike = document.getElementById("btn-like");
    const btnPass = document.getElementById("btn-pass");
    if (!card) return;

    const placeId = card.dataset.placeId;

    function animateOut(direction) {
      card.classList.add(direction === "right" ? "swiping-right" : "swiping-left");
    }

    if (btnLike) {
      btnLike.addEventListener("click", () => {
        animateOut("right");
        setTimeout(() => vote(placeId, true), 220);
      });
    }
    if (btnPass) {
      btnPass.addEventListener("click", () => {
        animateOut("left");
        setTimeout(() => vote(placeId, false), 220);
      });
    }

    // Basic drag support
    let startX = 0;
    let currentX = 0;
    let dragging = false;

    function onStart(x) {
      dragging = true;
      startX = x;
      card.style.transition = "none";
    }
    function onMove(x) {
      if (!dragging) return;
      currentX = x - startX;
      card.style.transform = `translateX(${currentX}px) rotate(${currentX / 20}deg)`;
    }
    function onEnd() {
      if (!dragging) return;
      dragging = false;
      card.style.transition = "";
      if (currentX > 100) {
        animateOut("right");
        setTimeout(() => vote(placeId, true), 220);
      } else if (currentX < -100) {
        animateOut("left");
        setTimeout(() => vote(placeId, false), 220);
      } else {
        card.style.transform = "";
      }
      currentX = 0;
    }

    card.addEventListener("mousedown", (e) => onStart(e.clientX));
    window.addEventListener("mousemove", (e) => onMove(e.clientX));
    window.addEventListener("mouseup", onEnd);

    card.addEventListener("touchstart", (e) => onStart(e.touches[0].clientX));
    card.addEventListener("touchmove", (e) => onMove(e.touches[0].clientX));
    card.addEventListener("touchend", onEnd);
  }

  bindCard();
})();
