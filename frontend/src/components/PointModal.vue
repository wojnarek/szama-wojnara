<template>
  <transition name="modal-fade">
    <div
      v-if="point"
      class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 z-[10000] fairy-modal-backdrop"
      @click.self="onClose"
    >
      <div
        class="bg-gradient-to-br from-pink-50 via-yellow-50 to-blue-100 rounded-[2.7rem] shadow-2xl w-full max-w-xl p-0 relative animate-modal-pop fairy-modal font-fredoka border-4 border-pink-200"
        style="max-width:84vw;"
      >
        <!-- Zamknij -->
        <button
          @click="onClose"
          class="absolute top-6 right-6 w-10 h-10 flex items-center justify-center rounded-full bg-red-500 hover:bg-red-600 shadow-2xl text-white text-xl border-4 border-white fairy-close"
          aria-label="Zamknij"
        >&#10005;</button>

        <!-- Ikonka + Nazwa + Kategoria -->
        <div class="px-9 pt-12 pb-5 flex flex-col items-center">
          <img
            :src="getCategoryIcon(point.main_category)"
            alt="ikona kategorii"
            class="w-16 h-16 rounded-full drop-shadow-xl bg-white border-2 border-pink-100 mb-2 fairy-pop"
          />
          <h2 class="text-3xl font-extrabold text-pink-700 tracking-tight mb-1 text-center drop-shadow flex items-center gap-2">
            {{ point.name }}
          </h2>
          <span class="inline-block px-4 py-1 rounded-full bg-gradient-to-r from-pink-200 via-yellow-100 to-blue-100 text-pink-800 font-bold text-xs uppercase tracking-wide shadow fairy-pop mb-2">
            🏷️ {{ point.main_category }}
          </span>
        </div>

        <div class="border-t-2 border-pink-100 mx-10"></div>

        <!-- Subcategories -->
        <div v-if="point.subcategories?.length" class="px-10 py-4 flex flex-wrap gap-2 justify-center">
          <span
            v-for="(cat, i) in point.subcategories"
            :key="cat"
            class="bg-blue-50 text-blue-700 px-3 py-1 rounded-full font-bold text-sm text-center shadow fairy-pop"
          >🔖 {{ cat }}</span>
        </div>
        <div v-else class="px-10 py-4 text-gray-400 text-sm italic text-center">Brak podkategorii</div>

        <div class="border-t-2 border-pink-100 mx-10"></div>

        <!-- Opis i właściciel -->
        <div class="px-10 py-6 text-gray-800 text-base leading-snug flex flex-col sm:flex-row items-center gap-3">
          <span class="text-2xl text-blue-400">📝</span>
          <span class="flex-1 text-center sm:text-left">{{ point.description }}</span>
          <span v-if="point.owner_name" class="flex items-center gap-1 text-purple-700 text-sm font-bold bg-purple-50 px-3 py-1 rounded-full shadow">👤 {{ point.owner_name }}</span>
        </div>

        <div class="border-t-2 border-pink-100 mx-10"></div>

        <!-- Przyciski -->
        <div class="flex gap-5 px-10 py-7 justify-center">
          <button
            :disabled="!point.website_url"
            @click="openUrl(point.website_url)"
            class="w-14 h-14 flex items-center justify-center rounded-2xl border-2 border-purple-100 bg-purple-50 hover:bg-purple-200 transition text-purple-700 disabled:opacity-40 shadow-lg hover:scale-105 fairy-shadow"
            aria-label="Strona www"
          >
            <svg class="w-7 h-7" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
              <circle cx="12" cy="12" r="10" />
              <path d="M2 12h20M12 2a15.3 15.3 0 0 1 0 20M12 2a15.3 15.3 0 0 0 0 20" />
            </svg>
          </button>
          <a
            :href="point.google_url"
            target="_blank"
            class="w-14 h-14 flex items-center justify-center rounded-2xl border-2 border-green-100 bg-green-50 hover:bg-green-200 transition text-green-700 shadow-lg hover:scale-105 fairy-shadow"
            aria-label="Mapa"
          >
            <svg class="w-7 h-7" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
              <path d="M21 10.5A8.38 8.38 0 0 1 12.11 21c-4.36 0-7.88-3.52-7.88-7.88A8.38 8.38 0 0 1 12.11 3c4.36 0 7.89 3.52 7.89 7.5Z"/>
              <circle cx="12" cy="11.5" r="3.5"/>
            </svg>
          </a>
          <button
            @click="shareLocation"
            class="w-14 h-14 flex items-center justify-center rounded-2xl border-2 border-blue-100 bg-blue-50 hover:bg-blue-200 transition text-blue-700 shadow-lg hover:scale-105 fairy-shadow"
            aria-label="Udostępnij"
          >
            <svg class="w-7 h-7" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
              <path d="M4 12v-2a4 4 0 1 1 8 0v2m0 0v2a4 4 0 1 0 8 0v-2M12 14v-4" />
            </svg>
          </button>
        </div>

        <!-- Alerty kopiowania -->
        <div
          v-if="showAlert"
          class="absolute left-1/2 bottom-5 -translate-x-1/2 px-5 py-2 bg-blue-600 text-white rounded-lg shadow font-medium animate-modal-pop z-30"
        >
          Link skopiowany do schowka! 🎉
        </div>
        <div
          v-if="copyError"
          class="absolute left-1/2 bottom-5 -translate-x-1/2 px-5 py-2 bg-red-600 text-white rounded-lg shadow font-medium animate-modal-pop z-30"
        >
          Nie udało się skopiować linku.<br>
          Skopiuj ręcznie: <span class="underline">{{ copyUrl }}</span>
        </div>
      </div>
    </div>
  </transition>
