<template>
  <div class="point-modal-overlay fixed inset-0 flex items-center justify-center bg-black bg-opacity-40 z-50" @click.self="onClose">
    <div class="bg-white rounded-xl p-6 max-w-md w-full shadow-lg animate-fade-in">
      <h2 class="text-xl font-bold mb-2">{{ point.name }}</h2>
      <div class="mb-1"><span class="font-semibold">Kategoria:</span> {{ point.main_category }}</div>
      <div class="mb-1"><span class="font-semibold">Podkategorie:</span>
        <span v-if="point.subcategories?.length">{{ point.subcategories.join(', ') }}</span>
        <span v-else>brak</span>
      </div>
      <div class="mb-2"><span class="font-semibold">Opis:</span> {{ point.description }}</div>
      <div class="mb-2">
        <span class="font-semibold">Google Maps:</span>
        <a :href="point.google_url" target="_blank" class="text-blue-600 underline">Pokaż na mapie</a>
      </div>
      <button class="mt-4 px-4 py-2 rounded-md bg-blue-600 text-white" @click="onClose">Zamknij</button>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  point: Object
})
const emit = defineEmits(['close'])
function onClose() {
  emit('close')
}
</script>

<style>
@keyframes fade-in {
  from { opacity: 0; transform: translateY(50px);}
  to { opacity: 1; transform: translateY(0);}
}
.animate-fade-in {
  animation: fade-in 0.3s;
}

.point-modal-overlay {
  position: fixed;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(0,0,0,0.4);
  z-index: 10000 !important; 
}
</style>
