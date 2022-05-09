function changeHeaderColor(color) {
    if (document.getElementById("brand_name").style.display !== "none") {
        document.getElementById("header").style.backgroundColor = color;
    }
}

window.onscroll = function () {
    scrollFunction()
};

function scrollFunction() {
    if (document.body.scrollTop > 350 || document.documentElement.scrollTop > 350) {
        document.getElementById("header").style.backgroundColor = "rgb(27, 27, 27)";
        document.getElementById("brand_name").style.display = "none";
    } else {
        document.getElementById("header").style.backgroundColor = "transparent";
        document.getElementById("brand_name").style.display = "block";
    }
}