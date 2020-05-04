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
        console.log(data)

        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            success: function (data) {
                swal('Отлично!', 'Товар добавлен в корзину', 'success')
                if (data['products']) {
                    $('#order_text').html('')
                    $('#text_in_basket').detach()
                    $('.cont').html('')
                    $('#count_orders').html('').append(data['products']['length'])
                    $.each(data['products'], function (key, value) {
                        $('#order_text').append('<div class="col-6" id="name_order">' + value.name + '</div>')
                        $('#order_text').append('<div class="col-2" id="count_order">' + value.nmb + '</div>')
                        $('#order_text').append('<div class="col-3" id="toggle_price">' + value.price + '</div>')

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

    $(document).scroll(function () {
        $('#scroll_to_top').fadeIn(200);
    })
    $('#scroll_to_top').click(function () {
        console.log('scroll')
        $('body,html').animate({scrollTop: 0}, 1000);
    })

});

