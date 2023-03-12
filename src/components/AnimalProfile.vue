<script setup></script>

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
        <span class="common-name">Axolotl</span>
        <span class="scientific-name">(Ambystoma mexicanum)</span>
      </header>

      <div class="more-information">
        <div class="info-box threats">
          <h3>Threats</h3>
          <ul>
            <li>Residential & commercial development</li>
            <li>Pollution</li>
          </ul>
        </div>

        <div class="info-box habitat">
          <h3>Habitat</h3>
          <ul>
            <li>Wetlands</li>
            <li>Artificial/Aquatic & Marine</li>
          </ul>
        </div>

        <div class="info-box countries">
          <h3>Countries</h3>
          <ul>
            <li>Mexico</li>
          </ul>
        </div>
      </div>

      <p class="additional-info">Additional Information</p>
    </div>

    <div class="status">Critically Endangered</div>
  </div>
</template>

<style scoped>
/* CONTAINER */
.animal-box {
  background-color: #eee;
  border: 2px solid #000;
  border-radius: 5px;

  display: flex;
  justify-content: center;
}

.basic-information {
  display: flex;
  flex-direction: column;
  flex: 1 0 0;
  gap: 20px;
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
