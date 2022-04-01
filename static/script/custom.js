$(document).ready(function(){
    // Product Review Save
$("#addForm").submit(function(){
    $.ajax({
      data:$(this).serialize(),
      method:$(this).attr('method'),
      url:$(this).attr('action'),
      dataType:'json',
      success:function(res){
        if(res.bool==true){
            $(".ajaxRes").html('Data has been added.');
      }
    }
    });
    e.preventDefault();
  });
  // End
});