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
      <a href="#settings" class="nav-link">Settings</a>
      <a href="#about" class="nav-link">About</a>
    </nav>

    <div id="about" class="modalDialog">
      <div class="dialog-box">
        <a href="#close" title="Close" class="close">X</a>

        <h2 class="dialog-header">About</h2>

        <div class="mission-statement">
          <h3 class="dialog-subheader">Mission</h3>
          <p>
            Our mission is to raise awareness regarding endangered animals.
            Habitat loss has endangered many species. Public awareness of the
            issue has the opportunity to incentivize the use of more sustainable
            practices. The endangerment of species is a highly relevant, yet
            underexplored, issue to the general public. Animals such as the
            monarch butterfly are near the edge of extinction. However, history
            proves that animals can be brought back from the brink. Bison,
            previously endangered due to industrial-scale hunting, have been
            protected due to human intervention. Some of the largest bison herds
            now live as a stable population in areas such as Yellowstone and the
            Black Hills of South Dakota. However, unlike the bison, many species
            have been brought to extinction, often due to human activity. Many
            endangered species could be saved, should the general public be more
            aware of endangerment and the threats, often human-made, that
            animals face today.
          </p>
        </div>

        <div>
          <h3 class="dialog-subheader">Developers</h3>
          <ul class="dialog-list">
            <li class="dialog-list-item">Jason Zhao (2050058)</li>
            <li class="dialog-list-item">Shreyaan Pathak (2050027)</li>
            <li class="dialog-list-item">Timothy Zhong (2050060)</li>
          </ul>
        </div>

        <div>
          <h3 class="dialog-subheader">Team Information</h3>
          <ul class="dialog-list">
            <li class="dialog-list-item">#2050-1</li>
          </ul>
        </div>

        <img src="../assets/logo-wtsa.png" alt="Logo" height="200" />
      </div>
    </div>

    <div id="settings" class="modalDialog">
      <div class="dialog-box">
        <a href="#close" title="Close" class="close">X</a>

        <h2 class="dialog-header">Settings</h2>
        <p><em>Coming Soon</em></p>
      </div>
    </div>
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

/* MODAL BOXES */
.modalDialog {
  background: rgba(0, 0, 0, 0.5);
  transition: opacity 400ms ease-in;

  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 99999;
  opacity: 0;

  pointer-events: none;
}

.modalDialog:target {
  opacity: 1;
  pointer-events: auto;
}

.modalDialog > div {
  font-size: 18px;
  background: #eee;
  border: 2px solid #000;
  border-radius: 10px;

  position: relative;
  width: 800px;
  padding: 20px;
  margin: auto;
  margin-top: 50px;
}
.close {
  text-align: center;
  text-decoration: none;
  font-weight: bold;
  line-height: 25px;

  color: #ffffff;
  background: #000;
  border-radius: 12px;

  position: absolute;
  top: -10px;
  right: -12px;
  width: 24px;
}
.close:hover {
  background: #70c3ed;
}

/* ABOUT BOX */
.dialog-box {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 15px;
}

.dialog-header {
  font-size: 28px;
  color: #70c3ed;
}

.dialog-subheader {
  font-size: 20px;
  text-align: center;
  color: #000;
}

.dialog-list {
  display: flex;
  flex-direction: column;
}

.dialog-list-item {
  list-style-type: none;
  text-align: center;
}
</style>
