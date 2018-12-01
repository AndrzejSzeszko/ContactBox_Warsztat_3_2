$(document).ready(function () {

    let phoneForm = $('.phone-form').clone(true);
    let addPhoneButton = $('#add-phone-button');

    let emailForm = $('.email-form').clone(true);
    let addEmailButton = $('#add-email-button');

    let initialGroupForm = $('.group-form');
    let groupForm = initialGroupForm.clone(true).removeAttr('hidden');
    let addGroupButton = $('#add-group-button');

    let addressFormRadio = $('#address-form-radio').attr('checked', true);
    let addressForm = $('#address-form');
    let addressListRadio = $('#address-list-radio');
    let addressList = $('#address-list');

    initialGroupForm.remove();

    $(document).on('click', '.remove-button', function () {
        $(this).parent().remove()
    });



    addGroupButton.on('click', function() {
        let groupFormToAdd = groupForm.clone(true);
        $(this).before(groupFormToAdd)
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