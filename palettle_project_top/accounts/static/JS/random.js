// Function to create the color palette
(function makePalette() {
    // Get the container element
    let makePalette = document.getElementById('makePalette-outer-container');

    // Loop to create 5 color palette containers
    for (let i = 0; i < 5; i++) {
        let makePalette_container = document.createElement('div');
        makePalette_container.classList.add('makePalette-inner-container');

        let box = document.createElement('div');
        box.classList.add('box');

        let p = document.createElement('p');
        p.innerText = '#000000';

        let input = document.createElement('input');
        input.setAttribute('type', 'color');

        // Event listener to update color on input change
        input.addEventListener('input', () => {
            console.log(input.value);
            box.style.backgroundColor = input.value;
            p.innerText = input.value;
        });

        // Append elements to the container
        makePalette_container.appendChild(box);
        makePalette_container.appendChild(p);
        makePalette_container.appendChild(input);
        makePalette.appendChild(makePalette_container);
    }
})();

// Function to fetch data from the API
const getAPI = async () => {
    try {
        let url = await fetch('http://127.0.0.1:8000/api/endpoint/');
        let response = await url.json();
        return response;
    } catch (error) {
        throw new Error(error);
    }
};

// Function to render API response data
const renderAPI = (arr) => {
    let randomPalette = document.getElementById('randomPalette-container');
    randomPalette.innerHTML = '';
    delete arr.pk
    // Loop through the colors in the response object
    for (const color of Object.values(arr)) {
        let color_container = document.createElement('div');
        color_container.classList.add('color-container');

        let box = document.createElement('div');
        box.classList.add('box');
        box.style.backgroundColor = color;

        let p = document.createElement('p');
        p.innerText = color;

        // Append elements to the container
        color_container.appendChild(box);
        color_container.appendChild(p);
        randomPalette.appendChild(color_container);
        console.log(color);
    }
};

// Fetch data from the API and render a random color palette
getAPI().then((res) => {
    let random_num = Math.floor(Math.random() * res.length);
    renderAPI(res[random_num]);
});

// Event listener for the "Generate" button
let randomGenerateButton = document.getElementById('random-generate');
randomGenerateButton.innerText = 'generate';

randomGenerateButton.addEventListener('click', () => {
    let randomPalette = document.getElementById('randomPalette-container');
    randomPalette.innerHTML = '<i class="fas fa-spinner fa-pulse"></i>';

    // Fetch data from the API and render a random color palette
    getAPI().then((res) => {
        let random_num = Math.floor(Math.random() * res.length);
        renderAPI(res[random_num]);
    });
});
