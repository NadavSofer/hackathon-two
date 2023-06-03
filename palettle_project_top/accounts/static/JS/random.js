

//http://127.0.0.1:8000/api/endpoint/




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