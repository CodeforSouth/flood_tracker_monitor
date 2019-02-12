function generateMarkers(DeviceObject, map){
    return new google.maps.Marker({
        position: {lat: DeviceObject.latitude, lng:DeviceObject.longatuide},
        map: map,
        title: DeviceObject.name
    });
}

async function initMap() {
    const miami = {lat: 25.727345, lng: -80.233346};
    const map = new google.maps.Map(document.getElementById('map'), {zoom: 10, center: miami});
    const response = await fetch('/api/devices').then( response => response.json());
    const markers = response.data.map(element => {
        console.log(element)
                return generateMarkers(element, map);            
  });
  console.log(markers)

}