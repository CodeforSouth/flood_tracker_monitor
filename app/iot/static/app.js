function generateMarkers(deviceObject, map){
    const marker =  new google.maps.Marker({
        position: {lat: deviceObject.latitude, lng:deviceObject.longatuide},
        map: map,
        title: deviceObject.name
    });
    addMarkerClickHandler(deviceObject, map, marker);
    addDeviceClickHandler(deviceObject, map, marker);
    return marker;
}

async function initMap() {
    const miami = {lat: 25.727345, lng: -80.233346};
    const map = new google.maps.Map(document.getElementById('map'), {zoom: 10, center: miami});
    const response = await fetch('/api/devices').then( response => response.json());
    response.data.map(element => {
                return generateMarkers(element, map);       
  });
  return map     
}

function getDeviceRadioElement(device){
    return document.getElementById(`device-${device.id -1}`);
}

function changeDeviceSelection(device) {
    const element = getDeviceRadioElement(device);
    if (element){
    element.checked = true;
    return true;
    }
    return false;
}

function addDeviceClickHandler(device, map, marker){
    const element = getDeviceRadioElement(device)
    return element ? element.addEventListener('click', function() {
    map.setZoom(14);
    map.setCenter(marker.getPosition());
    }) : null;
}

function addMarkerClickHandler(device, map, marker){
    marker.addListener('click', function() {
        map.setZoom(14);
        map.setCenter(marker.getPosition());
        changeDeviceSelection(device)
      });
}
