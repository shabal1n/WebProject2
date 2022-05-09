$('.carousel').carousel();

function redirectToPage(pageName) {
  // window.location = href;
  location.href = "http://127.0.0.1:8000/" + pageName;
}