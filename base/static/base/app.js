const sidebar = document.getElementById("sidebar");
const brand = document.getElementById("brand");
const toggleButton = document.getElementById("menu-toggle");

toggleButton.onclick = function () {
    window.alert('toto');

    sidebar.classList.toggle("sidebar-mini");
    sidebar.classList.toggle("col-md-1");
    sidebar.classList.toggle("col-sm-2");
    sidebar.classList.toggle("col-3");

    sidebar.classList.toggle("col-lg-4");
    sidebar.classList.toggle("col-sm-5");
    sidebar.classList.toggle("col-6");

    brand.classList.toggle("sidebar-mini");
    brand.classList.toggle("col-md-1");
    brand.classList.toggle("col-sm-2");
    brand.classList.toggle("col-3");

    brand.classList.toggle("col-lg-4");
    brand.classList.toggle("col-sm-5");
    brand.classList.toggle("col-6");
};

document.getElementById("deco").onclick = function () {
    window.alert('deco');

}