
const greenHeader = document.querySelector('.green');
const toggle = document.getElementById('toggle_header');

toggle.addEventListener('click', function () {
  if (greenHeader.classList.contains('red')) {
    greenHeader.classList.remove('red');
    greenHeader.classList.toggle('green');
    console.log('green');
  } else {
    greenHeader.classList.remove('green');
    greenHeader.classList.toggle('red');
    console.log('red');
  }
});
