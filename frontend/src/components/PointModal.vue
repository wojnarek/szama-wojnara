<template>
  <transition name="modal-fade">
    <div
      v-if="point"
      class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 z-[10000]"
      @click.self="onClose"
    >
      <div
        class="bg-white rounded-2xl shadow-2xl w-full max-w-md p-8 relative animate-modal-pop"
        style="max-width:90vw;"
      >
        <!-- Zamknięcie X -->
        <button
          @click="onClose"
          class="absolute top-4 right-4 text-gray-500 hover:text-blue-600 text-xl"
        >&times;</button>

        <h2 class="text-2xl font-extrabold mb-3 text-blue-700 tracking-tight">
          {{ point.name }}
        </h2>

        <div class="mb-2">
          <span class="inline-block px-3 py-1 rounded-full bg-blue-100 text-blue-700 font-semibold text-sm">
            {{ point.main_category }}
          </span>
        </div>

        <div class="mb-4">
          <div class="font-semibold mb-1 text-gray-700">Podkategorie:</div>
          <div>
            <template v-if="showAllSub || point.subcategories.length <= 3">
              <span
                v-for="(cat, i) in point.subcategories"
                :key="i"
                class="inline-block bg-gray-200 text-gray-700 px-2 py-1 rounded-full mr-2 mb-1 text-xs"
              >{{ cat }}</span>
            </template>
            <template v-else>
              <span
                v-for="(cat, i) in point.subcategories.slice(0, 3)"
                :key="i"
                class="inline-block bg-gray-200 text-gray-700 px-2 py-1 rounded-full mr-2 mb-1 text-xs"
              >{{ cat }}</span>
              <button
                @click="showAllSub = true"
                class="ml-2 text-blue-600 underline text-xs"
              >+{{ point.subcategories.length - 3 }} więcej</button>
            </template>
            <button
              v-if="showAllSub && point.subcategories.length > 3"
              @click="showAllSub = false"
              class="ml-2 text-blue-600 underline text-xs"
            >Pokaż mniej</button>
          </div>
        </div>

        <div class="mb-4 text-gray-800 text-base">
          {{ point.description }}
        </div>

        <a
          :href="point.google_url"
          target="_blank"
          class="block text-center bg-green-600 text-white rounded-lg px-4 py-2 font-semibold shadow hover:bg-green-700 transition"
        >Zobacz w Google Maps</a>
      </div>
    </div>
  </transition>
</template>

<script setup>
import { ref, watch } from 'vue'
const props = defineProps({
  point: Object
})
const emit = defineEmits(['close'])
const showAllSub = ref(false)

watch(() => props.point, () => {
  showAllSub.value = false // Resetuj po każdej zmianie punktu
})

function onClose() {
  emit('close')
}
</script>

<style scoped>
@keyframes modal-pop {
  0% {
    opacity: 0;
    transform: scale(0.85) translateY(40px);
  }
  100% {
    opacity: 1;
    transform: scale(1) translateY(0);
  }
}
.animate-modal-pop {
  animation: modal-pop 0.32s cubic-bezier(.44,1.5,.6,1) both;
}
.modal-fade-enter-active,
.modal-fade-leave-active {
  transition: opacity 0.25s;
}
.modal-fade-enter-from,
.modal-fade-leave-to {
  opacity: 0;
}
</style>