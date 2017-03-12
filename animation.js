function openNav() {
    if ($("#SidebarLinks").is(":visible") === true) {
        closeNav();
        return;
    }
    document.getElementById("mySidenav").style.width = "350px";
    document.getElementById("Header").style.left = "350px";
    document.getElementById("myclosebtn").style.animation = "rotation 0.5s cubic-bezier(.45, 0, .55, 1) 1";
    document.getElementById("myclosebtn").style.transform = "rotate(90deg) translate(-12px, -12px)";
    $( "#SidebarLinks" ).show();
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "100px";
    document.getElementById("Header").style.left = "100px";
    document.getElementById("myclosebtn").style.animation = "rotationReverse 0.5s cubic-bezier(.45, 0, .55, 1) 1";
    document.getElementById("myclosebtn").style.transform = "rotate(0deg) translate(0px, 0px)";
    $("#SidebarLinks").hide("fast");
}

function openProvinces() {
    if ($("#SidebarLinks2").is(":visible") === true) {
        closeProvinces();
        return;
    }
    $( "#SidebarLinks2" ).show("fast");
}

function closeProvinces() {
    $("#SidebarLinks2").hide("fast");
}
