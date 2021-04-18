const sidebar = document.getElementById("sidebar");
const toggleButton = document.getElementById("menu-toggle");

toggleButton.onclick = function () {
    sidebar.classList.toggle("sidebar-mini");
    sidebar.classList.toggle("col-md-1");
    sidebar.classList.toggle("col-sm-2");
    sidebar.classList.toggle("col-3");

    sidebar.classList.toggle("col-lg-4");
    sidebar.classList.toggle("col-sm-5");
    sidebar.classList.toggle("col-6");
};