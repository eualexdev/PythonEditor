let menuBarOpend = false;
const buttonNavBar = document.getElementById("buttonNavBar");
const menuBar = document.getElementById("MenuBar")
buttonNavBar.onclick = () => {
    if (menuBarOpend == false){
        menuBar.style.top = "82px";
        buttonNavBar.style.backgroundColor = "var(--secondColor)"
        menuBarOpend = true;
    } else {
        menuBar.style.top = "-100%";
        buttonNavBar.style.backgroundColor = "var(--firstColor)"
        menuBarOpend = false;
    }
};