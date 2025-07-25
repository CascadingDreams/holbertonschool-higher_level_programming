
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        console.log('Success:', data);

        const charID = document.getElementById("character");
        charID.textContent = data.name;
    })
    .catch(error => {
        console.error('Error:', error);
    });
