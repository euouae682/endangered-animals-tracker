<script setup></script>

<template>
  <div class="main-header">
    <div class="header">
      <img
        src="../assets/logo-paw-blue.png"
        alt="Logo"
        width="50"
        height="50"
        class="image"
      />

      <span class="title">Endangered Animals Tracker</span>
    </div>

    <nav class="nav-bar">
      <a href="#" class="nav-link">Settings</a>
      <a href="#" class="nav-link">About</a>
    </nav>
  </div>
</template>

<style scoped>
/* CONTAINER */
.main-header {
  border-top: 10px solid #70c3ed;
  background-color: #eee;

  display: flex;
  align-items: center;
  justify-content: space-between;
}

/* HEADER */
.header {
  display: flex;
  align-items: center;
  gap: 10px;
}

.image {
  margin-left: 5px;
}

.title {
  font-size: 26px;
  font-weight: bold;
  color: #70c3ed;
}

/* NAVIGATION */
.nav-bar {
  display: flex;
  align-items: center;
  /* align-self: stretch; */
}

.nav-link:any-link {
  font-size: 20px;
  text-decoration: none;
  color: #000;

  padding: 16px 25px;
}

.nav-link:hover {
  color: #fff;
  background-color: #70c3ed;
}
</style>
