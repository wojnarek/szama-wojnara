<template>
  <div class="map-container relative w-full h-[90vh]">
    <div id="map" class="absolute inset-0 w-full h-full"></div>
    <div id="popup-container" style="display:none;"></div>
    <PointModal v-if="selectedPoint" :point="selectedPoint" @close="selectedPoint = null" />

    <transition name="modal-fade">
      <div
        v-if="showNewMarkerForm"
        class="fixed inset-0 bg-black bg-opacity-40 flex items-center justify-center z-[9999]"
      >
        <NewMarker
          :latitude="newMarkerLat"
          :longitude="newMarkerLng"
          @close="handleCloseForm"
          @submit="handleCloseForm" />
      </div>
    </transition>
  </div>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'
import { render, h } from 'vue'
import L from 'leaflet'
import 'leaflet/dist/leaflet.css'
import axios from 'axios'

import kebabIcon from '@/assets/markers/kebab.png'
import pizzaIcon from '@/assets/markers/pizza.png'
import hamburgerIcon from '@/assets/markers/hamburger.png'
import restaurantIcon from '@/assets/markers/restaurant.png'
import karczmaIcon from '@/assets/markers/karczma.png'
import mexicoIcon from '@/assets/markers/mexico.png'
import sushiIcon from '@/assets/markers/sushi.png'
import chineseIcon from '@/assets/markers/chinese.png'
import fancy_restaurantIcon from '@/assets/markers/fancy_restaurant.png'

import SmallPop from '@/components/SmallPopup.vue'
import PointModal from '@/components/PointModal.vue'
import NewMarker from '@/components/NewMarker.vue'

const showNewMarkerForm = ref(false)
const newMarkerLat = ref(null)
const newMarkerLng = ref(null)

const points = ref([])
const selectedPoint = ref(null)
const urlPointId = ref(null)
let map

function getMarkerIcon(category) {
  const normalized = (category || '')
  let iconUrl
  switch (normalized) {
    case 'Kebab': iconUrl = kebabIcon; break
    case 'Pizza': iconUrl = pizzaIcon; break
    case 'Hamburger': iconUrl = hamburgerIcon; break
    case 'Restauracja': iconUrl = restaurantIcon; break
    case 'Karczma': iconUrl = karczmaIcon; break
    case 'Meksykańskie': iconUrl = mexicoIcon; break
    case 'Sushi': iconUrl = sushiIcon; break
    case 'Chinol': iconUrl = chineseIcon; break
    case 'Wykwintna restauracja': iconUrl = fancy_restaurantIcon; break
    default: iconUrl = kebabIcon
  }
  return L.icon({
    iconUrl,
    iconSize: [35, 35], 
    iconAnchor: [19, 38], 
    popupAnchor: [0, -36],
    className: "custom-marker-icon"
  })
}

function handleShowPointModal(e) {
  selectedPoint.value = e.detail
}

function handleCloseForm() {
  showNewMarkerForm.value = false
  newMarkerLat.value = null
  newMarkerLng.value = null
}

onMounted(() => {
  window.addEventListener('show-point-modal', handleShowPointModal)
})

onBeforeUnmount(() => {
  window.removeEventListener('show-point-modal', handleShowPointModal)
})

onMounted(async () => {
  const params = new URLSearchParams(window.location.search)
  urlPointId.value = params.get('pointId')

  const res = await axios.get(import.meta.env.VITE_API_URL2 + '/points/')
  points.value = res.data

  const defaultLat = 50.316753
  const defaultLng = 17.383472
  const defaultZoom = 15

  map = L.map('map').setView([defaultLat, defaultLng], defaultZoom)

  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
  }).addTo(map)

  points.value.forEach(point => {
    const container = document.createElement('div')
    container.id = `popup-vue-${point.id}`

    render(
      h(SmallPop, { point }),
      container
    )

    const marker = L.marker([point.latitude, point.longitude],
      {icon: getMarkerIcon(point.main_category)}
    ).addTo(map)
    marker.bindPopup(container)

    if (urlPointId && point.id === urlPointId) {
      axios.get(`${import.meta.env.VITE_API_URL2}/points/${point.id}`)
        .then(res => {
          selectedPoint.value = res.data
          marker.openPopup()
        })
        .catch(() => { /* ignoruj */ })
    }
  })

  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(
      (position) => {
        const { latitude, longitude } = position.coords
        map.setView([latitude, longitude], defaultZoom)
      },
      (err) => {
        console.warn('Nie udało się pobrać lokalizacji:', err.message)
      }
    )
  } else {
    console.warn('Twoja przeglądarka nie obsługuje geolokalizacji.')
  }

  map.on('dblclick', function(e) {
    newMarkerLat.value = e.latlng.lat
    newMarkerLng.value = e.latlng.lng
    showNewMarkerForm.value = true
  })
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
