<script setup>
import AnimalProfile from "./AnimalProfile.vue";
</script>

<template>
  <div class="article">
    <AnimalProfile
      class="animal-profile"
      commonName="Axolotl"
      scientificName="Ambystroma mexicanum"
      :threats="['Residential and commercial development', 'Pollution']"
      :habitat="['Wetlands', 'Artificial/Aquatic and Marine']"
      :countries="['Mexico']"
      status="Critically Endangered"
    />

    <AnimalProfile
      class="animal-profile"
      commonName="Axolotl"
      scientificName="Ambystroma mexicanum"
      :threats="['Residential and commercial development', 'Pollution']"
      :habitat="['Wetlands', 'Artificial/Aquatic and Marine']"
      :countries="['Mexico']"
      status="Critically Endangered"
    />

    <AnimalProfile
      class="animal-profile"
      commonName="Axolotl"
      scientificName="Ambystroma mexicanum"
      :threats="['Residential and commercial development', 'Pollution']"
      :habitat="['Wetlands', 'Artificial/Aquatic and Marine']"
      :countries="['Mexico']"
      status="Critically Endangered"
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
