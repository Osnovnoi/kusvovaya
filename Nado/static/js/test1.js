$(document).ready(function(){
    $('#chat-form').on('submit',function(event){
    event.preventDefault();
    ajax();
});
});
function ajax(){
   var mes = document.getElementById('chat-msg').value;
   var id = document.getElementById('id').value;
   console.log(mes);
   $.ajax({
    type : 'POST',
    url: '/Step1/general_page/'+id+'/',
    data: {msgbox: mes },
    success: function(json){
            $('#chat-msg').val('');
            $('#msg-list').append('<li class="mes">' + json.msg +'</li>');
            var message_list = document.getElementById('msg-list-div');
            message_list.scrollTop = message_list.scrollHeight;
        }

});
}
    
$(document).ready(function() {
     $('#chat-submit').attr('disabled','disabled');
     $('#chat-msg').keyup(function() {
        if($(this).val() != '') {
            $('#chat-submit').removeAttr('disabled');
        }
        else {
            $('#chat-submit').attr('disabled','disabled');
        }
     });
 });
$(document).ready(function() {
     $('#create').attr('disabled','disabled');
     $('#room').keyup(function() {
        if($(this).val() != '') {
            $('#create').removeAttr('disabled');
        }
        else {
            $('#create').attr('disabled','disabled');
        }
     });
 });

function get_masseges(){
    console.log('1');
    if (!scrolling){
        console.log('2');
        var id = document.getElementById('id');

        $.get('/messages/'+id.value+'/',function(messages){
            console.log('2');
            $('#msg-list').html(messages);
            console.log(messages);
            console.log($('#msg-list').html(messages));
            console.log('2');
            var message_list = document.getElementById('msg-list-div');
            message_list.scrollTop = message_list.scrollHeight;
        });
    }
    scrolling = false;
}
var scrolling = false;
$(function(){
    $('#msg-list-div').on('scroll',function(){
        scrolling = true;
    });
    refresh = setInterval(get_masseges,500);
});


function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});