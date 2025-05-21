<template>
  <div class="app-container">
    <Navbar />
    <Map />
  </div>
</template>

<script>
import Navbar from './components/Navbar.vue';
import Map from './components/Map.vue';

export default {
  components: { Navbar, Map },
};
</script>

