const menuBtn = document.querySelector('.menu-btn');
const menuLinks = document.querySelector('.menu-links');

menuBtn.addEventListener('click', () => {
  if (menuLinks.style.display === 'block') {
    menuLinks.style.display = 'none';
  } else {
    menuLinks.style.display = 'block';
  }
});

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
