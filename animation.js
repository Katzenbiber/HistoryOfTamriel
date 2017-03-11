/* Set the width of the side navigation to 250px and the left margin of the page content to 250px */
var isOpen = false;

function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
    if (screen.width / window.innerWidth > 2) {
        document.getElementById("main").style.marginLeft = "150px";
    }
    document.getElementById("myclosebtn").style.animation = "rotation 0.5s cubic-bezier(.45, 0, .55, 1) 1";
    document.getElementById("myclosebtn").style.transform = "rotate(90deg) translate(-12px, -12px)";
    /*myclosebtn.style.transform = "rotate(90deg) translate(-12px)";
    var closebtn = document.getElementsById('myclosebtn');
    var rot = 0;
    var id = setInterval(frame, 5);
    function frame() {
        if (pos == 90) {
            clearInterval(id);
        } else {
            rot++;
            closebtn.style.transform = 'rotate(' + rot + 'deg) translate(' + rot / 12 + ');';
        }
    }*/
    if (isOpen === true) {
        closeNav();
        return;
    }
    isOpen = true;
}

/* Set the width of the side navigation to 0 and the left margin of the page content to 0 */
function closeNav() {
    document.getElementById("mySidenav").style.width = "100px";
    document.getElementById("main").style.marginLeft = "0";
    document.getElementById("myclosebtn").style.animation = "rotationReverse 0.5s cubic-bezier(.45, 0, .55, 1) 1";
    document.getElementById("myclosebtn").style.transform = "rotate(0deg) translate(0px, 0px)";
    isOpen = false;
}