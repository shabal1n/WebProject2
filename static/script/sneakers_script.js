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



function change_sneakers_img0(){ 
    document.getElementsByTagName("img")[0].src="../img/sneakers/Man1.jpg";
  }
  
  function change_sneakers_rev0(){
    document.getElementsByTagName("img")[0].src="../img/sneakers/Man1.2.jpg";
  }
  function change_sneakers_img1(){ 
    document.getElementsByTagName("img")[1].src="../img/sneakers/Man2.jpg";
  }
  function change_sneakers_rev1(){
    document.getElementsByTagName("img")[1].src="../img/sneakers/Man2.2.jpg";
  }
  function change_sneakers_img2(){ 
    document.getElementsByTagName("img")[2].src="../img/sneakers/Man3.jpg";
  }
  function change_sneakers_rev2(){
    document.getElementsByTagName("img")[2].src="../img/sneakers/Man3.2.jpg";
  }
  function change_sneakers_img3(){ 
    document.getElementsByTagName("img")[3].src="../img/sneakers/Woman4.jpg";
  }
  function change_sneakers_rev3(){    
    document.getElementsByTagName("img")[3].src="../img/sneakers/Woman4.2.jpg";
  }
  function change_sneakers_img4(){ 
    document.getElementsByTagName("img")[4].src="../img/sneakers/Woman5.jpg";
  }
  function change_sneakers_rev4(){    
    document.getElementsByTagName("img")[4].src="../img/sneakers/Woman5.2.jpg";
  }
  function change_sneakers_img5(){ 
    document.getElementsByTagName("img")[5].src="../img/sneakers/Woman6.jpg";
  }
  function change_sneakers_rev5(){    
        document.getElementsByTagName("img")[5].src="../img/sneakers/Woman6.2.jpg";
  }
  function change_sneakers_img6(){ 
    document.getElementsByTagName("img")[6].src="../img/sneakers/Man7.jpg";
  }
  function change_sneakers_rev6(){    
    document.getElementsByTagName("img")[6].src="../img/sneakers/Man7.2.jpg";
  }
  function change_sneakers_img7(){ 
    document.getElementsByTagName("img")[7].src="../img/sneakers/Man8.jpg";
  }
  function change_sneakers_rev7(){    
    document.getElementsByTagName("img")[7].src="../img/sneakers/Man8.2.jpg";
  }