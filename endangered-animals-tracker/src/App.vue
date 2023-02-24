<script setup>
import Header from "./components/Header.vue";
</script>

<template>
  <body>
    <header class="main-header">
      <Header />
    </header>
  </body>
</template>

<style scoped>
* {
  margin: 0;
  padding: 0;
}

/* Page Sections */
body {
  font-family: sans-serif;

  color: #444;
  border-top: 10px solid #70c3ed;
}

.main-header {
  background-color: rgba(112, 195, 237, 0.5);
}
</style>
