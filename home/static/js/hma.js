

let body = document.body
let sun = document.querySelector('.toggle')
let moon = document.querySelector('.fa-moon')

moon.onclick = () =>{
    if(body.classList.toggle('dark')){
        moon.classList.replace('fa-moon', 'fa-sun');
    }else{
        moon.classList.replace('fa-sun', 'fa-moon')
    }
}