

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

    const numStars = 75; 
    const starContainer = document.getElementById('starry-background');

        for (let i = 0; i < numStars; i++) {
            const star = document.createElement('div');
            star.className = 'star';
            star.style.width = Math.random() * 5 + 'px'; // Random star size
            star.style.height = star.style.width;
            star.style.left = Math.random() * 100 + 'px'; // Random horizontal position
            star.style.top = Math.random() * 100 + 'px'; // Random vertical position
            star.style.animationDuration = Math.random() * 5 + 2 + 's'; // Random twinkle speed
            starContainer.appendChild(star);
        }

    function initMap() {
        const myLatlng = { lat: -25.363, lng: 131.044 };
        const map = new google.maps.Map(document.getElementById("map"), {
            zoom: 2,
            center: myLatlng,
            restriction: {
                latLngBounds: {
                north: 80,
                south: -80,
                east: 180,
                west: -180,
                },
            },

        });
        // Create the initial InfoWindow.
        let infoWindow = new google.maps.InfoWindow({
            content: "Click the map to get Lat/Lng!",
            position: myLatlng,
        });

        infoWindow.open(map);
        // Configure the click listener.
        map.setOptions({draggable: true, zoomControl: false, scrollwheel: false, disableDoubleClickZoom: true});
        map.addListener("click", (mapsMouseEvent) => {
            // Close the current InfoWindow.
            infoWindow.close();
            // Create a new InfoWindow.
            infoWindow = new google.maps.InfoWindow({
            position: mapsMouseEvent.latLng,
            });
            infoWindow.setContent(
            JSON.stringify(mapsMouseEvent.latLng.toJSON(), null, 2),
            );
            infoWindow.open(map);
        });
        }

        window.initMap = initMap;
        
    let navHeight = document.querySelector('nav').clientHeight;

    
    let landingContent = document.getElementById('landing');
    landingContent.style.paddingTop = navHeight * (navHeight * 0.1) + 'px';
    landingContent.style.height = 'calc(100vh - ' + (navHeight + (navHeight * 0.9)) * 2 + 'px)'; 
    
    

});