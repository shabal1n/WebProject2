function changeHeaderColor(color) {
    if(document.getElementById("brand_name").style.display != "none") {
      document.getElementById("header").style.backgroundColor = color; 
    }
}

window.onscroll = function() {scrollFunction()};
  
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
    document.getElementsByTagName("img")[0].src="../img/men/finn_flare2.jpg";
}

function change_rev0(){
    document.getElementsByTagName("img")[0].src="../img/men/finn_flare6.jpg";
}
function change_img1(){ 
    document.getElementsByTagName("img")[1].src="../img/men/finn_flare3.jpg";
}
function change_rev1(){
    document.getElementsByTagName("img")[1].src="../img/men/finn_flare7.jpg";
}
function change_img2(){ 
    document.getElementsByTagName("img")[2].src="../img/men/finn_flare4.jpg";
}
function change_rev2(){
    document.getElementsByTagName("img")[2].src="../img/men/finn_flare8.jpg";
}
function change_img3(){ 
    document.getElementsByTagName("img")[3].src="../img/men/finn_flare5.jpg";
}
function change_rev3(){    
    document.getElementsByTagName("img")[3].src="../img/men/finn_flare9.jpg";
}
function change_img4(){ 
    document.getElementsByTagName("img")[4].src="../img/men/finn_flare10.jpg";
}
function change_rev4(){    
    document.getElementsByTagName("img")[4].src="../img/men/finn_flare11.jpg";
}
function change_img5(){ 
    document.getElementsByTagName("img")[5].src="../img/men/finn_flare12.jpg";
}
function change_rev5(){    
        document.getElementsByTagName("img")[5].src="../img/men/finn_flare13.jpg";
}
function change_img6(){ 
    document.getElementsByTagName("img")[6].src="../img/men/finn_flare14.jpg";
}
function change_rev6(){    
    document.getElementsByTagName("img")[6].src="../img/men/finn_flare15.jpg";
}
function change_img7(){ 
    document.getElementsByTagName("img")[7].src="../img/men/finn_flare16.jpg";
}
function change_rev7(){    
    document.getElementsByTagName("img")[7].src="../img/men/finn_flare17.jpg";
}