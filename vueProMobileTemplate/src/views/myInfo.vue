<template>
    <div class="view">
<!--        <el-button @click="toMe" style="margin-top: 20px; margin-left: 10px">返回</el-button>-->
        <van-nav-bar title="个人信息" right-text="" left-arrow @click-left="toMe" style="margin-bottom: 10px; background: #409EFF"/>

        <el-row style="margin-top:50px; padding:10px">
            <el-col>
                <div class="grid-content bg-purple">
                    <el-card class="box-card">
                        <div slot="header" class="clearfix">
                            <span>个人中心</span>
                        </div>
                        <div class="name-role">
                            <span class="sender">{{this.cookie.getCookie('username')}}</span>
                        </div>
<!--                        <div class="registe-info">-->
<!--                            <span class="registe-info">-->
<!--                                注册时间：-->
<!--                                <li class="fa fa-clock-o"></li>-->
<!--                                 2020/4/10 9:40:33-->
<!--                            </span>-->
<!--                        </div>-->
                        <el-divider></el-divider>
                        <div class="personal-relation">
                            <div class="relation-item">邮箱:  <div style="float: right; padding-right:20px;">{{dataForm.email}}</div></div>
                        </div>
                        <div class="personal-relation">
                            <div class="relation-item">注册时间:  <div style="float: right; padding-right:20px;">{{ dataForm.start_date }}</div></div>
                        </div>
<!--                        <div class="personal-relation">-->
<!--                            <div class="relation-item">首页链接:  <div style="float: right; padding-right:20px;">{{dataForm.homeUrl}}</div></div>-->
<!--                        </div>-->
                    </el-card>
                </div>
            </el-col>
        </el-row>
    </div>

</template>

<script>
    import {Info} from '../api/index'

    export default {
        name: "MyInfo",
        data(){
            var dataForm = null;
            return{
                dataForm
            }
        },
        methods: {
            getData(){
                var param = new FormData();
                param.append('username', this.cookie.getCookie('username'))
                Info(param).then((response) => {
                    if(response.status === 200){
                        console.log("success")
                        this.dataForm = response.data
                    } else {
                        // console.log(response)
                        // 提示信息
                        this.$toast.fail('个人信息加载失败')
                        // this.$toast.fail(response.data.msg)
                    }
                }).catch((error) => {
                    console.log(error)
                    this.$toast.fail('个人信息加载失败')
                })
            },
            toMe() {
                this.$router.push('/me')
            }
        },
        created() {
            this.getData()
        }
    }
</script>

<style scoped>
    /*卡片样式*/
    .text {
        font-size: 14px;
    }

    .item {
        margin-bottom: 18px;
    }

    .clearfix:before,
    .clearfix:after {
        display: table;
    }
    .clearfix:after {
        clear: both
    }
    /*文本样式区*/
    .name-role {
          font-size: 16px;
          padding: 5px;
          text-align:center;
      }
    .sender{
        text-align:center;
    }
    .registe-info{
        text-align: center;
        padding-top:10px;
    }
    .personal-relation {
        font-size: 16px;
        padding: 0px 5px 15px;
        margin-right: 1px;
        width: 100%
    }

    .relation-item {
        padding: 12px;

    }
    .dialog-footer{
        padding-top:10px ;
        padding-left: 10%;
    }
    /*布局样式区*/
    .el-row {
        margin-bottom: 20px;
    }
    .el-col {
        border-radius: 4px;
    }
    .bg-purple-dark {
        background: #99a9bf;
    }
    .bg-purple {
        background: #d3dce6;
    }
    .bg-purple-light {
        background: #e5e9f2;
    }
    .grid-content {
        border-radius: 4px;
        min-height: 36px;
    }
    .row-bg {
        padding: 10px 0;
        background-color: #f9fafc;
    }
</style>
