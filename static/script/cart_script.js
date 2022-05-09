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