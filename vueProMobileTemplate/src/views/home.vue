<template>
  <div>
    <header-top title="首页"/>
      <div  style="margin-bottom: 50px; margin-top: 50px">
        <div class="content">
            <div>
                <img src="../assets/gifs/1.gif" @click="toupload" alt="上传">
            </div>
        </div>
          <div class="content-lan">
                <div style="margin-top: 10px; margin-left: 12px">
                    语种
                </div>
              <div style="padding: 10px; margin: 5px">
                  <img src="../assets/images/en.png" style="height: 60px; width: 100px; margin: 2px" @click="toupload_en" alt="en上传">
                  <img src="../assets/images/french.png" style="height: 60px; width: 100px; margin: 2px" @click="toupload_french" alt="french上传">
                  <img src="../assets/images/german.png" style="height: 60px; width: 100px; margin: 2px" @click="toupload_german" alt="german上传">
                  <img src="../assets/images/japan.png" style="height: 60px; width: 100px; margin: 2px" @click="toupload_japan" alt="japan上传">
              </div>

          </div>
          <div class="content-lan" style="margin-top: 20px">
              <div style="margin-top: 10px; margin-left: 12px">
                  应用
              </div>
              <div style="padding: 10px; margin: 5px">
                  <img src="../assets/images/idcard.png" style="height: 60px; width: 100px; margin: 2px" @click="toupload_idcard" alt="idcard上传">
                  <img src="../assets/images/carcard.png" style="height: 60px; width: 100px; margin: 2px" @click="toupload_carcard" alt="carcard上传">
              </div>

          </div>
      </div>
  </div>
</template>
<script>
  import headerTop from '../components/HeaderTop'

  export default {
    name: 'Home',
    data() {
      return {
      }
    },
    mounted(){
    },
    methods:{
        toupload(){
            this.$router.push({
                name: 'Upload',
            })
        },
        toupload_en(){
            this.$router.push({
                name: 'Upload_lan',
                params: {
                    type: 'en'
                }
            })
        },
        toupload_french(){
            this.$router.push({
                name: 'Upload_lan',
                params: {
                    type: 'french'
                }
            })
        },
        toupload_german(){
            this.$router.push({
                name: 'Upload_lan',
                params: {
                    type: 'german'
                }
            })
        },
        toupload_japan(){
            this.$router.push({
                name: 'Upload_lan',
                params: {
                    type: 'japan'
                }
            })
        },
        toupload_idcard(){
            this.$router.push({
                name: 'Upload_idcard',
                params: {
                    type: 'idcard'
                }
            })
        },
        toupload_carcard(){
            this.$router.push({
                name: 'Upload_carcard',
                params: {
                    type: 'carcard'
                }
            })
        }

    },
    components: {
      headerTop,
    },
  }
</script>

<style lang="stylus" rel="stylesheet/stylus" scoped>
  @import "../common/stylus/mixin.styl"
  *{
      padding: 0;
      margin: 0;
  }
  body{
      height: 100%;
      background-color: #7f8c8d;
      display: flex;
      justify-content: center;
  }
  .content{
      top: 20px;
      position: relative;
      overflow: hidden;
      display: flex;
      justify-content: center;
  }
  .content-lan{
      margin: 5px;
      background: white;
      margin-top: 40px;
      /*边框*/
      border: solid 1px rgba(102, 146, 191, 0.68);
      /*边角弧度*/
      border-radius: 10px;
      /*延迟过度*/
      -moz-box-sizing:border-box; /* Firefox */
      -webkit-box-sizing:border-box;
      -o-box-sizing:border-box; /* Opera */
      transition: all 0.3s linear;/*0.3s过渡时间*/
      -moz-transition: all 0.3s linear; /* Firefox 4 */
      -webkit-transition: all 0.3s linear; /* Safari 和 Chrome */
  }
  .content-lan:hover{
      /*边框*/
      border: solid 1px rgba(102, 146, 191, 0.68);
      /*边角弧度*/
      border-radius: 10px;
      box-shadow: 7px 15px 30px #285a63;
  }
  img{
      height: 200px;
      width: 300px;
      transition: .7s;
      overflow: hidden;
      justify-content: center;
  }


</style>
