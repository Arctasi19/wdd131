const themeSelect = document.getElementById('theme-select');
function changeTheme() {
    const selectedTheme = themeSelect.value;
    const imgState = document.getElementById("logo");
    if (selectedTheme === 'dark') {
        document.body.classList.add('dark');
        imgState.src = "images/white-byui.png";
    } else {
        document.body.classList.remove('dark');
        imgState.src = "images/byui-logo_blue.webp";
    }
}
themeSelect.addEventListener('change', changeTheme);