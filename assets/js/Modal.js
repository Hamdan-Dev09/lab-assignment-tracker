const btns = document.querySelectorAll('.table-btn');
btns.forEach(btn => {
    btn.addEventListener('click', () => {
        const modal = document.querySelector('.mdl');
        modal.classList.remove('mdl-inactive')
        modal.classList.add('mdl-active');
    });
});
