<script setup></script>

<template>
  <div class="header">
    <img
      src="../assets/logo-placeholder-image.png"
      alt="Logo"
      width="50"
      height="50"
    />

    <span>Endangered Animals Tracker</span>

    <nav>
      <a href="#">Settings</a>
      <a href="#">About</a>
    </nav>
  </div>
</template>

<style scoped>
/* CONTAINER */
.header {
  border-top: 10px solid #70c3ed;
  background-color: rgba(112, 195, 237, 0.5);

  display: flex;
  align-items: center;
}

/* LOGO */
img {
  margin: 2px 10px;
}

/* TITLE */
span {
  font-size: 26px;
  font-weight: bold;
}

/* NAVIGATION */
nav {
  order: 0;
  margin-left: auto;
}

a:any-link {
  font-size: 20px;
  text-decoration: none;

  color: #000;

  /* height: 100%; */
  padding: 16px 25px;
}

a:hover {
  background-color: #70c3ed;
}
</style>
