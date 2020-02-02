<template>
    <div id="window">
        <div id="inside">
            <h1>{{website.name}}</h1>
            <h2>{{website.desc}}</h2>
        </div>
        <!-- {{website}} -->
    </div>
</template>

<script>
import axios from "~/plugins/axios"

export default {
    props: ['website'],
    data(){
        return{
            title: '',
            desc: '',
            record_info: '',
            record_url: '',
        }
    },

}
</script>



<style scoped>
    #window{
        width: 100%;
        height: 150px;
        margin: 0 auto;
        border-bottom: 1px solid #5656;
    }
    #inside{
        width: 60%;
        height: 150px;
        margin: 0 auto;
        padding: 10px;
    }
    #inside h1{
        font-size: 30px;
        line-height: 30px;
        color: #111;
        margin-top: 30px;
    }
    #inside h2{
        font-size: 22px;
        line-height: 22px;
        padding-left: 33px;
        color: #0f0f0f;
        margin-top: 20px;
    }
</style>