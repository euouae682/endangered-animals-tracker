<script setup>
import AnimalProfile from "./AnimalProfile.vue";
</script>

<template>
  <div class="article">
    <AnimalProfile class="animal-profile" />
    <AnimalProfile class="animal-profile" />
    <AnimalProfile class="animal-profile" />
  </div>
</template>

<style scoped>
.article {
  background-color: hsla(120, 100%, 50%, 0.5);

  display: flex;
  align-items: center;
  flex-direction: column;

  padding-top: 20px;
}

.animal-profile {
  width: 95%;
  margin-bottom: 20px;
}
</style>
