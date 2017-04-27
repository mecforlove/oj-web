/* ------------------------------------------------------------------------------
 *
 *  # Template JS core
 *
 *  Core JS file with default functionality configuration
 *
 *  Version: 1.1
 *  Latest update: Oct 20, 2015
 *
 * ---------------------------------------------------------------------------- */

$(function () {

    //pnotify infos
    if ($(".hidden-message")) {
        var $hidenMsg = $(".hidden-message");
        for (var i = 0, len = $hidenMsg.length; i < len; i++) {
            (function (dom) {
                var category = $(dom).data("category");
                var message = $(dom).data("message");
                var classKey = {
                    error: "bg-danger",
                    info: "bg-info",
                    success: "bg-success",
                    warning: "bg-warning"
                };

                if (message) {
                    setTimeout(function () {
                        getNotify({
                            addclass: classKey[category],
                            text: message
                            //delay: (i + 1) * 750
                        });
                    }, i * 400);
                }
            })($hidenMsg[i]);
        }
    }


});


function getNotify(obj) {
    new PNotify(obj);
}
