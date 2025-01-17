function toggleMode() {
    const body = document.body;
    body.classList.toggle("dark-mode");
    body.classList.toggle("light-mode");
    const button = document.querySelector(".mode-toggle");
    if (body.classList.contains("dark-mode")) {
        button.innerHTML = "Eye Saver";
        localStorage.setItem("mode", "dark");
    } else {
        button.innerHTML = "Eye Burner";
        localStorage.setItem("mode", "light");
    }
}

function applyStoredMode() {
    const storedMode = localStorage.getItem("mode");
    const body = document.body;
    const button = document.querySelector(".mode-toggle");
    if (storedMode === "light") {
        body.classList.add("light-mode");
        body.classList.remove("dark-mode");
        button.innerHTML = "Eye Burner";
    } else {
        body.classList.add("dark-mode");
        body.classList.remove("light-mode");
        button.innerHTML = "Eye Saver";
    }
}

document.addEventListener("DOMContentLoaded", applyStoredMode);