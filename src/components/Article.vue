<script setup>
import AnimalProfile from "./AnimalProfile.vue";
import { ref, defineProps } from 'vue'

const props = defineProps(['species'])
</script>

<template>
  <div class="article">
    <AnimalProfile v-for="animal in species"
      class="animal-profile"
      :commonName="animal[0]"
      :scientificName="animal[1]"
      :threats="animal[3]"
      :habitat="animal[4]"
      :countries="animal[5]"
      :status="animal[2]"
      :additional="animal[6]"
    />
    <p>{{ species }}</p>
  </div>
</template>

<style scoped>
.article {
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
