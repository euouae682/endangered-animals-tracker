<script setup>
import AnimalProfile from "./AnimalProfile.vue";
import { ref, defineProps } from 'vue'

const props = defineProps(['species'])

const generateRandom = () => {
  return Math.floor(Math.random() * 21);
}

var nums = [generateRandom()]
var num2 = generateRandom()
while (num2 == nums[0]) {
  num2 = generateRandom()
}
nums.push(num2);
var num3 = generateRandom()
while (num3 == nums[0] || num3 == nums[1]) {
  num3 = generateRandom()
}
nums.push(num3)
</script>

<template>
  <div class="article">
    <AnimalProfile v-for="animal in [species[nums[0]], species[nums[1]], species[nums[2]]]"
      class="animal-profile"
      :commonName="animal[0]"
      :scientificName="animal[1]"
      :threats="animal[3]"
      :habitat="animal[4]"
      :countries="animal[5]"
      :status="animal[2]"
      :additional="animal[6]"
    />
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
