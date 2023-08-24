<template>
    <div class="app-container">
<!--        <el-button @click="toHome" style="margin-top: 20px; margin-left: 10px">返回</el-button>-->
<!--        <el-button @click="updatePic" style="float: right; margin-top: 20px; margin-right: 10px">上传</el-button>-->
        <van-nav-bar title="选择图片-身份证" right-text="识别" left-arrow @click-left="toHome"  @click-right="updatePic" />
        <div class="image-view">
            <el-form>
                <el-form-item>
                    <div class="addbox">
                        <!-- accept ： 接收类型；    image/*  ： 所有类型图片；   multiple： 多个     -->
                        <input type="file" @change="getImgBase()" name="file" accept="image/*" multiple>
                        <div class="addbtn">+</div>
                        <div class="texttips">&nbsp;添加图片</div>
                    </div>
                </el-form-item>
            </el-form>
            <div class="view">
                <div class="item" v-for="(item, index) in imgfilesPre" :key="(item, index)">
                    <span class="cancel-btn" @click="delImg(index)">x</span>
                    <img v-bind:src="item" alt="">
                </div>
            </div>
        </div>

        <div id="app">
            <router-view/>
            <loading></loading>
        </div>

    </div>
</template>
<script>
    import {Upload_idcard} from "../api/index";
    import Loading from "@/components/loading"

    export default {
        name: 'Upload_idcard',
        data() {
            return {
                imgfilesPre: [],      // 图片预览地址
                imgfiles: [],  // 图片原文件，上传到后台的数据
            }
        },
        created() {
        },
        methods: {
            //获取图片base64实现预览
            getImgBase() {
                var _this = this;
                var event = event || window.event;
                var fileList = event.target.files;
                let length = fileList.length;

                for (let i = 0; i < length; i++) {
                    var reader = new FileReader();
                    _this.imgfiles.push(fileList[i]);
                    reader.readAsDataURL(fileList[i]);

                    //转base64 base 64 图片地址形成预览
                    reader.onload = function (e) {
                        _this.imgfilesPre.push(e.target.result);
                    };
                }
                // 防止不能连续选同一图片
                event.target.value = "";
            },

            //删除图片
            delImg(index) {
                this.imgfilesPre.splice(index, 1);
            },

            // 上传图片至服务端
            updatePic() {
                this.bus.$emit('loading', true);
                var param = new FormData();
                var length = this.imgfiles.length;
                param.append('username', this.cookie.getCookie('username'))
                param.append('filetype', 'idcard')
                for (let i = 0; i < length; i++) {
                    let file = this.imgfiles[i];
                    // console.log(file, file['name'])
                    param.append('file', file, file['name'])
                }
                console.log(param.getAll("file"))

                this.listLoading = true;

                Upload_idcard(param).then((response) => {
                    this.bus.$emit('loading', false);
                    if(response.status === 201){
                        console.log("success")
                        this.$router.push({
                            name: "Detail", // 注：这里不能用path路径，只能用name【请对照router.js中的路由规则中的name项】，否则取不到传过去的数据
                            params: {
                                data: response.data
                            }
                        });
                    } else {
                        // console.log(response)
                        // 提示信息
                        this.$toast.fail('识别失败')
                        // this.$toast.fail(response.data.msg)
                    }
                }).catch((error) => {
                    this.bus.$emit('loading', false);
                    console.log(error)
                    this.$toast.fail('数据上传失败')
                })
            },
            toHome(){
                this.$router.push('/home')
            }
        },
        components:{
            Loading,
        }
    }
</script>
<style scoped>

    .image-view {
        width: auto;
        margin: 50px auto;

    }

    .image-view .addbox {
        margin: 0 auto;
        position: relative;
        height: 100px;
        width: 100px;
        margin-bottom: 20px;
        text-align: center;
    }

    .image-view .addbox input {
        position: absolute;
        height: 100px;
        width: 100px;
        opacity: 0;
        text-align: center;
    }

    .image-view .addbox .addbtn {

        height: 100px;
        width: 100px;
        line-height: 100px;
        color: #fff;
        font-size: 40px;
        background: #ccc;
        border-radius: 10px;
        text-align: center;
    }

    .image-view .texttips {
        color: #001528;
        text-align: center;
    }

    .image-view .item {
        position: relative;
        float: left;
        height: 100px;
        width: 100px;
        margin: 10px 10px 0 0;
    }

    .image-view .item .cancel-btn {
        position: absolute;
        right: 0;
        top: 0;
        display: block;
        width: 20px;
        height: 20px;
        color: #fff;
        line-height: 20px;
        text-align: center;
        background: red;
        border-radius: 10px;
        cursor: pointer;
    }

    .image-view .item img {
        width: 100%;
        height: 100%;
    }

    .image-view .view {
        clear: both;
    }
</style>
