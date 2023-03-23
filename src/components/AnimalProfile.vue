<script setup>
import { ref, defineProps } from "vue";

const props = defineProps([
  "commonName",
  "scientificName",
  "threats",
  "habitat",
  "countries",
  "status",
]);
const displayAdditional = ref(false);

function toggleAdditional(event) {
  displayAdditional.value = !displayAdditional.value;
}
</script>

<template>
  <div class="animal-box">
    <img
      src="../assets/demo-axolotl.jpg"
      alt="Logo"
      width="200"
      height="200"
      class="animal-image"
    />

    <div class="basic-information">
      <header class="animal-title">
        <span class="common-name">{{ commonName }}</span>
        <span class="scientific-name">({{ scientificName }})</span>
      </header>

      <div class="more-information">
        <div class="info-box threats">
          <h3>Threats</h3>
          <ul v-for="threat in threats">
            <li>{{ threat }}</li>
          </ul>
        </div>

        <div class="info-box habitat">
          <h3>Habitat</h3>
          <ul v-for="type in habitat">
            <li>{{ type }}</li>
          </ul>
        </div>

        <div class="info-box countries">
          <h3>Countries</h3>
          <ul v-for="country in countries">
            <li>{{ country }}</li>
          </ul>
        </div>
      </div>

      <p @click="toggleAdditional" class="additional-info">
        Additional Information
      </p>
    </div>

    <div class="status">{{ status }}</div>
    <div v-if="displayAdditional" class="additional">
      <h1>Hi additional info here</h1>
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
  grid-template-columns: 200px 5fr 1fr;
  grid-template-rows: 200px;
  column-gap: 10px;
  justify-content: center;
  align-content: center;
}

.basic-information {
  display: flex;
  flex-direction: column;
  justify-content: space-around;
}

.additional {
  text-align: center;
  grid-column: 1 / -1;
}

/* IMAGE */
.animal-image {
  margin-right: 10px;
}

/* ANIMAL TITLE */
.animal-title {
  font-size: 28px;
  color: #70c3ed;
  margin-top: 5px;
}

.common-name {
  font-weight: bold;
  margin-right: 10px;
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

hr {
  width: 100%;
}

/* STATUS */
.status {
  font-size: 20px;
  text-align: center;
  writing-mode: vertical-rl;
  word-spacing: 100vw;

  color: #fff;
  background-color: #e03531;
  /* background-color: #f0bd27;
  background-color: #51b364; */

  height: 200px;
  padding: 0 20px;
  margin-left: auto;
}
</style>
