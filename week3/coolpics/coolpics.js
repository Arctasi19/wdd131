// Variables
const menuButton = document.querySelector('#menu');
const navMenu = document.querySelector('#nav');
const gallery = document.querySelector('.gallery');
let modal;

// Functions
function toggleMenu() {
    navMenu.classList.toggle('hide');
}
function handleResize() {
    let windowWidth = window.innerWidth;
    if (windowWidth > 1000) {
        navMenu.classList.remove('hide');
    }
    else {
        navMenu.classList.add('hide');
    }
}
function createModal(Img) {
    const buildModal = document.createElement('dialog');  
    buildModal.classList.add('modal');
    buildModal.innerHTML = `
    <img src="${Img}"><button class='close-viewer'>X</button>
    `;
    document.body.append(buildModal);
    modal = buildModal;
    modal.showModal();
    modal.addEventListener('click', (event) => {
        if (event.target === modal) {
        modal.close();
  }
})
}
function galleryClickEvent(event) {
    if (event.target.closest('img')) {
        const imgSrc = event.target.getAttribute('src');
        const imgName = imgSrc.split('/').pop().split('-')[0];
        const resultImg = `images/${imgName}-full.jpeg`;
        createModal(resultImg);
    }
}


// Event Listeners
menuButton.addEventListener('click', toggleMenu);
window.addEventListener('resize', handleResize);
gallery.addEventListener('click', galleryClickEvent);
document.addEventListener('click', (event) => {
    if (event.target.classList.contains('close-viewer')) {
        modal.close();
    }
});

// Initial Function Runs
handleResize();