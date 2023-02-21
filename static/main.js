$('select[name="gen_type"]').change(function() {
    if($(this).val() == 'image') {
        $('select[name="gen_img_n"]').show();
        $('select[name="gen_img_size"]').show();
        $('select[name="gen_text_module"]').hide();
    } else {
        $('select[name="gen_img_n"]').hide();
        $('select[name="gen_img_size"]').hide();
        $('select[name="gen_text_module"]').show();
    }
});