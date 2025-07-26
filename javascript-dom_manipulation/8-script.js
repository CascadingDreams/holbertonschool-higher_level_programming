
document.addEventListener('DOMContentLoaded', function () {
    fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
        .then(function (response) {
            return response.json()
        })
        .then(function (jsonData) {
            console.log(jsonData)
            const helloMsg = document.getElementById('hello');
            helloMsg.textContent = jsonData.hello;
        });
});

