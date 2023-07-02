const marks_modal = document.querySelector('.marks-modal')
const review_btn = document.querySelectorAll('.review')
const cancel = document.querySelectorAll('.cancel')


review_btn.forEach(btn => {
    btn.addEventListener('click', (el)=>{
    el.preventDefault()
    const id = el.currentTarget.getAttribute('btn-id')
    document.getElementById(id).classList.add('modal-active')
})
})

// cancel.addEventListener('click', (el)=>{
//     el.preventDefault()
//     marks_modal.classList.remove('modal-active')
// })

cancel.forEach(btn => {
    btn.addEventListener('click', (el)=>{
    el.preventDefault()
    const id = el.currentTarget.getAttribute('btn-id')
    document.getElementById(id).classList.remove('modal-active')
})
})

