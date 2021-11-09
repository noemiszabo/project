var plantList = document.getElementById('plantList');

fetch('/inventory', {
    method: 'GET'
}).then(response => response.json()).then(response => plantList.innerText = response.items);

