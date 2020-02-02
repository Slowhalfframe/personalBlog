<template>
    <div id="window">
      <div id="title">
        <h3>{{content.title}}</h3>
        <p>{{content.create_time}} | 浏览：{{content.read_num}} | 文章类别： <nuxt-link :to="content.articletypeurl">{{content.articleTypeName}}</nuxt-link></p>
      </div>
        <div v-html="content.content" id="content"></div>
      <div id="like">
        <el-button type="danger" @click="like()">喜欢({{content.like_num}})</el-button>
      </div>
    </div>
</template>

<script>
  import axios from "../plugins/axios";
  export default {
      props: ['content'],
      data(){
          return{
          }
      },
      methods:{
          like(){
              var self = this;
              if(!window.localStorage.getItem(self.content.id)){
                  axios.get("articles/like/"+self.content.id+"/")
                      .then(function (res) {
                          if(res.data.code === 0){
                              window.localStorage.setItem(self.content.id, true);
                              self.content.like_num += 1;
                          }
                      })
                      .catch(function (error) {
                          self.$message.error("《" + self.content.title + "》喜欢上了别人~")
                      })
              }else{
                  self.$message.warning("《" + self.content.title + "》已经被您喜欢过了！")
              }
          }
      }
  }
</script>

<style scoped>
  #window{
    width: 50%;
    height: auto;
    margin: 20px auto;
    padding: 10px;
  }
  #title{
    padding: 20px;
    border: 1px solid #efefef;
  }
  #content{
    padding: 20px;
    line-height: 2;
    border: 1px solid #f1f1f1;
  }
  #content >>> img{
    width: 100%;
    height: auto;
  }
  #like{
    margin: 30px auto;
    width: 95px;
    height: 20px;
  }
</style>
