const nav = document.querySelector('.navigation');
const navClose = document.querySelector('.nav-close');
const navOpen = document.querySelector('.burger');

navClose.addEventListener('click', ()=>{
    nav.classList.remove('nav-active');
})

navOpen.addEventListener('click', () =>{
    nav.classList.toggle('nav-active');
})


const colors = ["#4abdac", "#fc4a1a", "#f78733", "#4717f6", "#a239ca", "#062f4f", "#813772", "#ff3b3f", "#76323f"];