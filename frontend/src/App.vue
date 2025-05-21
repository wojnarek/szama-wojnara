<template>
  <div class="app-container">
    <header class="navbar">
      <div class="nav-content">
        <h1>Moja Mapa</h1>
        <input
          type="text"
          v-model="search"
          placeholder="Szukaj..."
          class="search-input"
        />
      </div>
    </header>
    <div id="map" class="map-container"></div>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import L from 'leaflet'
import 'leaflet/dist/leaflet.css'

const search = ref('')

onMounted(() => {
  const map = L.map('map').setView([52.2297, 21.0122], 13) // Warszawa jako domyślna lokalizacja

  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '© OpenStreetMap'
  }).addTo(map)
})
</script>

<style>
/* Leaflet map height needs to be set explicitly */
html, body, #app, .app-container {
  height: 100%;
  margin: 0;
  padding: 0;
}

.app-container {
  height: 100vh;
  display: flex;
  flex-direction: column;
}

.navbar {
  position: sticky;
  top: 0;
  width: 100%;
  background: #1e293b;
  color: white;
  z-index: 10;
  padding: 0.5rem 0;
  box-shadow: 0 2px 8px rgba(30, 41, 59, 0.08);
}

.nav-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
  max-width: 900px;
  margin: 0 auto;
  width: 100%;
  padding: 0 1rem;
}

.search-input {
  padding: 0.4rem 1rem;
  border-radius: 999px;
  border: none;
  outline: none;
  font-size: 1rem;
  min-width: 180px;
}

.map-container {
  flex: 1 1 0%;
  width: 100%;
  height: 100%;
  min-height: 0;
}
</style>
