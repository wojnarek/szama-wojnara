<template>
  <form
    @submit.prevent="handleSubmit"
    class="max-w-md mx-auto px-8 py-8 bg-gradient-to-br from-green-100 via-blue-100 to-purple-100 shadow-2xl rounded-[2.5rem] flex flex-col gap-6 animate-fadein fairy-form"




    style="font-family: 'Fredoka', 'Comic Sans MS', cursive, sans-serif;"
  >
    <h2 class="text-3xl font-extrabold text-pink-600 text-center mb-1 flex items-center justify-center gap-2 drop-shadow-lg">
      <span>✨</span> Dodaj nową szamke <span>✨</span>
    </h2>

    <div>
      <label class="font-semibold block mb-1 text-blue-700 flex items-center gap-1">🏷️ Nazwa punktu</label>
      <input
        v-model="name"
        type="text"
        class="w-full border-2 border-pink-200 focus:border-pink-400 focus:ring-2 focus:ring-pink-200 bg-white rounded-2xl px-4 py-2 text-lg transition-all duration-200 fairy-shadow"
        placeholder="Jak nazywa się miejsce?"
        maxlength="30"
        :pattern="namePattern"
        required
      />
      <transition name="fade">
        <span v-if="name && !nameValid" class="text-red-500 text-xs mt-1">❗ Tylko litery, cyfry, myślniki, max 30 znaków</span>
      </transition>
    </div>

    <div class="relative">
  <label class="font-semibold block mb-1 text-yellow-700 flex items-center gap-1">🍕 Kategoria</label>
  <button
    type="button"
    class="w-full border-2 border-yellow-200 focus:border-yellow-400 focus:ring-2 focus:ring-yellow-200 bg-white rounded-2xl px-4 py-2 text-lg fairy-shadow flex items-center gap-2"
    @click="showCatDropdown = !showCatDropdown"
  >
    <img
      v-if="category"
      :src="getCategoryIcon(category)"
      alt="ikona kategorii"
      class="w-7 h-7 rounded-full drop-shadow-md transition-transform duration-300"
      :class="{'scale-110': showCatDropdown}"
    />
    <span>{{ category || 'Wybierz kategorię...' }}</span>
    <svg class="w-4 h-4 ml-auto" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M19 9l-7 7-7-7"/></svg>
  </button>
  <transition name="cat-dropdown-fade">
    <div
      v-if="showCatDropdown"
      class="absolute left-0 z-10 mt-2 w-full bg-white border-2 border-yellow-100 rounded-2xl shadow-xl fairy-shadow"
    >
      <ul class="flex flex-col gap-1 py-2">
        <li
          v-for="cat in categories"
          :key="cat"
          @click="selectCategory(cat)"
          class="flex items-center gap-3 px-4 py-2 cursor-pointer hover:bg-yellow-50 hover:scale-105 transition-all duration-150 rounded-xl"
        >
          <img :src="getCategoryIcon(cat)" alt="ikona" class="w-7 h-7 rounded-full drop-shadow" />
          <span class="font-bold text-lg text-yellow-800">{{ cat }}</span>
        </li>
      </ul>
    </div>
  </transition>
</div>

    <div>
      <label class="font-semibold block mb-1 text-blue-700 flex items-center gap-1">🏷️ Tagi <span class="text-sm">(po wpisaniu wciśnij enter)</span></label>
      <div class="flex flex-wrap gap-2 mb-2 min-h-[30px]">
        <transition-group name="pop" tag="div" class="flex flex-wrap gap-2">
          <span
            v-for="(tag, i) in subcategories"
            :key="tag"
            class="bg-gradient-to-r from-blue-200 via-pink-100 to-yellow-100 text-blue-700 px-3 py-1 rounded-full text-base flex items-center gap-1 shadow fairy-pop"
            style="animation-delay: calc(50ms * var(--i));"
            :style="{ '--i': i }"
          >
            <span>🔖</span>{{ tag }}
            <button type="button" class="ml-1 text-pink-700 hover:text-red-500 transition" @click="removeSubcategory(i)">×</button>
          </span>
        </transition-group>
      </div>
      <input
        v-model="subcategoryInput"
        @keydown.enter.prevent="addSubcategory"
        type="text"
        class="w-full border-2 border-blue-200 focus:border-blue-400 focus:ring-2 focus:ring-blue-200 bg-white rounded-2xl px-4 py-2 text-lg fairy-shadow transition-all duration-200"
        placeholder="Opisz szamke kilkoma słowami (max 8.)"
        :disabled="subcategories.length >= 8"
        :maxlength="20"
      />
      <transition name="fade">
        <span v-if="subcategories.length >= 8" class="text-blue-700 text-xs mt-1">🌟 Limit subkategorii osiągnięty!</span>
      </transition>
    </div>

    <div>
      <label class="font-semibold block mb-1 text-green-700 flex items-center gap-1">📝 Opis</label>
      <textarea
        v-model="description"
        class="w-full border-2 border-green-200 focus:border-green-400 focus:ring-2 focus:ring-green-200 bg-white rounded-2xl px-4 py-2 text-lg resize-none fairy-shadow transition-all duration-200"
        maxlength="200"
        rows="3"
        placeholder="Opisz punkt (max 200 znaków)"
        required
      ></textarea>
      <div class="text-xs text-gray-400 flex items-center gap-1 mt-1">
        <span>✏️</span>{{ description.length }}/200
      </div>
    </div>

    <input v-model="latitude" type="hidden" readonly />
    <input v-model="longitude" type="hidden" readonly />

    <div>
      <label class="font-semibold block mb-1 text-purple-700 flex items-center gap-1">🔑 Kod autoryzacyjny</label>
      <input
        v-model="code"
        type="text"
        class="w-full border-2 border-purple-200 focus:border-purple-400 focus:ring-2 focus:ring-purple-200 bg-white rounded-2xl px-4 py-2 text-lg fairy-shadow transition-all duration-200"
        maxlength="40"
        required
        placeholder="Wpisz kod zaufania ✨"
      />
    </div>

