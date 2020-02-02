import axios from 'axios'


// 设置baseURL
// axios.defaults.baseURL = 'http://127.0.0.1:8000/api/';
axios.defaults.baseURL = 'http://www.manbanzhen.top/api/';

// 创建axios对象，暴露
export default axios.create()
