function flash_close() {
    alert("bonjour");
    setTimeout(function time() {
        $("#{% if message.result %}success{% else %}error{% endif %}").addClass('inactive');
    }, 3000)
}