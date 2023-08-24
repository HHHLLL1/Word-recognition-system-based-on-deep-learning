<template>
  <div class="main">
    <header-top title="Home"/>
    <div style="margin-top: 55px">
      <div class="clearfix">
        <img src="../assets/images/people.png" class="user-head" @click="changeAvatar()" alt="">
        <span class="user-name">{{ this.cookie.getCookie('username') }}</span>
      </div>
      <div class="select my-collection" @click="myInfo()">
        <span class="left">个人信息</span>
        <i class="el-icon-star-on right"></i>
        <!-- <i class="el-icon-arrow-right right"></i> -->
      </div>
      <div class="select my-publish" @click="myHistory()">
        <span class="left">识别历史</span>
        <i class="el-icon-edit-outline right"></i>
        <!-- <i class="el-icon-arrow-right"></i> -->
      </div>
      <div class="select change-password" @click="changePassword()">
        <span class="left">修改密码</span>
        <i class="el-icon-setting right"></i>
      </div>
      <div>
        <el-row type="flex" justify="center" style="margin-left: 50px; margin-right: 50px; margin-top: 10px">
          <el-button type="danger" @click="signOut()">退出登录</el-button>
        </el-row>
      </div>
    </div>
  </div>

</template>
<script>
  import HeaderTop from '../components/HeaderTop'

  export default {
    data() {
      return {
      }
    },
    mounted(){
    },
    methods:{
      changeAvatar() {
        this.$router.push('/changeAvatar');
      },
      changePassword() {
        this.$router.push('/changePWD');
      },
      myInfo() {
        this.$router.push('/info');
      },
      myHistory() {
        this.$router.push('/history');
      },
      signOut() {
        this.cookie.clearCookie('username')
        // this.cookie.clearCookie('password')
        window.localStorage.clear();
        //清空vuex数据
        window.location.reload()
        //清空消息记录
        //this.actionClearMsgRecord()
        this.$router.push('/');
      }
    },
    components:{
      HeaderTop
    }
  }
</script>
<style lang="stylus" rel="stylesheet/stylus" scoped>
  @import "../common/stylus/mixin.styl"
  .main{
    padding: 5px
  }
  .block {
    height: 56px;
  }
  .clearfix {
    height: 60px;
    padding: 10px;
    width: 90%;
    /*border-bottom: 1px solid #ebeef5;*/
    /*box-sizing: border-box;*/
    margin: 0 auto;
    margin-top: 5px;
  }
  .user-head {
    width: 60px;
    height: 60px;
    border-radius: 50%;
    float: left;
  }
  .user-name {
    float: left;
    margin-left: 10px;
    text-align: left;
    /*font-weight: bold;*/
    text-overflow:ellipsis;
    width: 50%;
    height: 20px;
    overflow: hidden;
    white-space: nowrap;
    font-size: 17px;
    font-weight: bold;
  }
  .select {
    width: 90%;
    margin: 0 auto;
    border-bottom: 1px solid #ebeef5;
    height: 50px;
    font-size: 15px;
  }
  .left {
    float: left;
    padding-top: 20px;
  }
  .right {
    float: right;
    padding-top: 20px;
  }
  .el-button {
    width: 100%;
    margin-top: 20px;
    transition: .7s;
    overflow: hidden;
    justify-content: center;
  }



</style>
