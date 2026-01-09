const toggle = document.getElementById("themeToggle");
const root = document.documentElement;

const saved = localStorage.getItem("theme") || "dark";
root.setAttribute("data-theme", saved);

toggle.onclick = () => {
  const next = root.getAttribute("data-theme") === "dark" ? "light" : "dark";
  root.setAttribute("data-theme", next);
  localStorage.setItem("theme", next);
};
