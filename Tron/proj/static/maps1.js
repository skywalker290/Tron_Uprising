function initMap(lat,lng) {
    var map = new google.maps.Map(document.getElementById('map'), {
      zoom: 11,
      center: { lat: 28.4089, lng: 77.3178 }
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

  function geocodeAddress(address, callback) {
    // Initialize the Geocoder object
    var geocoder = new google.maps.Geocoder();
    
    // Call the geocode method to convert the address to latitude and longitude
    geocoder.geocode({ address: address }, function(results, status) {
      // If the geocode was successful
      if (status === google.maps.GeocoderStatus.OK) {
        // Extract the latitude and longitude from the first result
        var lat = results[0].geometry.location.lat();
        var lng = results[0].geometry.location.lng();
        
        // Create an object with the latitude and longitude
        var coords = { lat: lat, lng: lng };
        
        // Call the callback function with the coordinates
        callback(coords);
      } else {
        // If the geocode was not successful, log an error message
        console.error('Geocode was not successful for the following reason: ' + status);
      }
    });
  }
  