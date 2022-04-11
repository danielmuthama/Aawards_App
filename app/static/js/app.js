$(function () {
    toastr.options = {
        "closeButton": true, "debug": false, "newestOnTop": true,
        "progressBar": false, "positionClass": "toast-top-right", "preventDuplicates": true,
        "onclick": null, "showDuration": "300", "hideDuration": "1000", "timeOut": "5000",
        "extendedTimeOut": "1000", "showEasing": "swing", "hideEasing": "linear",
        "showMethod": "fadeIn", "hideMethod": "fadeOut"
    };

    $('#imageUpload').on('change', function () {
        $(this).closest('form').trigger('submit')
    });

    $('[data-bs-toggle="tooltip"]').tooltip()

    $('.share').on('click', function () {
        const url = $(this).data('url')
        const title = $(this).attr('title')
        if (navigator.share) {
            navigator.share({
                title,
                text: url,
                url
            }).then(() => {
                showCopiedTooltip($(this))
            }).catch(err => {
                console.log(`Couldn't share because of`, err.message);
            });
        } else {
            navigator.clipboard.writeText(url);
            showCopiedTooltip($(this))
        }
    });

    $('.project-card .overlay').on('click', function (e) {
        if ($(e.target).hasClass('not-link')) return;
        const url = $(this).data('url');
        window.location.href = url
    })
})

const showCopiedTooltip = function (element, delay = 3000) {
    element.attr('data-bs-original-title', 'Url copied!')
    element.tooltip("show")
    setTimeout(() => {
        element.attr('data-bs-original-title', 'Copy image url')
        element.tooltip("hide")
    }, delay)
}