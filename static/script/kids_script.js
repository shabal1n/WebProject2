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


function change_kids_img0(){ 
  document.getElementsByTagName("img")[0].src="../img/kids/kids1.jpg";
}

function change_kids_rev0(){
  document.getElementsByTagName("img")[0].src="../img/kids/kids1.2.jpg";
}
function change_kids_img1(){ 
  document.getElementsByTagName("img")[1].src="../img/kids/kids2.jpg";
}
function change_kids_rev1(){
  document.getElementsByTagName("img")[1].src="../img/kids/kids2.2.jpg";
}
function change_kids_img2(){ 
  document.getElementsByTagName("img")[2].src="../img/kids/kids3.jpg";
}
function change_kids_rev2(){
  document.getElementsByTagName("img")[2].src="../img/kids/kids3.2.jpg";
}
function change_kids_img3(){ 
  document.getElementsByTagName("img")[3].src="../img/kids/kids4.jpg";
}
function change_kids_rev3(){    
  document.getElementsByTagName("img")[3].src="../img/../img/kids/kids4.2.jpg";
}
function change_kids_img4(){ 
  document.getElementsByTagName("img")[4].src="../img/kids/kids5.jpg";
}
function change_kids_rev4(){    
  document.getElementsByTagName("img")[4].src="../img/kids/kids5.2.jpg";
}
function change_kids_img5(){ 
  document.getElementsByTagName("img")[5].src="../img/kids/kids6.jpg";
}
function change_kids_rev5(){    
      document.getElementsByTagName("img")[5].src="../img/kids/kids6.2.jpg";
}
function change_kids_img6(){ 
  document.getElementsByTagName("img")[6].src="../img/kids/kids7.jpg";
}
function change_kids_rev6(){    
  document.getElementsByTagName("img")[6].src="../img/kids/kids7.2.jpg";
}
function change_kids_img7(){ 
  document.getElementsByTagName("img")[7].src="../img/kids/kids8.jpg";
}

function change_kids_rev7(){    
  document.getElementsByTagName("img")[7].src="../img/kids/kids8.2.jpg";
}