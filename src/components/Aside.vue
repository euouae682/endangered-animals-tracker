<script setup>
import { ref } from "vue";
const objectItems = ["Animal", "Plant", "Fungi"];
const regions = [
  "Africa",
  "Antarctica",
  "Asia",
  "Europe",
  "North America",
  "Oceania",
  "South America",
];

const display_taxonomy = ref(true);
const display_region = ref(true);

function toggle_taxonomy(event) {
  display_taxonomy.value = !display_taxonomy.value;
}

function toggle_region(event) {
  display_region.value = !display_region.value;
}
</script>

<template>
  <div class="container">
    <div class="search">
      <img src="../assets/search-icon.png" alt="Logo" width="20" height="20" />
      <input type="text" class="search-bar" placeholder="Search..." />
    </div>

    <div class="line"></div>

    <button @click="toggle_taxonomy" type="button" class="collapsible-button">
      Taxonomy
    </button>
    <div v-if="display_taxonomy" class="collapsible" id="collapse-taxonomy">
      <form>
        <div v-for="item in objectItems" class="checkbox-list">
          <input
            type="checkbox"
            :id="'taxonomy-' + item.toLowerCase()"
            :name="'taxonomy-' + item.toLowerCase()"
          />
          <label :for="'taxonomy-' + item.toLowerCase()"> {{ item }} </label
          ><br />
        </div>
      </form>
    </div>

    <div class="line"></div>

    <button @click="toggle_region" type="button" class="collapsible-button">
      Region
    </button>
    <div v-if="display_region" class="collapsible" id="collapse-region">
      <form>
        <div v-for="region in regions" class="checkbox-list">
          <input
            type="checkbox"
            :id="'region-' + region.toLowerCase()"
            :name="'region-' + region.toLowerCase()"
          />
          <label :for="'region-' + region.toLowerCase()"> {{ region }} </label>
        </div>
      </form>
    </div>

    <div class="line"></div>

    <button type="button" class="collapsible-button">Habitat</button>
  </div>
</template>

<style scoped>
/* CONTAINER */
.container {
  text-align: center;
  background-color: #ddd;

  display: flex;
  flex-direction: column;
  align-items: center;
  padding-top: 20px;
}

/* COLLAPSIBLES */
.collapsible-button {
  font-size: 18px;

  color: #fff;
  background-color: #70c3ed;
  border: 3px solid #78787880;

  align-self: stretch;
  margin: 0 3%;
}

.collapsible-button:hover {
  color: #000;
  background-color: #ddd;
}

.collapsible {
  text-align: left;
  align-self: flex-start;

  margin-left: 10%;
}

/* CHECKBOXES */
.checkbox-list {
  display: flex;
  align-items: center;
  margin-top: 5px;
}

input[type="checkbox"] {
  background-color: #eee;

  margin-right: 5px;
  height: 15px;
  width: 15px;
}

/* LINE */
.line {
  border-bottom: 5px solid #78787880;
  border-radius: 20px;

  margin: 20px auto 0;
  width: 95%;
}

/* SEARCH BAR */
.search {
  display: flex;
}

.search-bar {
  font-size: 20px;

  background-color: #ddd;
  border: none;
  border-bottom: 2px solid #333;

  margin-left: 5px;
}
</style>
