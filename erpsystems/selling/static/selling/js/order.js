$(document).ready(function() {
    $('.edit-order-button').on('click', function() {
        var orderId = $(this).data('id');
        $('#orderId').val(orderId);
        $.ajax({
            url: '/get-order/' + orderId + '/',
            method: 'GET',
            success: function(data) {
                $('#client_name').val(data.client_name);
                $('#client_phone_number').val(data.client_phone_number);
                $('#client_email').val(data.client_email);
                $('#delivery_address').val(data.delivery_address);
                $('#price').val(data.price);
                $('#discount').val(data.discount);
                $('#total_payable').val(data.total_payable);
                $('#status').val(data.status);
            }
        });
    });

    $('#editOrderForm').on('submit', function(e) {
        e.preventDefault();

        var orderId = $('#orderId').val();

        $.ajax({
            url: '/update-order/' + orderId + '/',
            method: 'POST',
            data: $(this).serialize(),
            success: function(data) {
                $('td:contains("Ім\'я клієнта")').next().text(data.client_name);
                $('td:contains("Телефон")').next().text(data.client_phone_number);
                $('td:contains("Email")').next().text(data.client_email);
                $('td:contains("Адреса доставки")').next().text(data.delivery_address);
                $('td:contains("Підсумкова сума")').next().text(data.price);
                $('td:contains("Знижка")').next().text(data.discount);
                $('td:contains("Разом до оплати")').next().text(data.total_payable);
                $('#editOrderModal').modal('hide');
            }
        });
    });
});
