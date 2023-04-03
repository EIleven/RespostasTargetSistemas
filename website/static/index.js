function deleteNote(noteId) {
    fetch(`/?id=${noteId}`, {
        method: "DELETE",
    }).then((_res) => {
        window.location.href = "/";
    });
}


window.addEventListener('scroll', function() {
    sessionData = {
        'scrollPosition': window.scrollY
    };
    
    sessionStorage.setItem('sessionData', JSON.stringify(sessionData));
});

window.onload = function() {
    if (sessionStorage.getItem('sessionData')) {
        var sessionData = JSON.parse(sessionStorage.getItem('sessionData'));
        window.scrollTo(0, sessionData.scrollPosition);
    }
};