function changeHeaderColor(color) {
    if (document.getElementById("brand_name").style.display != "none") {
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


function change_img() {
    const allImages = document.getElementsByTagName('img');
    for (let i = 0; i < allImages.length; i++) {
        const imgSource = allImages[i].src;
        allImages[i].addEventListener("mouseleave", function (event) {
            allImages[i].src = imgSource.slice(0, -6) + ".jpg";
        });
        allImages[i].addEventListener("mouseenter", function (event) {
            allImages[i].src = imgSource.slice(0, -4) + ".2.jpg";
        });
    }
}