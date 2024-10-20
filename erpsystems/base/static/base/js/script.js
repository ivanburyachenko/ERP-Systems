$(document).ready(() => {
    if (localStorage.getItem('isAuthenticated') == 'true') {
        $('.header-auth-done').removeClass('d-none');
        $('.header-auth').addClass('d-none');
    }else{
        $('.header-auth-done').addClass('d-none');
        $('.header-auth').removeClass('d-none'); 
    }
    $('#btn-register').click(() => {
        var url = $('#btn-register').attr('url');
        $.ajax({
            url: url,
            type: 'POST',
            data: {
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                name: $('input[name=name]').val(),
                surname: $('input[name=surname]').val(),
                password: $('input[name=password-reg]').val(),
                username: $('input[name=username-reg]').val(),
                repeat_password: $('input[name=repeat-password]').val(),
            },
            success: function (response) {
                if (response.isRegister) {
                    $('.hello-user-register').text(`Дякуємо за реєстрацію, ${response.name}!`)
                    $('input[name=name]').val('')
                    $('input[name=password-reg]').val('')
                    $('input[name=surname]').val('')
                    $('input[name=repeat-password]').val('')
                    $('input[name=username-reg]').val('')
                    $('.register-error').text('')
                }
                if (response.error) {
                    $('.register-error').text(response.error)
                }
            }
        })
    })
    $('#btn-auth').click(() => {
        var url = $('#btn-auth').attr('url');
        $.ajax({
            url: url,
            type: 'POST',
            data: {
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                username: $('input[name=username-auth]').val(),
                password: $('input[name=loginPassword]').val(),
            },
            success: function (response) {
                if (response.isLogin) {
                    $('.hello-user-auth').text(`Вітаємо, ${response.username}!`)
                    $('input[name=username-auth]').val('')
                    $('input[name=loginPassword]').val('')
                    localStorage.setItem('isAuthenticated', 'true')
                    $('.header-auth-done').removeClass('d-none');
                    $('.header-auth').addClass('d-none');
                }
                if (response.error) {
                    $('.login-error').text(response.error)
                }
            }
        })
    })
})