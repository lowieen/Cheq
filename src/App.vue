<script>
import HeaderComponent from './components/Header.vue';
import LoginComponent from './components/Login.vue';
import FooterComponent from './components/Footer.vue';
import CarshopComponent from './components/Carshop.vue';

export default {
  components: {
    'header-component': HeaderComponent,
    'footer-component': FooterComponent,
    'login-component': LoginComponent,
    'carshop-component': CarshopComponent
  }
}
</script>


<template>
  <div id="app">
    <header-component></header-component>
    <router-view></router-view>
    <footer-component></footer-component>
  </div>
</template>
