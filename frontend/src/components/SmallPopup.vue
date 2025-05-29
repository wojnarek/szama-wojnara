<template>
  <div class="fairy-popup bg-gradient-to-br from-yellow-50 via-pink-50 to-blue-100 rounded-3xl shadow-xl px-5 py-6 w-72 flex flex-col items-center border-2 border-pink-100 animate-popup-fade fairy-shadow fairy-border">
    <!-- Ikonka kategorii -->
    <img
      :src="getCategoryIcon(point.main_category)"
      alt="ikona kategorii"
      class="w-14 h-14 mb-2 drop-shadow-md fairy-pop"
      style="background:rgba(255,255,255,0.75); border-radius: 100%;"
    />
    <!-- Point name -->
    <div class="text-xl font-extrabold text-pink-700 text-center mb-1 font-fredoka tracking-wide flex items-center gap-2 drop-shadow">
      {{ point.name }}
    </div>
    <!-- Main category -->
    <span class="inline-flex items-center gap-1 px-4 py-1 mb-2 rounded-full bg-gradient-to-r from-pink-200 via-yellow-100 to-blue-100 text-pink-800 font-bold text-xs uppercase tracking-wide shadow fairy-pop">
      <span>🏷️</span>{{ point.main_category }}
    </span>
    <!-- Subcategories -->
    <div v-if="point.subcategories?.length" class="flex flex-wrap justify-center gap-1 mb-2 min-h-[24px]">
      <transition-group name="pop" tag="div" class="flex flex-wrap gap-1">
        <span
          v-for="(cat, i) in point.subcategories"
          :key="cat"
          class="bg-blue-50 text-blue-700 px-2 py-1 rounded-full font-medium text-xs shadow fairy-pop"
        >🔖 {{ cat }}</span>
      </transition-group>
    </div>
    <div v-else class="text-gray-400 italic text-xs mb-2">Brak podkategorii</div>
    <!-- More button -->
    <button
      @click="handleMoreClick"
      :disabled="loading"
      class="w-11 h-11 flex items-center justify-center rounded-full bg-gradient-to-br from-blue-300 via-pink-300 to-yellow-200 hover:scale-110 transition-all text-white shadow-lg mt-2 fairy-glow relative"
      title="Więcej informacji"
    >
      <svg v-if="!loading" class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="2.2" viewBox="0 0 24 24">
        <path d="M9 18l6-6-6-6"/>
      </svg>
      <svg v-else class="w-6 h-6 animate-spin" viewBox="0 0 24 24">
        <circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4" fill="none"/>
      </svg>
      <span class="absolute -top-4 left-1/2 -translate-x-1/2 text-[0.65rem] text-yellow-500 animate-bounce select-none">info!</span>
    </button>
    <div v-if="error" class="text-xs text-red-500 mt-2 font-bold">{{ error }}</div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
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

const props = defineProps({
  point: Object
})

const loading = ref(false)
const error = ref(null)

function getCategoryIcon(category) {
  switch ((category || '')) {
    case 'Kebab': return kebabIcon
    case 'Pizza': return pizzaIcon
    case 'Hamburger': return hamburgerIcon
    case 'Restauracja': return restaurantIcon
    case 'Karczma': return karczmaIcon
    case 'Meksykanskie': return mexicoIcon
    case 'Sushi': return sushiIcon
    case 'Chinol': return chineseIcon
    case 'Wykwintna restauracja': return fancy_restaurantIcon
    default: return kebabIcon
  }
}

async function handleMoreClick() {
  loading.value = true
  error.value = null
  try {
    const res = await axios.get(import.meta.env.VITE_API_URL + '/points/' + props.point.id)
    window.dispatchEvent(new CustomEvent('show-point-modal', { detail: res.data }))
  } catch (e) {
    error.value = "Nie udało się pobrać szczegółów."
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@400;700&display=swap');

.fairy-popup {
  font-family: 'Fredoka', 'Comic Sans MS', cursive, sans-serif;
  animation: popup-fade 0.42s cubic-bezier(.55,1.45,.52,1.09) both;
}
@keyframes popup-fade {
  0% { opacity: 0; transform: scale(0.88) translateY(20px);}
  100% { opacity: 1; transform: scale(1) translateY(0);}
}
.fairy-shadow {
  box-shadow: 0 4px 18px 0 rgba(155, 130, 255, 0.09);
}
.fairy-border {
  border-width: 2.4px;
}
.fairy-glow {
  box-shadow: 0 0 0 3px #fef08a50, 0 6px 24px 0 #dbeafe44;
}

.fairy-pop {
  animation: fairy-pop-in 0.19s cubic-bezier(.56,1.62,.51,.98);
}
@keyframes fairy-pop-in {
  0% { opacity: 0; transform: scale(0.77);}
  100% { opacity: 1; transform: scale(1);}
}

/* Przejścia dla tagów */
.pop-enter-active, .pop-leave-active {
  transition: all 0.19s cubic-bezier(.56,1.62,.51,.98);
}
.pop-enter-from, .pop-leave-to {
  opacity: 0;
  transform: scale(0.85);
}
</style>
