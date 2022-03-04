function changeHeaderColor(color) {
  if(document.getElementById("brand_name").style.display != "none") {
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
  temp = number.charAt(0).toUpperCase() + number.slice(1);
  price = parseInt(document.getElementById('total' + temp).innerHTML);
  ov = parseInt(document.getElementById('price').innerHTML);
  document.getElementById('price').innerHTML = ov - price;
}

function changeTotal(number) {
  price = parseInt(document.getElementById('price_value_' + number.toLowerCase()).innerHTML);
  multiplier = document.getElementById('counter_value_' + number.toLowerCase()).value;
  itemTotal = document.getElementById('total' + number);
  if(parseInt(itemTotal.innerHTML) >= (price * multiplier)) {
    diff = parseInt(itemTotal.innerHTML) - (price * multiplier);
    overall = parseInt(document.getElementById('price').innerHTML);
    document.getElementById('price').innerHTML = overall - diff;
  } else {
    diff = (price * multiplier) - parseInt(itemTotal.innerHTML);
    overall = parseInt(document.getElementById('price').innerHTML);
    document.getElementById('price').innerHTML = overall + diff;
  }
  document.getElementById('total' + number).innerHTML = price * multiplier;
}

$('#proceed').on('click', function() {
  $('#proceed').hide();
  $('.hidden').css('display', 'block');
});

function dateBound() {
  var today = new Date();
  var dd = String(today.getDate()).padStart(2, '0');
  var mm = String(today.getMonth() + 1).padStart(2, '0');
  var yyyy = today.getFullYear();

  today = yyyy + "-" + mm + "-" + dd;
  document.getElementById('shippingDate').min = today;
}

document.onload(dateBound());