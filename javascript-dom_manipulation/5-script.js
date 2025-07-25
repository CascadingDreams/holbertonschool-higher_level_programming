const upHeader = document.getElementById("update_header");
const newHeader = document.querySelector("header");

upHeader.addEventListener('click', function () {
    newHeader.textContent = "New Header!!!";
});