$(document).ready(function () {
    $(function () {
        jQuery("#zoom").imagezoomsl({
            zoomrange: [1, 1],
        });
    });
    // Product Review Save
    $("#addForm").submit(function () {
        print("Clicked")
        $.ajax({
            data: $(this).serialize(),
            method: $(this).attr('method'),
            url: $(this).attr('action'),
            dataType: 'json',
            success: function (res) {
                if (res.bool === true) {
                    $(".ajaxRes").html('Data has been added.');
                }
            }
        });
        e.preventDefault();
    });
});