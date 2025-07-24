
const redHeader = document.getElementById('red_header');
const headerEle = document.querySelector('header');
redHeader.addEventListener('click', function () {
  headerEle.classList.add('red');
});
