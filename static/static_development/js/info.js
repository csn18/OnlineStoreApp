new WOW().init()

$(document).ready(function () {
    $('#to_order').on('click', function (e) {
        e.preventDefault()
        let phone_number = $('#form_phone_number').val()
        let url = $('form').attr('action')

        let data = {}
        data.csrfmiddlewaretoken = $('#phone_number [name="csrfmiddlewaretoken"]').val()
        data.phone_number = phone_number

        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            success: function (data) {
                for (let elem of data) {
                    $('#id_order').append('<li class="li-info">' + elem['id'] + '</li>' + '<hr>')
                    $('#number_phone').append('<li class="li-info">' + elem['phone'] + '</li>' + '<hr>')
                    $('#address').append('<li class="li-info">' + elem['address'] + '</li>' + '<hr>')
                    $('#created').append('<li class="li-info">' + elem['created_date'].slice(0, 19) + '</li>' + '<hr>')
                    $('#status').append('<li class="li-info">' + elem['status'] + '</li>' + '<hr>')

                }
            }
        })
    })

    $(document).scroll(function () {
        $('#to_order').fadeIn(200);
    })
    $('#to_order').click(function () {
        $('body,html').animate({
            scrollTop: 900
        }, 1000);
    })

    $(document).scroll(function () {
        $('#scroll_to_top').fadeIn(200);
    })
    $('#scroll_to_top').click(function () {
        $('body,html').animate({
            scrollTop: 0
        }, 1000);
    })
})