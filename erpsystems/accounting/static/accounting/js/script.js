function sortByName() {
    const sortDirection = $('.filter-item:contains("Ім\'я")').hasClass('asc') ? 'desc' : 'asc';
    $('.filter-item:contains("Ім\'я")').toggleClass('asc', sortDirection === 'asc');
    $.ajax({
        url: filterUrl,
        type: 'GET',
        data: {
            'filter': 'name',
            'order': sortDirection
        },
        success: function (data) {
            $('#employee-list').html(data);
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
            $('#employee-list').html(data);
        }
    });
});
$(document).on('click', '.sort-item', function () {
    if ($(this).text().trim() === "Дата прийому") {
        const sortDirection = $(this).hasClass('asc') ? 'desc' : 'asc';
        $(this).toggleClass('asc', sortDirection === 'asc');
        $.ajax({
            url: filterUrl,
            type: 'GET',
            data: {
                'filter': 'hiring_date',
                'order': sortDirection
            },
            success: function (data) {
                $('#employee-list').html(data);
            }
        });
    } else {
        sortByName();
    }
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
            $('#employee-list').html(data);
        }
    });
});
$(document).ready(function() {
    $('#employeeForm').on('submit', function(e) {
        e.preventDefault(); // Prevent default form submission

        $.ajax({
            type: 'POST',
            url: $('#addEmployeeUrl').val(), // Adjust this to your URL for adding an employee
            data: $(this).serialize(),
            success: function(response) {
                // Handle success, e.g., close modal and refresh employee list
                $('#employeeModal').modal('hide');
                // Optionally, add new employee data to the table or refresh it
                alert('Співробітника успішно додано!');
            },
            error: function(xhr, status, error) {
                alert('Сталася помилка: ' + error);
            }
        });
    });
});