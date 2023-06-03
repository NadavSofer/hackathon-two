(function makePalette() {
    let makePalette = document.getElementById('makePalette-container');
    for (let i = 0; i < 5; i++) {
        let makePalette_container = document.createElement('div');
        makePalette_container.classList.add('makePalette-container')

        let box = document.createElement('div');
        box.classList.add('box');
        box.style.width = '5rem';
        box.style.height = '5rem';
        

        let input = document.createElement('input');
        input.setAttribute('type', 'color');

        input.addEventListener('input', ()=>{
            console.log(input.value);
            box.style.backgroundColor = input.value;
        })

        makePalette_container.appendChild(box);
        makePalette_container.appendChild(input);
        makePalette.appendChild(makePalette_container);
    }
})()

const getAPI = async ()=>{
    try {
        let url = await fetch('http://127.0.0.1:8000/api/endpoint/');
        let response = await url.json();
        return response
    } catch (error) {
        throw new Error(error);
    }
}

const renderAPI = (arr) => {
    let randomPalette = document.getElementById('randomPalette-container');
    randomPalette.innerHTML = ''
    delete arr.pk
    for (const color of Object.values(arr)) {
        let color_container = document.createElement('div');
        color_container.classList.add('color-container');

        let box = document.createElement('div');
        box.classList.add('box');
        box.style.width = '5rem';
        box.style.height = '5rem';
        box.style.backgroundColor = color;

        let p = document.createElement('p');
        p.innerText = color

        color_container.appendChild(box)
        color_container.appendChild(p)
        randomPalette.appendChild(color_container)
        console.log(color);
    }
}

getAPI()
.then((res)=> {
    let random_num = Math.floor(Math.random() * res.length);
    renderAPI(res[random_num]);
})

let randomGenerateButton = document.getElementById('random-generate');
randomGenerateButton.innerText = 'generate'

randomGenerateButton.addEventListener('click', ()=>{
    let randomPalette = document.getElementById('randomPalette-container');
    randomPalette.innerHTML = '<i class="fas fa-spinner fa-pulse"></i>'
    getAPI()
    .then((res)=> {
        let random_num = Math.floor(Math.random() * res.length);
        renderAPI(res[random_num]);
})
})