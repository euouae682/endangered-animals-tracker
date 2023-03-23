<script setup>
import { ref, defineProps } from "vue";

const props = defineProps([
  "commonName",
  "scientificName",
  "threats",
  "habitat",
  "countries",
  "status",
  "additional",
]);
const displayAdditional = ref(false);
const status_colors = {
  "Least Concern\r": "green",
  "Vulnerable\r": "blue",
  "Near Threatened\r": "rgb(181, 175, 0)",
  "Threatened\r": "rgb(181, 91, 0)",
  "Endangered\r": "red",
  "Critically Endangered\r": "black",
  "Unknown\r": "gray",
};

function toggleAdditional(event) {
  displayAdditional.value = !displayAdditional.value;
}
</script>

<template>
  <div class="animal-box">
    <img
      :src="'../assets/' + commonName.substring(0, commonName.length - 2)"
      alt="Logo"
      width="200"
      height="200"
      class="animal-image"
    />

    <div class="basic-information">
      <div>
        <header class="animal-title">
          <p class="common-name">{{ commonName }}</p>
          <p class="scientific-name">{{ scientificName }}</p>
        </header>

        <div class="more-information">
          <div class="info-box threats">
            <h3>Habitats</h3>
            <p>{{ threats }}</p>
            <!-- <ul v-for="threat in threats">
            <li>{{ threat }}</li>
          </ul> -->
          </div>

          <div class="info-box habitat">
            <h3>Continents</h3>
            <p>{{ habitat }}</p>
            <!-- <ul v-for="type in habitat">
            <li>{{ type }}</li>
          </ul> -->
          </div>

          <div class="info-box countries">
            <h3>Countries</h3>
            <p>{{ countries }}</p>
            <!-- <ul v-for="country in countries">
            <li>{{ country }}</li>
          </ul> -->
          </div>
        </div>
      </div>

      <p @click="toggleAdditional" class="additional-info">
        Additional Information
      </p>
    </div>

    <div :style="'background-color: ' + status_colors[status]" class="status">
      {{ status }}
    </div>

    <div v-if="displayAdditional" class="additional">
      <h3>Summary</h3>
      <p>{{ additional }}</p>
    </div>
  </div>
</template>

<style scoped>
/* CONTAINER */
.animal-box {
  background-color: #eee;
  border: 2px solid #000;
  border-radius: 5px;

  display: grid;
  grid-template-columns: 200px 1fr auto;
  grid-template-rows: 200px;
  column-gap: 10px;
  row-gap: 15px;
}

.basic-information {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  margin-bottom: 5px;
}

.additional {
  text-align: center;
  justify-self: flex-end;
  grid-column: 2 / 3;
}

/* ANIMAL TITLE */
.animal-title {
  text-align: center;
  color: #70c3ed;
  margin-top: 5px;
}

.common-name {
  font-size: 24px;
  font-weight: bold;
}

.scientific-name {
  color: gray;
}

/* INFORMATION */
.more-information {
  font-size: 24px;
  display: flex;
  justify-content: space-between;
}

.info-box {
  flex: 1 1 0px;
  margin: 10px;
}

h3 {
  font-size: 20px;
  text-align: center;
  color: #70c3ed;
}

li {
  font-size: 16px;
  font-style: italic;
  text-align: center;
  list-style-type: none;

  margin-bottom: 5px;
}

.additional-info {
  text-align: center;
  color: #70c3ed;
}

.additional-info:hover {
  color: #2aa7e6;
  cursor: pointer;
}

/* STATUS */
.status {
  font-size: 18px;
  text-align: center;
  writing-mode: vertical-rl;

  color: #fff;
  background-color: #e03531;
  padding: 0 20px;
}

p {
  font-size: 16px;
  text-align: center;
}
</style>
