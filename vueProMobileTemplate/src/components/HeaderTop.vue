<template>
  <div class="header">
    <slot name="left"></slot>
    <span class="header_title">
      <span class="header_title_text ellipsis">{{title}}</span>
    </span>
    <slot name="right"></slot>
  </div>
</template>

<script>
  export default {
      props:{
        title:String
      }
  }
</script>

<style lang="stylus" rel="stylesheet/stylus">
  @import "../common/stylus/mixin.styl"
  .header
    background-color $color-theme
    /*position fixed*/
    position fixed  //固定header
    z-index 100
    left 0
    top 0
    width 100%
    display: flex;
    align-items: center;
    justify-content: space-around;
    height $header-title-height
    .header_title
      position absolute
      top 50%
      left 50%
      transform translate(-50%, -50%)
      width 50%
      color #fff
      text-align center
      .header_title_text
        font-size 18px
        color #fff
        display block

</style>