</template>

<script setup>
import { ref } from 'vue'
import kebabIcon from '@/assets/markers/kebab.png'
import pizzaIcon from '@/assets/markers/pizza.png'
import hamburgerIcon from '@/assets/markers/hamburger.png'
import restaurantIcon from '@/assets/markers/restaurant.png'
import karczmaIcon from '@/assets/markers/karczma.png'
import mexicoIcon from '@/assets/markers/mexico.png'
import sushiIcon from '@/assets/markers/sushi.png'
import chineseIcon from '@/assets/markers/chinese.png'
import fancy_restaurantIcon from '@/assets/markers/fancy_restaurant.png'
const props = defineProps({
  point: Object
})
const emit = defineEmits(['close'])
const showAlert = ref(false)
const copyError = ref(false)
const copyUrl = ref('')

function getCategoryIcon(category) {
  switch ((category || '').toLowerCase()) {
    case 'kebab': return kebabIcon
    case 'pizza': return pizzaIcon
    case 'hamburger': return hamburgerIcon
    case 'restauracja': return restaurantIcon
    case 'karczma': return karczmaIcon
    case 'meksykanskie': return mexicoIcon
    case 'sushi': return sushiIcon
    case 'chinol': return chineseIcon
    case 'wykwintna restauracja': return fancy_restaurantIcon
    default: return kebabIcon
  }
}

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
@import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@400;700&display=swap');

.font-fredoka {
  font-family: 'Fredoka', 'Comic Sans MS', cursive, sans-serif;
}
.fairy-modal {
  animation: modal-pop 0.35s cubic-bezier(.55,1.45,.52,1.09) both;
}
.fairy-modal-backdrop {
  animation: fadein-modal-bg 0.29s both;
}
@keyframes modal-pop {
  0% { opacity: 0; transform: scale(0.86) translateY(40px);}
  100% { opacity: 1; transform: scale(1) translateY(0);}
}
@keyframes fadein-modal-bg {
  0% { opacity: 0;}
  100% { opacity: 1;}
}
.fairy-pop {
  animation: fairy-pop-in 0.23s cubic-bezier(.56,1.62,.51,.98);
}
@keyframes fairy-pop-in {
  0% { opacity: 0; transform: scale(0.8);}
  100% { opacity: 1; transform: scale(1);}
}
.fairy-shadow {
  box-shadow: 0 4px 18px 0 rgba(155, 130, 255, 0.09);
}
.fairy-close {
  transition: box-shadow 0.19s, background 0.18s;
  box-shadow: 0 2px 16px 0 #fda4af40;
}
.fairy-close:hover {
  box-shadow: 0 3px 18px 0 #f8717144;
  background: #ef4444 !important;
}
.modal-fade-enter-active,
.modal-fade-leave-active {
  transition: opacity 0.28s;
}
.modal-fade-enter-from,
.modal-fade-leave-to {
  opacity: 0;
}
</style>
