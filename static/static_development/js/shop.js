new WOW().init()

$(document).ready(function () {
    $('#form_submit').on('submit', function (e) {
        e.preventDefault()

        let btn = $('#btn_submit')
        let product_price = btn.data('product_price')
        let product_name = btn.data('product_name')
        let product_id = btn.data('product_id')
        let nmb = $('#nmb').val()

        let data = {}
        data.product_id = product_id
        data.nmb = nmb
        data['csrfmiddlewaretoken'] = $('#form_submit [name="csrfmiddlewaretoken"]').val()

        let url = $('form').attr('action')

        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            success: function (data) {
                console.log(data['products'])
                if (data['products']) {
                    $.each(data['products'], function (key, value) {
                        $('#name_order').empty().append(value.name)
                        $('#count_order').empty().append(value.nmb)
                        $('#toggle_price').empty().append(value.price)
                    })
                }
            }
        })


    })

    function showHidden(selector) {
        $(selector).removeClass('hidden')
    }

    function addHidden(selector) {
        $(selector).addClass('hidden')
    }

    $('.basket-container').on('click', function (e) {
        e.preventDefault()
        showHidden('.basket-item')
    })

    $('.basket-container').mouseover('click, handler', function () {
        showHidden('.basket-item')
    })

    $('.basket-container').mouseout(function (e) {
        e.preventDefault()
        addHidden('.basket-item')
    })

});

// '<li>' + product_name + ' ' + product_price + '₽' + 'Кол-во' + data['total-nmb'] + '</li>'