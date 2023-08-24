<template>
    <div >
<!--        <el-button @click="toHome" style="margin-top: 20px; margin-left: 10px">返回</el-button>-->
        <van-nav-bar title="识别结果" right-text="" left-arrow @click-left="toHome" style="margin-bottom: 10px; background: #409EFF"/>
        <div class="item" v-for="(item,index) in dectdata" :key="(item,index)">
            <div class="content-detail" style="padding: 30px">
<!--                <img v-bind:src="item.file" alt="">-->
                <div class="imgp">
                    <img class="preview-img" v-bind:src="item.file" height="100" alt="">
                </div>
                <div class="text"  v-html="item.text">

                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import {uploadRoot} from '../api/config'

    export default {
        name: "Detail",
        data(){
            var dectdata = null;
            var url = uploadRoot;
            return{
                dectdata,
                url
            }
        },
        methods: {
            getData() {
                this.dectdata = this.$route.params.data
                this.dectdata.forEach((ele)=>{
                    ele.w=300;
                    ele.h=200;//缩率图显示的高
                })
                console.log(this.dectdata)
            },
            toHome() {
                this.$router.push('/home')
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
        margin: 10px;
        margin-top: 20px;
        background: white;
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

        margin-top: 20px;
        position: relative;
        overflow: hidden;
        display: flex;
        justify-content: center;
    }
</style>
