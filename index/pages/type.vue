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
        async asyncData (pages) {
            var query = encodeURI(pages.route.query.typename);
            let [articleList, website, nav] = await Promise.all([
                axios.get('/articles/article/?typename='+query),
                axios.get('/common/website/'),
                axios.get('/common/nav/')
            ])

            return {
                articleList: articleList.data,
                website: website.data,
                nav: nav.data,
            }
        },
        computed:{
            typeName(){
                return this.$route.query.typename
            }
        },
        watch:{
            typeName:function (newVal, oldVal) {
                var self = this;
                axios.get('/articles/article/?typename='+newVal)
                    .then(function (res) {
                        self.articleList = res.data;
                    })
                    .catch(function (error) {
                        self.$message.error("出现意外错误")
                    })
            }
        },
        head(){
            return{
                title: this.website.name +"--"+ this.website.desc + "--个人博客站点" ,
                meta: [
                    { hid: 'description', name: 'description', content: "当前页面文章类型为：" + this.$route.query.typename + "; " + this.descriptions + '慢半帧, manbanzhen, python, vue, js.photoshop, ps' },
                    { hid: 'keywords', name: 'keywords', content: "当前页面文章类型为：" + this.$route.query.typename + "; " + this.keywords + '慢半帧, manbanzhen, python, vue, js.photoshop, ps'}
                ],
            }
        }
    }
</script>

<style>

</style>
