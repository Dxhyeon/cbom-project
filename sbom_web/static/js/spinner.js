const spinnerBox = document.getElementById('spinner-box')
const responseDiv = document.getElementById('response')

$('#upload-btn').on('click', function () {
    // Show the spinner box
    spinnerBox.classList.remove('not-visible');

    $.ajax({
        // Your AJAX settings go here
        beforeSend: function () {
            responseDiv.classList.add('hidden');
        },
        complete: function () {

            setTimeout(function() {
                spinnerBox.classList.add('not-visible');
            }, 60000);
        },
    });
});