<template>
    <footer>
        <div class="inside">
            ©2019 <a href="http://www.manbanzhen.top">慢半帧</a> |
            备案号：<a :href="record.record_url">{{record.record_info}}</a>
        </div>
    </footer>
</template>

<script>
export default {
    props: ['record']
}
</script>

<style scoped>
  footer{
    position: absolute;
    left: 0;
    bottom: 0;
    width: 100%;
    height: 50px;
  }
    .inside{
        width: 360px;
        height: 50px;
        margin: 0 auto;
        line-height: 50px;
        color: #111;
        font-size: 15px;
        letter-spacing: 1px;
    }
    .inside a{
        color: #111;
        text-decoration: none;
    }
</style>
