window.addEventListener("load", () => {
  const loader = document.getElementById("ai-loader");

  setTimeout(() => {
    loader.style.opacity = "0";
    loader.style.pointerEvents = "none";

    setTimeout(() => {
      loader.remove();
      document.body.classList.add("booted");
    }, 800);

  }, 3200); // boot duration
});
