<template>
  <div class="bg-white rounded-2xl shadow-md px-4 py-4 w-64 flex flex-col items-center border border-gray-100">
    <!-- Point name -->
    <div class="text-lg font-extrabold text-blue-700 text-center mb-1">
      {{ point.name }}
    </div>
    <!-- Main category -->
    <span class="inline-block px-3 py-1 mb-2 rounded-full bg-blue-100 text-blue-700 font-semibold text-xs uppercase tracking-wide shadow-sm">
      {{ point.main_category }}
    </span>
    <!-- Subcategories -->
    <div v-if="point.subcategories?.length" class="flex flex-wrap justify-center gap-1 mb-2">
      <span
        v-for="(cat, i) in point.subcategories"
        :key="i"
        class="bg-gray-100 text-gray-800 px-2 py-1 rounded-full font-medium text-xs"
      >{{ cat }}</span>
    </div>
    <div v-else class="text-gray-400 italic text-xs mb-2">Brak podkategorii</div>
    <!-- More button -->
    <button
      @click="handleMoreClick"
      :disabled="loading"
      class="w-9 h-9 flex items-center justify-center rounded-full bg-blue-600 hover:bg-blue-700 transition text-white shadow-lg mt-2"
      title="Więcej informacji"
    >
      <svg v-if="!loading" class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2.2" viewBox="0 0 24 24">
        <path d="M9 18l6-6-6-6"/>
      </svg>
      <svg v-else class="w-5 h-5 animate-spin" viewBox="0 0 24 24">
        <circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4" fill="none"/>
      </svg>
    </button>
    <div v-if="error" class="text-xs text-red-500 mt-2">{{ error }}</div>
  </div>
</template>

<script setup>
import axios from 'axios'
import { ref } from 'vue'

const props = defineProps({
  point: Object
})
const emit = defineEmits(['more'])

const loading = ref(false)
const error = ref(null)

async function handleMoreClick() {
  loading.value = true
  error.value = null
  try {
    const res = await axios.get(import.meta.env.VITE_API_URL + '/points/' + props.point.id)
    emit('more', res.data) //emit data to parent
  } catch (e) {
    error.value = "Nie udało się pobrać szczegółów."
  } finally {
    loading.value = false
  }
}
</script>
