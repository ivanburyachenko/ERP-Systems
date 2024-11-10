function sortByNumber() {
    const numberDirection = $('.filter-item:contains("Номер")').hasClass('asc') ? 'desc' : 'asc';
    $('.filter-item:contains("Номер")').toggleClass('asc', numberDirection === 'asc');
    $.ajax({
        url: filterUrl,
        type: 'GET',
        data: {
            'filter': 'number',
            'number': numberDirection
        },
        success: function (data) {
            $('#orders-list').html(data);
        }
    });
}
function sortByDate() {
    const date_orderDirection = $('.filter-item:contains("Дата прийому")').hasClass('asc') ? 'desc' : 'asc';
    $('.filter-item:contains("Дата прийому")').toggleClass('asc', date_orderDirection === 'asc');
    $.ajax({
        url: filterUrl,
        type: 'GET',
        data: {
            'filter': 'date_order',
            'date_order': date_orderDirection
        },
        success: function (data) {
            $('#orders-list').html(data);
        }
    });
}
function sortByPrice() {
    const total_payableDirection = $('.filter-item:contains("Ціна")').hasClass('asc') ? 'desc' : 'asc';
    $('.filter-item:contains("Ціна")').toggleClass('asc', total_payableDirection === 'asc');
    $.ajax({
        url: filterUrl,
        type: 'GET',
        data: {
            'filter': 'total_payable',
            'total_payable': total_payableDirection
        },
        success: function (data) {
            $('#orders-list').html(data);
        }
    });
}
function sortByEmail() {
    const client_emailDirection = $('.filter-item:contains("Email")').hasClass('asc') ? 'desc' : 'asc';
    $('.filter-item:contains("Email")').toggleClass('asc', client_emailDirection === 'asc');
    $.ajax({
        url: filterUrl,
        type: 'GET',
        data: {
            'filter': 'client_email',
            'client_email': client_emailDirection
        },
        success: function (data) {
            $('#orders-list').html(data);
        }
    });
}
$(document).on('click', '.dropdown-item', function () {
    const filter = $(this).closest('.dropdown').find('h2').text().toLowerCase();
    const value = $(this).text();
    $.ajax({
        url: filterUrl,
        type: 'GET',
        data: {
            'filter': filter,
            'value': value
        },
        success: function (data) {
            $('#orders-list').html(data);
        }
    });
});
$(document).on('click', '#clear-filters', function () {
    $('.filter-item').removeClass('asc');
    $('.dropdown-menu .dropdown-item').removeClass('active');
    $.ajax({
        url: filterUrl,
        type: 'GET',
        data: {
            'filter': '',
            'value': ''
        },
        success: function (data) {
            $('#orders-list').html(data);
        }
    });
});
$(document).ready(function() {
    $('#orderForm').on('submit', function(e) {
        e.preventDefault();

        $.ajax({
            type: 'POST',
            url: $('#addOrderUrl').val(),
            data: $(this).serialize(),
            success: function(response) {
                $('#orderModal').modal('hide');
                $('#orderForm')[0].reset();
            }
        });
    });
});
