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
            $('#tasks-list').html(data);
        }
    });
}
function sortByDate() {
    const date_startDirection = $('.filter-item:contains("Дата початку")').hasClass('asc') ? 'desc' : 'asc';
    $('.filter-item:contains("Дата початку")').toggleClass('asc', date_startDirection === 'asc');
    $.ajax({
        url: filterUrl,
        type: 'GET',
        data: {
            'filter': 'date_start',
            'date_start': date_startDirection
        },
        success: function (data) {
            $('#tasks-list').html(data);
        }
    });
}
function sortByPercent() {
    const progressDirection = $('.filter-item:contains("Процент виконання")').hasClass('asc') ? 'desc' : 'asc';
    $('.filter-item:contains("Процент виконання")').toggleClass('asc', progressDirection === 'asc');
    $.ajax({
        url: filterUrl,
        type: 'GET',
        data: {
            'filter': 'progress',
            'progress': progressDirection
        },
        success: function (data) {
            $('#tasks-list').html(data);
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
            $('#tasks-list').html(data);
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
            $('#tasks-list').html(data);
        }
    });
});
$(document).ready(function() {
    $('#taskForm').on('submit', function(e) {
        e.preventDefault(); // Prevent default form submission

        $.ajax({
            type: 'POST',
            url: $('#addTaskUrl').val(), // Ensure this URL is valid
            data: $(this).serialize(),
            success: function(response) {
                alert('Завдання успішно додано!');
                $('#taskModal').modal('hide'); // Hide the modal after successful submission
                $('#taskForm')[0].reset(); // Reset the form
            },
            error: function(xhr, status, error) {
                alert('Сталася помилка: ' + error);
            }
        });
    });
});
