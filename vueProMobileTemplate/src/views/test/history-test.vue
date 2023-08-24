<template>
    <div class="view">
        <el-button @click="toMe" style="margin-top: 20px; margin-left: 10px">返回</el-button>
<!--        <div class="item" v-for="(item,index) in historydata" :key="(item,index)" style="padding:10px" >-->
<!--            <div class="content-detail" style="padding: 10px">-->
<!--                &lt;!&ndash;                <img v-bind:src="item.file" alt="">&ndash;&gt;-->
<!--                <div class="imgp">-->
<!--                    <img class="preview-img" v-bind:src="item.file" height="100" alt="">-->
<!--                </div>-->
<!--                <div class="text">-->
<!--                    类型：{{ item.filetype }}-->
<!--                </div>-->
<!--                <div class="text">-->
<!--                    时间：{{ item.date }}-->
<!--                </div>-->
<!--                <div class="text">-->
<!--                    识别结果：{{ item.text }}-->
<!--                </div>-->
<!--            </div>-->
<!--        </div>-->

        <el-row style="margin-top:50px; padding:10px">
            <el-col>
                <div class="grid-content bg-purple">
                    <el-card class="box-card">
                        <div class="item" v-for="(item,index) in historydata" :key="(item,index)" style="padding:10px" >
                            <div class="content-detail" style="padding: 10px">
                                <!--                <img v-bind:src="item.file" alt="">-->
                                <div class="imgp">
                                    <img class="preview-img" v-bind:src="item.file" height="100" alt="">
                                </div>
                                <div class="text">
                                    类型：{{ item.filetype }}
                                </div>
                                <div class="text">
                                    时间：{{ item.date }}
                                </div>
                                <div class="text">
                                    识别结果：{{ item.text }}
                                </div>
                            </div>
                        </div>
                    </el-card>
                </div>
            </el-col>
        </el-row>
    </div>
</template>

<script>
    import {uploadRoot} from "../../api/config";
    import {History_info} from "../../api";

    export default {
        name: "History",
        data(){
            var historydata = null;
            var url = uploadRoot;
            return{
                historydata,
                url
            }
        },
        methods: {
            getData() {
                var param = new FormData();
                param.append('username', this.cookie.getCookie('username'))
                History_info(param).then((response) => {
                    if(response.status === 201){
                        console.log("success")
                        this.historydata = response.data
                    } else {
                        // console.log(response)
                        // 提示信息
                        this.$toast.fail('历史信息加载失败')
                        // this.$toast.fail(response.data.msg)
                    }
                }).catch((error) => {
                    console.log(error)
                    this.$toast.fail('历史信息加载失败')
                })
                this.dectdata.forEach((ele)=>{
                    ele.w=300;
                    ele.h=200;//缩率图显示的高
                })
                console.log(this.dectdata)
            },
            toMe() {
                this.$router.push('/me')
            }
        },
        created:function () {
            this.getData()
        }
    }
</script>

<style scoped>
    .imgp{
        margin-top: 20px;
        position: relative;
        overflow: hidden;
        display: flex;
        justify-content: center;
    }
    .content-detail{
        background: #f9fafc;
        margin-top: 20px;
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
    .content-detail:hover{
        /*边框*/
        border: solid 1px rgba(102, 146, 191, 0.68);
        /*边角弧度*/
        border-radius: 10px;
        box-shadow: 7px 15px 30px #285a63;
    }
    .text{
        padding-top: 10px;
        margin-top: 20px;
        position: relative;
        overflow: hidden;
        display: flex;
        justify-content: center;
    }

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
