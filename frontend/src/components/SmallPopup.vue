<template>
  <div>
    <strong>{{ point.name }}</strong><br/>
    <span>Kategoria: {{ point.main_category }}</span><br/>
    <span>Podkategorie: {{ point.subcategories?.join(', ') }}</span><br/>
    <button @click="handleMoreClick" class="mt-1 px-3 py-1 rounded bg-blue-600 text-white">Więcej</button>
  </div>
</template>

<script setup>
const props = defineProps({
  point: Object
})
const emit = defineEmits(['more'])

function handleMoreClick() {
  emit('more', props.point)
}
</script>
