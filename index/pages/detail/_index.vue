<template>
  <div>
    <Nav :nav="nav"/>
    <Content :content="article"/>
    <Footer :record="website"/>
  </div>
</template>

<script>
    // import Nav from '~/components/public/nav.vue'
    // import Content from '~/components/content.vue'
    // import Footer from "../components/public/footer";
    // import host from "../plugins/host";
    // import axios from "../plugins/axios";

    import Nav from "../../components/public/nav";
    import Content from "../../components/content";
    import Footer from "../../components/public/footer";
    import axios from "../../plugins/axios";
    import host from "../../plugins/host";

    export default {
        components: {
            Footer, Nav, Content
        },
        data(){
            return{
                article: '',
                website: '',
                nav: '',
            }
        },
        head () {
            return {
                title: this.article.title,
                meta: [
                    { hid: 'description', name: 'description', content: this.delHtmlTag(this.article.content) },
                    { hid: 'keywords', name: 'keywords', content: this.article.title + this.article.desc + '慢半帧' }
                ],
                link: [
                    {rel: 'stylesheet', href:   '/code.css'}
                ]
            }
        },
        methods:{
            delHtmlTag(str){
                return str.replace(/<[^>]+>/g,"");  //正则去掉所有的html标记
            }
        },
        async asyncData (pages) {
            let [article, website, nav] = await Promise.all([
                axios.get('/articles/detail/'+pages.route.params.index + '/'),
                axios.get('/common/website/'),
                axios.get('/common/nav/')
            ])

            return {
                article: article.data,
                website: website.data,
                nav: nav.data,
            }
        },
    }
</script>

<style scoped>

</style>
