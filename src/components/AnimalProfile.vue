<script setup></script>

<template>
  <div class="container">
    <header class="title">
      <img
        src="../assets/logo-placeholder-image.png"
        alt="Logo"
        width="50"
        height="50"
        class="animal-image"
      />

      <span class="common-name">Animal Name</span>
      <span class="scientific-name">(Scientific Name)</span>
    </header>

    <article>
      <p>Status</p>
      <p>Stability</p>
    </article>
  </div>
</template>

<style scoped>
/* CONTAINER */
.container {
  border: 2px solid #000;
  border-radius: 5px;
}

/* TITLE */
.title {
  display: flex;
  align-items: center;
}

.animal-image {
  margin-right: 10px;
}

.common-name {
  font-weight: bold;
  margin-right: 10px;
}

.scientific-name {
  color: #777;
}
</style>
