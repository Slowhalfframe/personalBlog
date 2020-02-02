<template>
    <div>
        <TopBar :website="website"/>
        <Nav :nav="nav"/>
        <ArticleList :lists="articleList"/>
        <Footer :record="website"/>
    </div>
</template>

<script>
  import TopBar from "../components/public/top_bar";
  import Nav from '../components/public/nav'
  import ArticleList from "../components/articleList";
  import Footer from "../components/public/footer";
  import axios from "../plugins/axios";
  import host from "../plugins/host";

    export default {
        name: "index",
        components:{
            TopBar, Nav, ArticleList, Footer
        },
        data(){
            return{
                articleList: '',
                website: '',
                nav: '',
                keywords:'',
                descriptions: '',
            }
        },
        async asyncData () {
            let [articleList, website, nav] = await Promise.all([
                axios.get('/articles/article/'),
                axios.get('/common/website/'),
                axios.get('/common/nav/')
            ])

            return {
                articleList: articleList.data,
                website: website.data,
                nav: nav.data,
            }
        },
        mounted(){
            for(var i=0; i<this.articleList.length; i++){
                // console.log(this.articleList[i].title)
                // 生成关键字
                this.keywords += this.articleList[i].title;
                this.keywords += ",";
                //生成descriptions
                this.descriptions += this.articleList[i].title;
                this.descriptions += this.articleList[i].desc;
                this.descriptions += ",";
            }
        },
        head(){
            return{
                title: this.website.name +"--"+ this.website.desc + "--个人博客站点" ,
                meta: [
                    { hid: 'description', name: 'description', content: this.descriptions + '慢半帧, manbanzhen, python, vue, js.photoshop, ps' },
                    { hid: 'keywords', name: 'keywords', content: this.keywords + '慢半帧, manbanzhen, python, vue, js.photoshop, ps'}
                ],
            }
        }
    }
</script>

<style>

</style>
