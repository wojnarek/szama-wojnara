<template>
  <transition name="modal-fade">
    <div
      v-if="point"
      class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 z-[10000]"
      @click.self="onClose"
    >
      <div
        class="bg-white rounded-3xl shadow-2xl w-full max-w-lg p-0 relative animate-modal-pop border border-gray-100"
        style="max-width:80vw;"
      >
        <button
          @click="onClose"
          class="absolute top-5 right-5 w-8 h-8 flex items-center justify-center rounded-full bg-red-500 hover:bg-red-600 shadow text-white text-lg"
          aria-label="Zamknij"
          style="z-index:2"
        >&#10005;</button>

        <div class="px-7 pt-9 pb-3 flex flex-col items-center">
          <h2 class="text-2xl font-extrabold text-blue-700 tracking-tight mb-2 text-center">{{ point.name }}</h2>
          <span class="inline-block px-3 py-1 rounded-full bg-blue-100 text-blue-700 font-semibold text-xs uppercase tracking-wide shadow-sm mb-1">
            {{ point.main_category }}
          </span>
        </div>
        <div class="border-t border-gray-200 mx-7"></div>

        <div v-if="point.subcategories?.length" class="px-7 py-4 flex flex-wrap gap-2 justify-center">
          <span
            v-for="(cat, i) in point.subcategories"
            :key="i"
            class="bg-gray-100 text-gray-800 px-3 py-1 rounded-lg font-medium text-sm text-center border border-gray-200"
          >{{ cat }}</span>
        </div>
        <div v-else class="px-7 py-4 text-gray-400 text-sm italic text-center">Brak podkategorii</div>
        <div class="border-t border-gray-200 mx-7"></div>

        <div class="px-7 py-5 text-gray-800 text-base leading-snug flex items-center gap-2">
          <span class="text-xl text-blue-500">📝</span>
          <span>{{ point.description }}</span>
          <span>{{ point.owner }}</span>
        </div>
        <div class="border-t border-gray-200 mx-7"></div>

        <div class="flex gap-3 px-7 py-6 justify-center">
          <button
            :disabled="!point.website_url"
            @click="openUrl(point.website_url)"
            class="w-12 h-12 flex items-center justify-center rounded-xl border bg-gray-100 hover:bg-gray-200 transition text-gray-600 disabled:opacity-50 disabled:cursor-not-allowed shadow"
            aria-label="Strona www"
          >
            <svg class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
              <circle cx="12" cy="12" r="10" />
              <path d="M2 12h20M12 2a15.3 15.3 0 0 1 0 20M12 2a15.3 15.3 0 0 0 0 20" />
            </svg>
          </button>
          <a
            :href="point.google_url"
            target="_blank"
            class="w-12 h-12 flex items-center justify-center rounded-xl border bg-green-100 hover:bg-green-200 transition text-green-800 shadow"
            aria-label="Mapa"
          >
            <svg class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
              <path d="M21 10.5A8.38 8.38 0 0 1 12.11 21c-4.36 0-7.88-3.52-7.88-7.88A8.38 8.38 0 0 1 12.11 3c4.36 0 7.89 3.52 7.89 7.5Z"/>
              <circle cx="12" cy="11.5" r="3.5"/>
            </svg>
          </a>
          <button
            @click="shareLocation"
            class="w-12 h-12 flex items-center justify-center rounded-xl border bg-blue-100 hover:bg-blue-200 transition text-blue-700 shadow"
            aria-label="Udostępnij"
          >
            <svg class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
              <path d="M4 12v-2a4 4 0 1 1 8 0v2m0 0v2a4 4 0 1 0 8 0v-2M12 14v-4" />
            </svg>
          </button>
        </div>
        <div
          v-if="showAlert"
          class="absolute left-1/2 bottom-4 -translate-x-1/2 px-5 py-2 bg-blue-600 text-white rounded-lg shadow font-medium animate-modal-pop"
        >
          Link skopiowany do schowka!
        </div>
        <div
          v-if="copyError"
          class="absolute left-1/2 bottom-4 -translate-x-1/2 px-5 py-2 bg-red-600 text-white rounded-lg shadow font-medium animate-modal-pop"
        >
          Nie udało się skopiować linku. Skopiuj ręcznie: {{ copyUrl }}
        </div>
      </div>
    </div>
  </transition>
</template>

<script setup>
import { ref } from 'vue'
const props = defineProps({
  point: Object
})
const emit = defineEmits(['close'])
const showAlert = ref(false)
const copyError = ref(false)
const copyUrl = ref('')

function onClose() {
  emit('close')
}

function openUrl(url) {
  if (url) window.open(url, '_blank')
}

function shareLocation() {
  const url = `${window.location.origin}/?pointId=${props.point.id}`
  if (navigator.clipboard && navigator.clipboard.writeText) {
    navigator.clipboard.writeText(url)
      .then(() => {
        showAlert.value = true
        setTimeout(() => showAlert.value = false, 2000)
      })
      .catch(() => {
        copyUrl.value = url
        copyError.value = true
        setTimeout(() => copyError.value = false, 3500)
      })
  } else {
    copyUrl.value = url
    copyError.value = true
    setTimeout(() => copyError.value = false, 3500)
  }
}
</script>

<style scoped>
@keyframes modal-pop {
  0% {
    opacity: 0;
    transform: scale(0.8) translateY(30px);
  }
  100% {
    opacity: 1;
    transform: scale(1) translateY(0);
  }
}
.animate-modal-pop {
  animation: modal-pop 0.32s cubic-bezier(.4,1.2,.6,1) both;
}
.modal-fade-enter-active,
.modal-fade-leave-active {
  transition: opacity 0.24s;
}
.modal-fade-enter-from,
.modal-fade-leave-to {
  opacity: 0;
}
</style>
