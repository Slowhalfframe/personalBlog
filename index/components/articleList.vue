<template>
    <div id="bigbox">
      <div v-if="lists.length > 0">
        <div class="item" v-for="item in lists" :key="item.title">
            <h2><nuxt-link :to="detailUrl(item.id)">{{item.title}}</nuxt-link></h2>
            <div class="mark">
              <div class="desc">{{item.desc}}</div>
              <div class="img dis" v-if="item.cove_img"><img :src="host + item.cove_img" alt=""></div>
            </div>
            <div class="footer">
              <span class="dis">时间：{{item.create_time}}</span>
              <span>分类：<nuxt-link :to="item.articletypeurl">{{item.articletypename}}</nuxt-link></span> |
              <span>阅读量：{{item.read_num}}</span> |
              <span>喜欢：{{item.like_num}}</span>
            </div>
        </div>
<!--        <div class="item" v-for="item in lists" :key="item.title">-->
<!--            <h2>-->
<!--                <nuxt-link :to="detailUrl(item.id)">-->
<!--                {{item.title}}-->
<!--                </nuxt-link>-->
<!--            </h2>-->
<!--            <div class="con">-->
<!--                <div class="left">-->
<!--                    <div class="mark">-->
<!--                        {{item.desc}}-->
<!--                    </div>-->
<!--                    <div class="bottom">-->
<!--                        <span>时间：{{item.create_time}}</span>-->
<!--                      <span>分类： <nuxt-link :to="item.articletypeurl">{{item.articletypename}}</nuxt-link></span>-->
<!--                        <span>阅读量： {{item.read_num}}</span>-->
<!--                        <span>喜欢： {{item.like_num}}</span>-->
<!--                    </div>-->
<!--                </div>-->
<!--                <div class="right">-->
<!--                    <img :src="host + item.cove_img" alt="">-->
<!--                </div>-->
<!--            </div>-->
<!--        </div>-->
      </div>
      <div v-else>暂无文章</div>
    </div>
</template>

<script>
import host from '~/plugins/host'

export default {
  props: ['lists'],
  data(){
      return{
          host: host,
      }
  },
    methods:{
        detailUrl(url){
            return '/detail/'+ url + '/';
        }
    }
}
</script>


<style scoped>
  @import "assets/css/articleList.css";

  /*  #bigbox{*/
  /*      width: 50%;*/
  /*      height: auto;*/
  /*      margin: 20px auto;*/
  /*  }*/
  /*  .item{*/
  /*      width: 100%;*/
  /*      !*height: 150px;*!*/
  /*      height: auto;*/
  /*      border: 1px dashed #345;*/
  /*      border-radius: 5px;*/
  /*  }*/
  /*  .item h2{*/
  /*      padding: 10px;*/
  /*      font-size: 22px;*/
  /*  }*/
  /*  .item h2 a,*/
  /*  .con .left .bottom a{*/
  /*      text-decoration: none;*/
  /*      color: #222;*/
  /*  }*/
  /*  .con{*/
  /*      width: 100%;*/
  /*      !*height: 100px;*!*/
  /*      height: auto;*/
  /*  }*/
  /*  .con .left{*/
  /*      float: left;*/
  /*      width: 75%;*/
  /*      height: 100px;*/
  /*  }*/
  /*  .con .left .mark{*/
  /*      padding: 5px 10px;*/
  /*      height: 50px;*/
  /*      margin: 5px;*/
  /*  }*/
  /*  .con .left .bottom{*/
  /*      padding: 6px 10px;*/
  /*  }*/
  /*  .con .left .bottom span{*/
  /*      margin-right: 15px;*/
  /*  }*/
  /*  .con .right{*/
  /*      float: right;*/
  /*      width: 12%;*/
  /*      padding-right: 20px;*/
  /*  }*/
  /*  .item img{*/
  /*      width: 100%;*/
  /*      height: 100px;*/
  /*      border-radius: 6px;*/
  /*  }*/
  /*  .bottom{*/
  /*    width: 100%;*/
  /*    overflow: hidden;*/
  /*  }*/

  /*!*适配移动端*!*/
  /*@media (max-width: 1550px) {*/
  /*  #bigbox{*/
  /*    width: 80%;*/
  /*  }*/
  /*}*/

  /*  @media (max-width: 960px) {*/
  /*    #bigbox{*/
  /*      width: 98%;*/
  /*    }*/
  /*    !*.bottom{*!*/
  /*    !*  display: none;*!*/
  /*    !*}*!*/
  /*    .con .left{*/
  /*      float: left;*/
  /*      width: 98%;*/
  /*    }*/
  /*    .con .right{*/
  /*      display: none;*/
  /*    }*/
  /*  }*/
</style>
