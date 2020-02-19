var currentPhotoCount = document.getElementById("progressMarker");
var output = document.getElementById("curPhoto");
output.innerHTML = currentPhotoCount.value + '/' + currentPhotoCount.max;

currentPhotoCount.oninput = function() {
    setPhoto(this.value)
}

function getPhoto() {
    let currentPhoto = document.getElementById("plantPhoto").attributes.src;
    let photoLoc = Number(currentPhoto.value.search(/\/photos\//i)) + 8;
    let jpgLoc= Number(currentPhoto.value.search(/jpg/i)) - 1;
    
    return Number(currentPhoto.value.substring(photoLoc, jpgLoc));
}

function setPhoto(value) {
    let currentPhoto = document.getElementById("plantPhoto").attributes.src;
    let photoLoc = Number(currentPhoto.value.search(/\/photos\//i)) + 8;
    
    document.getElementById("plantPhoto").src = currentPhoto.value.substring(0,photoLoc) + value + '.jpg';
    output.innerHTML = value + '/' + currentPhotoCount.max;
    document.getElementById("progressMarker").value = value;
}

function play() {
    alert("Play button temporarily broken while I learn async!")
}

function first() {
    setPhoto(1);
}

function last() {
    setPhoto(currentPhotoCount.max);
}

function next() {
    let curPhoto = getPhoto();
    if (curPhoto < currentPhotoCount.max) {
        setPhoto(curPhoto + 1)
    }
}

function prev() {
    let curPhoto = getPhoto();
    if (curPhoto > 1) {
        setPhoto(curPhoto - 1)
    }
}



$('img[data-enlargable]').addClass('img-enlargable').click(function(){
    var src = $(this).attr('src');
    $('<div>').css({
        background: 'RGBA(0,0,0,.5) url('+src+') no-repeat center',
        backgroundSize: 'contain',
        width:'100%', height:'100%',
        position:'fixed',
        zIndex:'10000',
        top:'0', left:'0',
        cursor: 'zoom-out'
    }).click(function(){
        $(this).remove();
    }).appendTo('body');
});