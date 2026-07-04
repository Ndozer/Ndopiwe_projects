$(".album").turn();
$(document).keydown(function(e) {
        switch (e.keyCode) {
            case 37: //ascii left
                $('.album').turn('previous');
                break;
            case 39://ascii right
                $('.album').turn('next');
                break;
        }
    });
$('.add-photo').on('click', function(e) {
    if ($(e.target).is('input')) return; 
        $(this).find('input[type="file"]').trigger('click');
    });

$('.add-photo input[type="file"]').on('change', function(e) {
    const file = e.target.files[0];
    const $button = $(this).parent('.add-photo');

    if (file) {
        const reader = new FileReader();
                
        reader.onload = function(event) {
            $button.css({
                'background-image': `url(${event.target.result})`,
                'background-size': 'cover',
                'background-position': 'center',
                'border': 'none'
            });
            $button.find('span').hide();
        };
                
        reader.readAsDataURL(file);
    }
});
var title = document.getElementById('title');
var end_title = document.getElementById('end-title');
var front_cover = document.getElementById('front-cover');
var back_cover = document.getElementById('back-cover');
var edit_btn = document.getElementById('edit-btn');
var upgrade = document.getElementById('upgrade');
var account = document.getElementById('login');

edit_btn.addEventListener('click', function(){
    front_cover.innerText = "";
    back_cover.innerText = "";
    front_cover.innerHTML = `<h1>${title.value}</h1>`;
    back_cover.innerHTML = `<h1>${end_title.value}</h1>`;
});
upgrade.addEventListener('click', function(){
    window.location.href = 'upgrade.html';
});
account.addEventListener('click', function(){
    window.location.href = 'login.html';
});