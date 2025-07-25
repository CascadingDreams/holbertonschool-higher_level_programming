const addListItem = document.getElementById("add_item");
const list = document.querySelector(".my_list");

addListItem.addEventListener('click', function () {
    const newListItem = document.createElement("li");
    newListItem.textContent = "Item";
    list.appendChild(newListItem);
});