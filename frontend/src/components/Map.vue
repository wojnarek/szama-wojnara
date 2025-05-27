<template>
  <div class="map-container relative w-full h-[90vh]">
    <div id="map" class="absolute inset-0 w-full h-full"></div>
    <div id="popup-container" style="display:none;"></div>
    <PointModal v-if="selectedPoint" :point="selectedPoint" @close="selectedPoint = null" />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { render, h } from 'vue'
import L from 'leaflet'
import 'leaflet/dist/leaflet.css'
import axios from 'axios'

import SmallPop from '@/components/SmallPopup.vue'
import PointModal from '@/components/PointModal.vue'

const points = ref([])
const selectedPoint = ref(null)
const urlPointId = ref(null)
let map
onMounted(async () => {
  const params = new URLSearchParams(window.location.search)
  urlPointId.value = params.get('pointId')

  const res = await axios.get(import.meta.env.VITE_API_URL + '/points/')
  points.value = res.data

//default location, my city
  const defaultLat = 50.316753
  const defaultLng = 17.383472
  const defaultZoom = 15

  //set map to defualt location
  const map = L.map('map').setView([defaultLat, defaultLng], defaultZoom)

  

  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
  }).addTo(map)

 points.value.forEach(point => {
    //Container for markers
    const container = document.createElement('div')
    container.id = `popup-vue-${point.id}`

    //Smallpopup render
    render(
      h(SmallPop, {
        point,
        onMore: () => {
          selectedPoint.value = point
          map.closePopup()
        }
      }),
      container
    )

    const marker = L.marker([point.latitude, point.longitude]).addTo(map)
    marker.bindPopup(container)

    if (urlPointId && point.id === urlPointId) {
      selectedPoint.value = point
      map.setView([point.latitude, point.longitude], 16)
      marker.openPopup()
}


  })




  //get user location
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(
      (position) => {
        const { latitude, longitude } = position.coords
        map.setView([latitude, longitude], defaultZoom)

      },
      (err) => {
        //access = no, no location :()
        console.warn('Nie udało się pobrać lokalizacji:', err.message)
      }
    )
  } else {
    // browser does not support geolocation
    console.warn('Twoja przeglądarka nie obsługuje geolokalizacji.')
  }
})
</script>

<style>

.map-container {
  width: 100%;
  height: 90vh;
  min-height: 300px;
}
#map {
  width: 100%;
  height: 100%;
}
</style>
