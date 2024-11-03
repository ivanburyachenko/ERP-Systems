$('.edit-task-btn').on('click', function() {
    var taskId = $(this).data('task-id');
    $.ajax({
        url: '/get-task/' + taskId + '/',
        method: 'GET',
        success: function(data) {
            $('#taskId').val(taskId);
            $('#status').val(data.status);
            $('#priority').val(data.priority);
            $('#description').val(data.description);
            $('#date_start').val(data.date_start);
            $('#date_finish').val(data.date_finish);
            $('#progress').val(data.progress);
            $('#comments').val(data.comments);
        
        }
    });
});

$('#editTaskForm').on('submit', function(e) {
    e.preventDefault();
    var taskId = $('#taskId').val();

    $.ajax({
        url: '/update-task/' + taskId + '/',
        method: 'POST',
        data: $(this).serialize(),
        success: function(data) {
            console.log(data)
            $('td:contains("Статус")').next().text(data.status);
            $('td:contains("Пріоритет")').next().text(data.priority);
            $('td:contains("Опис")').next().text(data.description);
            $('td:contains("Дата завдання")').next().text(data.date_start);
            $('td:contains("Дата початку")').next().text(data.date_start);
            $('td:contains("Дата закінчення")').next().text(data.date_finish);
            $('td:contains("Прогрес")').next().text(data.progress);
            $('td:contains("Коментарі")').next().text(data.comments);
            $('#editTaskModal').modal('hide');
        }
    });
});
