<template>
    <div class="view">
        <van-nav-bar title="历史记录" right-text="" left-arrow @click-left="toMe" style="margin-bottom: 10px; background: #409EFF"/>

        <div class="item" v-for="(item,index) in historydata" :key="(item,index)" style="padding:10px" >
            <el-card class="box-card">
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
                    识别结果：
                    <br><br>
                    <div style="width: 100%; height: 100%" v-html="item.text"></div>
                </div>
            </el-card>
        </div>
    </div>
</template>

<script>
    import {uploadRoot} from "../api/config";
    import {History_info} from "../api/index";

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
    .text{
        padding-top: 10px;
        margin-top: 20px;

    }

    /*卡片样式*/
    .text {
        font-size: 14px;
        width: 100%;
    }

    .item {
        margin-bottom: 18px;
    }

</style>
