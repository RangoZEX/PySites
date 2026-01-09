/* =========================================================
   BOOK ENGINE — PAGE NAVIGATION CORE
   ========================================================= */

document.addEventListener("DOMContentLoaded", () => {
  const pages = Array.from(document.querySelectorAll(".page"));
  let current = 0;
  let isAnimating = false;

  if (!pages.length) return;

  /* INITIAL STATE */
  pages.forEach((page, index) => {
    if (index === 0) {
      page.classList.add("active");
    } else {
      page.classList.remove("active", "turned");
    }
  });

  /* ---------------------------------------------------------
     TURN NEXT PAGE
     --------------------------------------------------------- */
  function turnNext() {
    if (isAnimating) return;
    if (current >= pages.length - 1) return;

    isAnimating = true;

    const currentPage = pages[current];
    currentPage.classList.add("turned");
    currentPage.classList.remove("active");

    current += 1;

    const nextPage = pages[current];
    nextPage.classList.add("active");

    setTimeout(() => {
      isAnimating = false;
    }, 1200);
  }

  /* ---------------------------------------------------------
     TURN PREVIOUS PAGE
     --------------------------------------------------------- */
  function turnPrev() {
    if (isAnimating) return;
    if (current <= 0) return;

    isAnimating = true;

    const currentPage = pages[current];
    currentPage.classList.remove("active");

    current -= 1;

    const prevPage = pages[current];
    prevPage.classList.remove("turned");
    prevPage.classList.add("active");

    setTimeout(() => {
      isAnimating = false;
    }, 1200);
  }

  /* ---------------------------------------------------------
     CLICK CONTROL
     --------------------------------------------------------- */
  document.addEventListener("click", (e) => {
    // Ignore clicks on interactive elements later
    turnNext();
  });

  /* ---------------------------------------------------------
     KEYBOARD CONTROL
     --------------------------------------------------------- */
  document.addEventListener("keydown", (e) => {
    if (e.key === "ArrowRight") {
      turnNext();
    }

    if (e.key === "ArrowLeft") {
      turnPrev();
    }
  });

  /* ---------------------------------------------------------
     TOUCH SUPPORT (MOBILE)
     --------------------------------------------------------- */
  let touchStartX = null;

  document.addEventListener("touchstart", (e) => {
    touchStartX = e.changedTouches[0].screenX;
  });

  document.addEventListener("touchend", (e) => {
    if (touchStartX === null) return;

    const touchEndX = e.changedTouches[0].screenX;
    const deltaX = touchEndX - touchStartX;

    if (deltaX < -60) {
      turnNext();
    } else if (deltaX > 60) {
      turnPrev();
    }

    touchStartX = null;
  });
});
