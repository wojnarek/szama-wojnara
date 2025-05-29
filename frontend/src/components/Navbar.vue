<template>
  <nav class="fairy-navbar sticky top-0 z-50 w-full">
    <div class="container flex items-center justify-between py-2 px-3">
      <div class="fairy-search-wrapper relative w-full max-w-xl flex justify-center items-center mx-auto animate-navbar-pop">
        <input
          type="text"
          v-model="search"
          class="fairy-search-input w-full h-12 pl-12 pr-7 rounded-full bg-white text-lg text-pink-900 border-2 border-pink-200 shadow focus:ring-2 focus:ring-yellow-200 focus:border-yellow-300 outline-none transition-all duration-300 fairy-shadow"
          placeholder="🔍 Wyszukaj szamke..."
        />
      </div>

      <span class="hidden sm:inline-block min-w-[80px]"></span>
    </div>
  </nav>
</template>

<script setup>
import { ref } from 'vue'
const search = ref('')
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@400;700&display=swap');

.fairy-navbar {
  background: linear-gradient(87deg, #ffe6f6 0%, #fffde2 55%, #e3f1ff 100%);
  box-shadow: 0 3px 18px 0 rgba(255, 189, 245, 0.09);
  border-bottom: 2.4px solid #fbcfe8;
  font-family: 'Fredoka', 'Comic Sans MS', cursive, sans-serif;
  animation: navbar-fadein 0.38s cubic-bezier(.56,1.62,.51,.98);
}
@keyframes navbar-fadein {
  0% { opacity: 0; transform: translateY(-16px);}
  100% { opacity: 1; transform: translateY(0);}
}

.fairy-logo {
  color: #e11d48;
  letter-spacing: 0.02em;
  text-shadow: 0 1px 6px #fff2;
  margin-right: 10px;
}

.fairy-search-wrapper {
  width: 100%;
  max-width: 440px;
  position: relative;
}

.fairy-search-input {
  background: rgba(255,255,255,0.98);
  font-family: 'Fredoka', 'Comic Sans MS', cursive, sans-serif;
  box-shadow: 0 2px 18px 0 rgba(251, 207, 232, 0.13);
  border-width: 2.4px;
  transition: box-shadow 0.22s, border 0.22s, transform 0.19s;
}

.fairy-search-input:focus {
  border-color: #fde68a;
  box-shadow: 0 2px 20px 0 #fef9c33a;
  transform: scale(1.04);
}

.fairy-bubble {
  background: linear-gradient(110deg, #fde68a 0%, #fbcfe8 100%);
  border-radius: 99px;
  padding: 3px 7px 3px 7px;
  box-shadow: 0 1px 7px #fbcfe899, 0 0px 5px #fff3;
  display: flex;
  align-items: center;
  border: 1.5px solid #fbcfe8;
}

.animate-navbar-pop {
  animation: navbar-pop-in 0.39s cubic-bezier(.56,1.62,.51,.98);
}
@keyframes navbar-pop-in {
  0% { opacity: 0; transform: scale(0.93);}
  100% { opacity: 1; transform: scale(1);}
}

.animate-sparkle {
  animation: sparkle-pop 1.6s infinite alternate;
}
@keyframes sparkle-pop {
  0% { opacity: 0.6; transform: scale(1) rotate(-10deg);}
  100% { opacity: 1; transform: scale(1.13) rotate(12deg);}
}
</style>
