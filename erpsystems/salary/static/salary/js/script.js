$(document).on('click', '.edit-btn', function() {
    const row = $(this).closest('tr');
    row.find('td').each(function(index) {
        if (index === 2 || index === 3 || index === 4) {
            $(this).attr('contenteditable', 'true').css('background-color', '#eaf4fc')
        }
    });
    $(this).text('Зберегти').removeClass('edit-btn').addClass('save-btn');
});

$(document).on('click', '.save-btn', function() {
    const row = $(this).closest('tr');
    const id = row.data('id');
    const date = row.find('td:eq(2)').text();
    const amount = row.find('td:eq(3)').text();
    const status = row.find('td:eq(4)').text();

    $.ajax({
        url: `/update_salary/${id}/`,
        type: 'POST',
        data: {
            'amount': amount,
            'status': status,
            'date': date,
            'csrfmiddlewaretoken': '{{ csrf_token }}'
        },
        success: function() {
            row.find('td').attr('contenteditable', 'false').css('background-color', '');
            row.find('.save-btn').text('Редагувати').removeClass('save-btn').addClass('edit-btn');
        }
    });
});
$(document).on('click', '.delete-btn', function() {
    const row = $(this).closest('tr');
    const id = row.data('id');

    $.ajax({
        url: `/delete_salary/${id}/`,
        type: 'POST',
        data: {
            'csrfmiddlewaretoken': '{{ csrf_token }}'
        },
        success: function() {
            row.remove();
        }
    });
});