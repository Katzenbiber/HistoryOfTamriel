/* Set the width of the side navigation to 250px and the left margin of the page content to 250px */
var isOpen = false;

function openNav() {
    document.getElementById("mySidenav").style.width = "350px";
    document.getElementById("myclosebtn").style.animation = "rotation 0.5s cubic-bezier(.45, 0, .55, 1) 1";
    document.getElementById("myclosebtn").style.transform = "rotate(90deg) translate(-12px, -12px)";
    $( "div:hidden" ).show();
    if (isOpen === true) {
        closeNav();
        return;
    }
    isOpen = true;
}

/* Set the width of the side navigation to 0 and the left margin of the page content to 0 */
function closeNav() {
    document.getElementById("mySidenav").style.width = "100px";
    document.getElementById("myclosebtn").style.animation = "rotationReverse 0.5s cubic-bezier(.45, 0, .55, 1) 1";
    document.getElementById("myclosebtn").style.transform = "rotate(0deg) translate(0px, 0px)";
    $("#SidebarLinks").hide("fast");
    isOpen = false;
}