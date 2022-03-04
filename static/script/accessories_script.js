function changeHeaderColor(color) {
    if (document.getElementById("brand_name").style.display != "none") {
        document.getElementById("header").style.backgroundColor = color;
    }
}
window.onscroll = function () { scrollFunction() };

function scrollFunction() {
    if (document.body.scrollTop > 350 || document.documentElement.scrollTop > 350) {
        document.getElementById("header").style.backgroundColor = "rgb(27, 27, 27)";
        document.getElementById("brand_name").style.display = "none";
    } else {
        document.getElementById("header").style.backgroundColor = "transparent";
        document.getElementById("brand_name").style.display = "block";
    }
}


function change_img0(){ 
    document.getElementsByTagName("img")[0].src="../img/acessories/louis-vuitton-1bag.png";
}

function change_rev0(){
    document.getElementsByTagName("img")[0].src="../img/acessories/animated/louis-vuitton-second-voyage-man-bag1.png";
}
function change_img1(){ 
    document.getElementsByTagName("img")[1].src="../img/acessories/louis-vuitton-2bag.png";
}
function change_rev1(){
    document.getElementsByTagName("img")[1].src="../img/acessories/animated/louis-vuitton-second-man-bag3.png";
}
function change_img2(){ 
    document.getElementsByTagName("img")[2].src="../img/acessories/louis-vuitton-3bag.png";
}
function change_rev2(){
    document.getElementsByTagName("img")[2].src="../img/acessories/animated/louis-vuitton-second-man-bag2.png";
}
function change_img3(){ 
    document.getElementsByTagName("img")[3].src="../img/acessories/louis-vuitton-4-womanbag.png";
}
function change_rev3(){    
    document.getElementsByTagName("img")[3].src="../img/acessories/animated/louis-vuitton-second_woman_bag2.jfif";
}
function change_img4(){ 
    document.getElementsByTagName("img")[4].src="../img/acessories/louis-vuitton-5-womanbag.png";
}
function change_rev4(){    
    document.getElementsByTagName("img")[4].src="../img/acessories/animated/louis-vuitton-second_woman_bag_3.jfif";
}
function change_img5(){ 
    document.getElementsByTagName("img")[5].src="../img/acessories/louis-vuitton-6-womanbag.png";
}
function change_rev5(){    
        document.getElementsByTagName("img")[5].src="../img/acessories/animated/louis-vuitton-second_woman_bag1.jfif";
}
function change_img6(){ 
    document.getElementsByTagName("img")[6].src="../img/acessories/louis-vuitton-watch-man1.png";
}
function change_rev6(){    
    document.getElementsByTagName("img")[6].src="../img/acessories/animated/louis-vuitton-watch_second2.png";
}
function change_img7(){ 
    document.getElementsByTagName("img")[7].src="/img/acessories/louis-vuitton-watch-man2.png";
}
function change_rev7(){    
    document.getElementsByTagName("img")[7].src="../img/acessories/animated/louis-vuitton-watch_second.png";
}