<div class="flex gap-3 justify-center mt-4">
  <button
    type="button"
    class="px-5 py-2 rounded-2xl bg-gray-200 hover:bg-pink-200 text-gray-700 font-semibold shadow transition-all fairy-shadow"
    @click="$emit('close')"
  >❌ Anuluj</button>
  <button
    @click="handleSubmit()"
    type="submit"
    class="py-2 px-8 rounded-xl bg-gradient-to-r from-lime-300 via-green-200 to-emerald-200 text-green-800 font-extrabold text-lg shadow-xl hover:scale-110 hover:shadow-green-300 transition-all duration-200 fairy-shadow flex items-center gap-2"
    :disabled="!formValid"
  >⬆️<span>Dodaj punkt</span>⬆️</button>
</div>


  </form>
</template>

<script setup>
import { ref, computed, watch } from 'vue'
const emit = defineEmits(['close', 'submit'])
const props = defineProps({
  latitude: Number,
  longitude: Number,
})

import kebabIcon from '@/assets/markers/kebab.png'
import pizzaIcon from '@/assets/markers/pizza.png'
import hamburgerIcon from '@/assets/markers/hamburger.png'
import restaurantIcon from '@/assets/markers/restaurant.png'
import karczmaIcon from '@/assets/markers/karczma.png'
import mexicoIcon from '@/assets/markers/mexico.png'
import sushiIcon from '@/assets/markers/sushi.png'
import chineseIcon from '@/assets/markers/chinese.png'
import fancy_restaurantIcon from '@/assets/markers/fancy_restaurant.png'

const name = ref('')
const namePattern = '^[a-zA-Z0-9ąćęłńóśźżĄĆĘŁŃÓŚŹŻ\\- ]{1,30}$'
const nameValid = computed(() => new RegExp(namePattern).test(name.value))

const category = ref('')
const categories = [
  'Kebab', 'Pizza', 'Hamburger', 'Restauracja',
  'Karczma', 'Meksykanskie', 'Sushi', 'Chinol', 'Wykwintna restauracja'
]
function getCategoryIcon(category) {
  switch (category) {
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

const showCatDropdown = ref(false)
function selectCategory(cat) {
  category.value = cat
  showCatDropdown.value = false
}

const subcategories = ref([])
const subcategoryInput = ref('')

function addSubcategory() {
  const value = subcategoryInput.value.trim()
  if (
    value &&
    subcategories.value.length < 8 &&
    /^[a-zA-Z0-9ąćęłńóśźżĄĆĘŁŃÓŚŹŻ\- ]{1,20}$/.test(value) &&
    !subcategories.value.includes(value)
  ) {
    subcategories.value.push(value)
    subcategoryInput.value = ''
  }
}
function removeSubcategory(i) {
  subcategories.value.splice(i, 1)
}

const description = ref('')
const code = ref('')

const latitude = ref(props.latitude)
const longitude = ref(props.longitude)
watch(() => props.latitude, (val) => { latitude.value = val })
watch(() => props.longitude, (val) => { longitude.value = val })

const formValid = computed(() =>
  nameValid.value &&
  category.value &&
  description.value.length <= 200 &&
  subcategories.value.length <= 8 &&
  latitude.value && longitude.value &&
  code.value
)

function handleSubmit() {
  if (!formValid.value) return
  const payload = {
    name: name.value,
    category: category.value,
    subcategories: subcategories.value,
    description: description.value,
    latitude: latitude.value,
    longitude: longitude.value,
    code: code.value
  }
  alert('Dane do wysłania: ' + JSON.stringify(payload, null, 2))
  // emit('submit', payload) // użyj w produkcji
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@400;700&display=swap');

.cat-dropdown-fade-enter-active, .cat-dropdown-fade-leave-active {
  transition: opacity 0.24s cubic-bezier(.56,1.62,.51,.98), transform 0.25s cubic-bezier(.56,1.62,.51,.98);
}
.cat-dropdown-fade-enter-from, .cat-dropdown-fade-leave-to {
  opacity: 0;
  transform: translateY(-10px) scale(0.98);
}

.fairy-form {
  /* animacja na wejście */
  animation: fairy-form-pop 0.4s cubic-bezier(.56,1.62,.51,.98);
  font-family: 'Fredoka', 'Comic Sans MS', cursive, sans-serif;
}
@keyframes fairy-form-pop {
  0% { opacity: 0; transform: scale(0.92) translateY(48px);}
  100% { opacity: 1; transform: scale(1) translateY(0);}
}
.animate-fadein {
  animation: fadein 0.5s both;
}
@keyframes fadein {
  0% { opacity: 0;}
  100% { opacity: 1;}
}
.fairy-shadow {
  box-shadow: 0 3px 18px 0 rgba(175, 163, 255, 0.11);
}

.fairy-pop {
  animation: fairy-pop-in 0.25s cubic-bezier(.56,1.62,.51,.98);
}
@keyframes fairy-pop-in {
  0% { opacity: 0; transform: scale(0.82);}
  100% { opacity: 1; transform: scale(1);}
}

/* Animacje i przejścia */
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.25s;
}
.fade-enter-from, .fade-leave-to {
  opacity: 0;
}
.pop-enter-active, .pop-leave-active {
  transition: all 0.2s cubic-bezier(.56,1.62,.51,.98);
}
.pop-enter-from, .pop-leave-to {
  opacity: 0;
  transform: scale(0.85);
}
</style>
