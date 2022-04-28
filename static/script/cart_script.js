function changeHeaderColor(color) {
  if(document.getElementById("brand_name").style.display !== "none") {
    document.getElementById("header").style.backgroundColor = color; 
  }
}
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 250 || document.documentElement.scrollTop > 250) {
    document.getElementById("header").style.backgroundColor = "rgb(27, 27, 27)";
    document.getElementById("brand_name").style.display = "none";
  } else {
    document.getElementById("header").style.backgroundColor = "transparent";
    document.getElementById("brand_name").style.display = "block";
  }
}

function hideItems(number) {
  document.getElementById('item_'+number).style.display = 'none';
  let temp = number.charAt(0).toUpperCase() + number.slice(1);
  let price = parseInt(document.getElementById('total' + temp).innerHTML);
  let ov = parseInt(document.getElementById('price').innerHTML);
  document.getElementById('price').innerHTML = ov - price;
}



// $('#proceed').on('click', function() {
//   $('#proceed').hide();
//   $('.hidden').css('display', 'block');
// });

// function dateBound() {
//   let today = new Date();
//   const dd = String(today.getDate()).padStart(2, '0');
//   const mm = String(today.getMonth() + 1).padStart(2, '0');
//   const yyyy = today.getFullYear();
//
//   today = yyyy + "-" + mm + "-" + dd;
//   document.getElementById('shippingDate').min = today;
// }
//
// document.onload(dateBound());