fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        console.log('Success:', data);

        const filmTitles = document.getElementById("list_movies");
        //loop through array
        data.results.forEach(item => {
            const newListItem = document.createElement('li');
            newListItem.textContent = item.title;
            filmTitles.appendChild(newListItem);
        })
    })

    .catch(error => {
        console.error('Error:', error);
    });
