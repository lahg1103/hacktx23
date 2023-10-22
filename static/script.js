

  let map;

  async function initMap() {
    const { Map } = await google.maps.importLibrary("maps");
  
    map = new Map(document.getElementById("map"), {
      center: { lat: -34.397, lng: 150.644 },
      zoom: 0,
    });
  }
  
  initMap();


  window.addEventListener('DOMContentLoaded', () => {

    function random(range, unit) {
    let randNum = Math.floor(Math.random() * range) + 1;
    return `$(randNum)$(unit)`;
    }
    function createStar(s) {
            let star = document.createElement('div');
            star.classList.add('star');

            let randRange = Math.floor(Math.random() * 5) + 1;
            star.classList.add(`blink_${randRange}`);

            let widthAndHeight = random(s, 'px');
            star.style.height = star.style.width = widthAndHeight;

            star.style.left = random(window.innerWidth, 'px');
            star.style.top = random(window.innerHeight, 'px');

            sky.appendChild(star);
        }
    function renderStar(stars, size) {
        while (sky.firstChild) {
            sky.removeChild(sky.firstChild);
        }
        for (let i = 0; i < stars; i++) {
            createStar(size);
        }
    }

    let navHeight = document.querySelector('nav').clientHeight;

    
    let landingContent = document.getElementById('landing');
    landingContent.style.paddingTop = navHeight * (navHeight * 0.1) + 'px';
    landingContent.style.height = 'calc(100vh - ' + (navHeight + (navHeight * 0.9)) * 2 + 'px)'; 
    
    var sky = document.querySelector('.sky');
    
    renderStar(50, 4);
});