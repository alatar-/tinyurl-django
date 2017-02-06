$(document).ready(function() {
    $('.panel-body').each(function() {
        var text = $(this).find('a').text();
        var button = $(this).find('button');

        button.bind('click', {'text': text}, onCopyButtonClick);
    });
});

function onCopyButtonClick(event) {
    copyToClipboard(event.data.text);
}

function copyToClipboard(text) {
    // http://stackoverflow.com/a/30905277
    var $temp = $("<input>");
    $("body").append($temp);
    $temp.val(text).select();
    document.execCommand("copy");
    $temp.remove();
}
