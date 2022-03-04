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


function change_woman_img0(){ 
  document.getElementsByTagName("img")[0].src="../img/woman/Woman1.jpg";
}

function change_woman_rev0(){
  document.getElementsByTagName("img")[0].src="../img/woman/Woman1.2.jpg";
}
function change_woman_img1(){ 
  document.getElementsByTagName("img")[1].src="../img/woman/Woman2.jpg";
}
function change_woman_rev1(){
  document.getElementsByTagName("img")[1].src="../img/woman/Woman2.2.jpg";
}
function change_woman_img2(){ 
  document.getElementsByTagName("img")[2].src="../img/woman/Woman3.jpg";
}
function change_woman_rev2(){
  document.getElementsByTagName("img")[2].src="../img/woman/Woman3.2.jpg";
}
function change_woman_img3(){ 
  document.getElementsByTagName("img")[3].src="../img/woman/Woman4.jpg";
}
function change_woman_rev3(){    
  document.getElementsByTagName("img")[3].src="../img/woman/Woman4.2.jpg";
}
function change_woman_img4(){ 
  document.getElementsByTagName("img")[4].src="../img/woman/Woman5.jpg";
}
function change_woman_rev4(){    
  document.getElementsByTagName("img")[4].src="../img/woman/Woman5.2.jpg";
}
function change_woman_img5(){ 
  document.getElementsByTagName("img")[5].src="../img/woman/Woman6.jpg";
}
function change_woman_rev5(){    
      document.getElementsByTagName("img")[5].src="../img/woman/Woman6.2.jpg";
}
function change_woman_img6(){ 
  document.getElementsByTagName("img")[6].src="../img/woman/Woman7.jpg";
}
function change_woman_rev6(){    
  document.getElementsByTagName("img")[6].src="../img/woman/Woman7.2.jpg";
}
function change_woman_img7(){ 
  document.getElementsByTagName("img")[7].src="../img/woman/Woman8.jpg";
}
function change_woman_rev7(){    
  document.getElementsByTagName("img")[7].src="../img/woman/Woman8.2.jpg";
}