<script setup>
import Header from "./components/Header.vue";
import Aside from "./components/Aside.vue";
import Article from "./components/Article.vue";
import Footer from "./components/Footer.vue";

// const fetchItems = async (url) => {
//     const res = await fetch(url, {
//       'methods':'GET',
//       headers : {
//         'Content-Type':'application/json'
//       }
//     });
//     const data = await res.json();
//     console.log(data)
//     return data;
//   } 

const species = []

function readTextFile(file)
{
    var rawFile = new XMLHttpRequest();
    rawFile.open("GET", file, false);
    var allText = "";
    rawFile.onreadystatechange = function ()
    {
        if(rawFile.readyState === 4)
        {
            if(rawFile.status === 200 || rawFile.status == 0)
            {
                allText = rawFile.responseText;
                console.log(allText);
                // return allText;
            }
        }
    }
    rawFile.send(null);
    return allText;
}

const fetchItems = () => {
  species.push(readTextFile("../cache/Data/Africa/Animal Name Bat-Eared Fox.txt").split("\n"));
  species.push(readTextFile("../cache/Data/Africa/Animal Name Black and White Colobus.txt").split("\n"));
  species.push(readTextFile("../cache/Data/Africa/Animal Name Gerenuk.txt").split("\n"));
  species.push(readTextFile("../cache/Data/Antartica/Animal Name Antarctic hair grass.txt").split("\n"));
  species.push(readTextFile("../cache/Data/Antartica/Animal Name Antarctic springtail.txt").split("\n"));
  species.push(readTextFile("../cache/Data/Antartica/Animal Name Hoff Crab.txt").split("\n"));
}

fetchItems();
console.log(species);
</script>

<template>
  <Header class="header" />

  <div class="main-body">
    <Aside class="aside" />
    <Article class="article" :species="species" />
  </div>

  <Footer class="footer" />
</template>

<style scoped>
/* MAIN BODY */
.main-body {
  display: flex;
}

.aside {
  flex: 0 0 20%;
}

.article {
  flex: 1;
}
</style>
