<template>
    <div>
      <product-list :title="title"></product-list>
    </div>
</template>
  
<script>
  import ProductList from "@/components/ProductList.vue";
  
  export default {
    components: {
      ProductList
    },
    data(){
      return {
        title: null,
      }
    },
    methods:{
      changeTitle(){
        this.title = 'Pantalones'
      }
    },
    mounted(){
      this.changeTitle();
    },
    beforeRouteEnter(to, from, next) {
      window.scrollTo(0, 0);
      next();
    },
  };
  </script>