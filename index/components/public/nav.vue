<template>
    <div id="window">
        <div id="inside">
            <ul>
                <li><nuxt-link to="/">首页</nuxt-link></li>
                <li v-for="item in nav" :key="item.name">
                  <a v-if="item.sort != -1" :href="item.url">
                  {{item.name}}
                  </a>
                  <nuxt-link :to="item.url" v-else>{{item.name}}</nuxt-link>
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
  export default {
      props:['nav']
  }
</script>


<style scoped>
    #window{
        width: 100%;
        height: 70px;
        background-color: #223;
        border-top: 1px solid #abc;
        border-bottom: 1px solid #abc;
        color: #efefef;
    }
    #inside{
        width: 65%;
        height: 70px;
        margin: 0 auto;
    }
    #inside ul li{
        float: left;
      /*padding: 0 20px;*/
        /*width: 99px;*/
        text-align: center;
        height: 70px;
        list-style: none;
        line-height: 70px;
    }
    #inside ul li a{
        display: inline-block;
        /*width: 99px;*/
        height: 70px;
        color: #efefef;
        text-decoration: none;
        font-size: 19px;
        padding: 0 30px;
    }
    #inside ul li a:hover{
        background-color: #234;;
    }

    @media (max-width: 1550px){
      #inside{
        width: 85%;
      }
    }

  @media (max-width: 960px) {
    #inside{
      width: 98%;
    }
    #inside ul li a{
      padding: 0 15px;
    }
  }
</style>
