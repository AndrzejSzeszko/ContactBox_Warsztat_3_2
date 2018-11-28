$(document).ready(function () {
    let phoneForm = $('.phone-form').clone(true);
    let addPhoneButton = $('#add-phone-button');
    let emailForm = $('.email-form').clone(true);
    let addEmailButton = $('#add-email-button');

    $(document).on('click', '.remove-button', function () {
        $(this).parent().remove()
    });

    addPhoneButton.on('click', function () {
        let phoneFormToAdd = phoneForm.clone(true);
        $(this).before(phoneFormToAdd)
    });
    
    addEmailButton.on('click', function () {
        let emailFormToAdd = emailForm.clone(true);
        $(this).before(emailFormToAdd)
    });

});