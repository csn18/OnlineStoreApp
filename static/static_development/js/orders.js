new WOW().init()

$(document).ready(function () {
    $('.cross-button').on('click', function (e) {
        e.preventDefault()

        let data = {}
        data.id = $('#cross').data('item_id')
        data.is_delete = true
        data.csrfmiddlewaretoken = $('#items [name="csrfmiddlewaretoken"]').val()
        let url = $('form').attr('action')

        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            success: function (data) {
                $('#cross').parent('div').parent('div').parent('div').parent('div').detach()
                swal('Товар удален', '', 'success')
            }
        })
    })

    function basketAmount() {
        let total_order_amount = 0;
        $('.total-price-in-basket').each(function () {
            total_order_amount += parseInt($(this).text())
            $('#total_order_amount').text(total_order_amount)
        })
    }

    $(document).on('change', '.product-nmb', function () {
        let current_nmb = $(this).val()
        let current_class = $(this).closest('.row')
        let current_price = parseInt(current_class.find('.product-price').text())
        let total_amount = current_nmb * current_price
        current_class.find('.total-price-in-basket').text(total_amount + '₽')
        basketAmount()
    })

    basketAmount()


    $(document).scroll(function () {
        $('#scroll').fadeIn(200);
    })
    $('#scroll').click(function () {
        $('body,html').animate({
            scrollTop: 900
        }, 1000);
    })

    $(document).scroll(function () {
        $('#scroll_to_top').fadeIn(200);
    })
    $('#scroll_to_top').click(function () {
        console.log('scroll')
        $('body,html').animate({scrollTop: 0}, 1000);
    })

})