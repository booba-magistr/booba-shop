$(document).ready(function () {

    $(document).on("click", ".add-to-cart", function (e) {
        e.preventDefault();

        var product_id = $(this).data("product-id");
        var add_to_cart_url = $(this).attr("href");

        $.ajax({
            type: "POST",
            url: add_to_cart_url,
            data: {
                product_id: product_id,
                csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
            },
            success: function (data) {
                var cartItemsContainer = $(".cart-section");
                cartItemsContainer.html(data.cart_items_html);
            }
        });
    });
})



$(document).on("click", ".cart-product__remove-btn", function (e) {
    e.preventDefault();

    var cart_id = $(this).data("cart-id");
    var remove_from_cart = $(this).attr("href");

    $.ajax({
        type: "POST",
        url: remove_from_cart,
        data: {
            cart_id: cart_id,
            csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
        },
        success: function (data) {
            var cartItemsContainer = $("body");
            cartItemsContainer.html(data.cart_items_html);
        }
    });
});


$(document).on("click", ".count__down", function () {
    var url = $(this).data("count-url");
    var cartID = $(this).data("cart-id");
    var $input = $(this).closest('.cart-product__count').find('.number');
    var currentValue = parseInt($input.val());
    if (currentValue > 1) {
        $input.val(currentValue - 1);
        updateCart(cartID, currentValue - 1, -1, url);
    }
});

$(document).on("click", ".count__up", function () {
    var url = $(this).data("count-url");
    var cartID = $(this).data("cart-id");
    var $input = $(this).closest('.cart-product__count').find('.number');
    var currentValue = parseInt($input.val());

    $input.val(currentValue + 1);
    updateCart(cartID, currentValue + 1, 1, url);
});

function updateCart(cartID, quantity, change, url) {
    $.ajax({
        type: "POST",
        url: url,
        data: {
            cart_id: cartID,
            quantity: quantity,
            csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
        },

        success: function (data) {
            var cartItemsContainer = $(".number");
            cartItemsContainer.html(data.cart_items_html);

        },
    });
}