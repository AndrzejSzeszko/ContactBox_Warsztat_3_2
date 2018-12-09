$(document).ready(function () {

    let phoneForm = $('.phone-form').first().clone(true);
    let addPhoneButton = $('#add-phone-button');

    let emailForm = $('.email-form').first().clone(true);
    let addEmailButton = $('#add-email-button');

    let initialGroupForm = $('.group-form').first();
    let groupForm = initialGroupForm.clone(true).removeAttr('hidden');
    let addGroupButton = $('#add-group-button');

    let addressFormRadio = $('#address-form-radio').attr('checked', true);
    let initialAddressForm = $('#address-form');
    let addressForm = initialAddressForm.clone(true);
    let addressListRadio = $('#address-list-radio');
    let initialAddressList = $('#address-list');
    let addressList = initialAddressList.clone(true);

    initialGroupForm.remove();
    initialAddressList.remove();

    $(document).on('click', '.remove-button', function () {
        $(this).parent().remove()
    });

    addressFormRadio.on('change', function () {
        $('#address-list').remove();
        let addressFormToAdd = addressForm.clone(true);
        $(this).next().after(addressFormToAdd)
    });

    addressListRadio.on('change', function () {
        $('#address-form').remove();
        let addressListToAdd = addressList.clone(true);
        $(this).next().after(addressListToAdd)
    });

    addGroupButton.on('click', function () {
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