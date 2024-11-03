$(document).ready(function() {
    $('.edit-button').on('click', function() {
        var employeeId = $(this).data('id');
        $('#employeeId').val(employeeId);
        $.ajax({
            url: '/get-employee/' + employeeId + '/',
            method: 'GET',
            success: function(data) {
                $('#first_name').val(data.first_name);
                $('#last_name').val(data.last_name);
                $('#patronymic').val(data.patronymic);
                $('#date_of_birthday').val(data.date_of_birthday);
                $('#gender').val(data.gender);
                $('#residential_address').val(data.residential_address);
                $('#phone_number').val(data.phone_number);
                $('#email').val(data.email);
                $('#position').val(data.position);
                $('#hiring_date').val(data.hiring_date);
                $('#status').val(data.status);
                $('#schedule').val(data.schedule);
            }
        });
    });
    $('#editEmployeeForm').on('submit', function(e) {
        e.preventDefault();

        var employeeId = $('#employeeId').val();

        $.ajax({
            url: '/update-employee/' + employeeId + '/',
            method: 'POST',
            data: $(this).serialize(),
            success: function(data) {
                $('#name-of-employee').text(data.first_name + ' ' + data.last_name + ' ' + data.patronymic);
                $('td:contains("Дата народження")').next().text(data.date_of_birthday);
                $('td:contains("Стать")').next().text(data.gender);
                $('td:contains("Адреса")').next().text(data.residential_address);
                $('td:contains("Телефон")').next().text(data.phone_number);
                $('td:contains("Email")').next().text(data.email);
                $('td:contains("Позиція")').next().text(data.position);
                $('td:contains("Дата прийому на роботу")').next().text(data.hiring_date);
                $('td:contains("Статус")').next().text(data.status);
                $('td:contains("Графік роботи")').next().text(data.schedule);
                $('#editEmployeeModal').modal('hide');
            }
        });
    });
})