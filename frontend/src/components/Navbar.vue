<template>
  <nav class="navbar">
    <div class="container">
      <div class="flex-1"></div>
<div class="search-wrapper relative w-full flex justify-center items-center">
  <svg
    class="absolute left-4 top-1/2 -translate-y-1/2 text-gray-400 w-7 h-7 pointer-events-none"
    fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"
  >
    <circle cx="11" cy="11" r="8" />
    <line x1="21" y1="21" x2="16.65" y2="16.65" />
  </svg>
  <input
    type="text"
    v-model="search"
    class="search-input w-full sm:w-80 md:w-96 max-w-lg h-12 p-3 rounded-full border border-gray-300 outline-none transition-all duration-300 bg-white text-gray-900 text-lg shadow focus:ring-2 focus:ring-blue-400 focus:scale-105 focus:shadow-lg focus:border-blue-400 pl-12"
    placeholder="Wyszukaj lokalizację lub miejsce..."
  />
</div>
      <div class="flex-1"></div>
    </div>
  </nav>
</template>

<script setup>
import { ref } from 'vue'
const search = ref('')
const focused = ref(false)
</script>
