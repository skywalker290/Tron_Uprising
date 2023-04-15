var x = document.getElementById("location");
function getPreciseLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showExactPosition)
  } else {
    x.innerHTML = "Geolocation is not supported"
  }
}
function showExactPosition(position) {
  initMap(position.coords.latitude, position.coords.longitude);
}

function initMap(lati,long) {
var map = new google.maps.Map(document.getElementById('map'), {
zoom: 11,
center: { lat: lati, lng: long }
});



var request = {
location: map.getCenter(),
radius: '5000',
type: ['art_gallery']
};

var service = new google.maps.places.PlacesService(map);
service.nearbySearch(request, callback);

function callback(results, status) {
if (status == google.maps.places.PlacesServiceStatus.OK) {
  for (var i = 0; i < results.length; i++) {
    createMarker(results[i]);
  }
}
}

function createMarker(place) {
var marker = new google.maps.Marker({
  map: map,
  position: place.geometry.location
});

google.maps.event.addListener(marker, 'click', function() {
  var infowindow = new google.maps.InfoWindow({
    content: place.name
  });
  infowindow.open(map, this);
});
}
}