<template>
  <div id="app">
    <router-view/>
<!--    <header-top v-if="$route.meta.isHead"></header-top>-->
    <foot-bar v-if="$route.meta.isMenu"></foot-bar>
  </div>
</template>
<script>
  import footBar from '@/components/footBar'
  // import HeaderTop from "./components/HeaderTop";
  export default {
    name: 'App',
    components: {
      // HeaderTop,
      footBar
    },
  }
</script>
<style lang="stylus">
#app
  font-size 16px//默认字体大小
</style>
