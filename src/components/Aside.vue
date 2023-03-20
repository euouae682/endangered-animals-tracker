<script setup>
import { ref } from 'vue'
const objectItems = [ "Animal", "Plant", "Fungi" ]
const regions = ["Africa", "Antarctica", "Asia", "Europe", "North America", "Oceania", "South America"]

const displayTaxonomy = ref(true)
const displayRegion = ref(true)

function toggleTaxonomy(event) {
  displayTaxonomy.value = !displayTaxonomy.value
}

function toggleRegion(event) {
  displayRegion.value = !displayRegion.value
}
</script>

<template>
  <div class="container">
    <input type="text" class="search-bar" placeholder="Search..." />

    <div class="line"></div>

    <button @click="toggleTaxonomy" type="button" class="collapsible-button">Taxonomy</button>
    <div v-if="displayTaxonomy" class="collapsible" id="collapse-taxonomy">
      <form>
        <div v-for="item in objectItems">
          <input type="checkbox" :id="'taxonomy-' + item.toLowerCase()" :name="'taxonomy-' + item.toLowerCase()">
          <label :for="'taxonomy-' + item.toLowerCase()"> {{ item }} </label><br>     
        </div>
      </form>
    </div>

    <div class="line"></div>

    <button @click="toggleRegion" type="button" class="collapsible-button">Region</button>
    <div v-if="displayRegion" class="collapsible" id="collapse-region">
      <form>
        <div v-for="region in regions">
          <input type="checkbox" :id="'region-' + region.toLowerCase()" :name="'region-' + region.toLowerCase()">
          <label :for="'region-' + region.toLowerCase()"> {{ region }} </label>
        </div>
      </form>
    </div>

    <div class="line"></div>

    <button type="button" class="collapsible-button">Habitat</button>

    <div class="line"></div>

    <p>Advanced Search</p>
  </div>
</template>

<style scoped>
/* CONTAINER */
.container {
  text-align: center;
  background-color: #ddd;
  padding: 20px 0;
}

/* COLLAPSIBLES */
.collapsible-button {
  width: 95%;
}

.collapsible {
  text-align: left;
  margin-left: 10%;
}

/* LINE */
.line {
  border-bottom: 5px solid hsla(0, 0%, 47%, 0.5);
  border-radius: 20px;

  margin: 20px auto 0;
  width: 95%;
}

/* SEARCH BAR */
.search-bar {
  font-size: 20px;

  border: none;
}
</style>
