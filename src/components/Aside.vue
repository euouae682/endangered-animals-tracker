<script setup></script>

<template>
  <div class="container">
    <input type="text" class="search-bar" placeholder="Search..." />

    <div class="line"></div>

    <button type="button" class="collapsible-button">Taxonomy</button>
    <div class="collapsible">
      <form>
        <input type="checkbox" id="taxonomy-animal" name="taxonomy-animal" />
        <label for="taxonomy-animal">Animal</label><br />

        <input type="checkbox" id="taxonomy-plant" name="taxonomy-plant" />
        <label for="taxonomy-plant">Plant</label><br />

        <input type="checkbox" id="taxonomy-fungi" name="taxonomy-fungi" />
        <label for="taxonomy-fungi">Fungi</label><br />
      </form>
    </div>

    <div class="line"></div>

    <button type="button" class="collapsible-button">Region</button>
    <div class="collapsible">
      <form>
        <input type="checkbox" id="region-africa" name="region-africa" />
        <label for="region-africa">Africa</label><br />

        <input
          type="checkbox"
          id="region-antarctica"
          name="region-antarctica"
        />
        <label for="region-antarctica">Antarctica</label><br />

        <input type="checkbox" id="region-asia" name="region-asia" />
        <label for="region-asia">Asia</label><br />

        <input type="checkbox" id="region-europe" name="region-europe" />
        <label for="region-europe">Europe</label><br />

        <input
          type="checkbox"
          id="region-north-america"
          name="region-north-america"
        />
        <label for="region-north-america">North America</label><br />

        <input type="checkbox" id="region-oceania" name="region-oceania" />
        <label for="region-oceania">Oceania</label><br />

        <input
          type="checkbox"
          id="region-south-america"
          name="region-south-america"
        />
        <label for="region-south-america">South America</label><br />
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
  background-color: rgba(255, 0, 0, 0.273);

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
