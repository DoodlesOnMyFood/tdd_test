var init = function (){
    $('input[name="text"]').on('keypress', function (){
        $('.has-error').hide();
    });
};
console.log('list.js loaded')
