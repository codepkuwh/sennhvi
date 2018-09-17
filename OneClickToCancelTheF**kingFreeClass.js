$('table :checkbox').each(
    function(){
        var isChecked = $(this).prop('checked');
        if(isChecked){$(this).click()};
    }
);
$(".save_btn").click();
