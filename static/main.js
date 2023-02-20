console.log(1)
console.log($("#gen_type").val());
$("#gen_type").change(function(){
    console.log($(this).val());
    if($(this).val() == "image"){
        $('#img_n').show();
        $('#img_size').show();
        $('#text_model').hide();
    }else{
        $('#img_n').hide();
        $('#img_size').hide();
        $('#text_model').show();
    }
})