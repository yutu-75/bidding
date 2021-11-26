<template>

  <!--      site-header no-select is-homepage gizle sabit-->
  <!--      site-header no-select is-homepage gizle yya-->
  <!--      site-header no-select is-homepage gizle sabit-->
  <!--      site-header no-select is-homepage gizle sabit-->
  <div class="top">

    <!--    <div class="scrollbar" id="bar" :style="sliderStyle"></div>-->
    <!--    <a href="#" :class="c_top" :style="s_top"></a>-->

    <!--navbar navbar-default site-header no-select is-homepage gizle yya-->

    <nav :class="class_header" role="navigation">
      <div class="container-fluid">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle" data-toggle="collapse"
                  data-target="#example-navbar-collapse">
            <span class="sr-only">切换导航</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <div class="site-branding">
          <span class="site-title">
            <span class="logolink moe-mashiro"><a href="/"><img src="@/assets/logo1.png" alt="">  <span class="shironeko"> 招标信息</span></a> </span>
          <span class="logolink moe-mashiro" v-show="false">
            <router-link to='/' alt="津久见的白猫">
              <ruby>
                <span class="sakuraso"> bidding  </span>
                <span class="no">❄</span>
                <span class="shironeko"> 招标信息</span>
                <rp></rp>
                <rt class="chinese-font">招标信息</rt>
                <rp></rp>
              </ruby>
            </router-link>
          </span> </span>
          </div>


        </div>
        <div class="collapse navbar-collapse" id="example-navbar-collapse">


          <!--    这是导航栏元素-->
          <!--		<ul class="nav navbar-nav">-->
          <!--			<li class="active"><a href="#">iOS</a></li>-->
          <!--			<li><a href="#">SVN</a></li>-->
          <!--			<li class="dropdown">-->
          <!--				<a href="#" class="dropdown-toggle" data-toggle="dropdown">-->
          <!--					Java <b class="caret"></b>-->
          <!--				</a>-->
          <!--				<ul class="dropdown-menu">-->
          <!--					<li><a href="#">jmeter</a></li>-->
          <!--					<li><a href="#">EJB</a></li>-->
          <!--					<li><a href="#">Jasper Report</a></li>-->
          <!--					<li class="divider"></li>-->
          <!--					<li><a href="#">分离的链接</a></li>-->
          <!--					<li class="divider"></li>-->
          <!--					<li><a href="#">另一个分离的链接</a></li>-->
          <!--				</ul>-->
          <!--			</li>-->
          <!--		</ul>-->

          <div class="header-user-avatar">

            <div class="register" v-show="!token">
              <router-link to="/login">
                <button class="signin">登录</button>
              </router-link>
              <!--                &nbsp;&nbsp;|&nbsp;&nbsp;-->
              <a target="_blank" href="#">
                <router-link to="/register">
                  <!--                    <button class="signup">注册</button>-->
                </router-link>

              </a>
            </div>

            <div class="nav-item dropdown" v-show="token">

              <a style="text-decoration:none;" class="nav-link dropdown-toggle" href="javascript:void(0)" data-toggle="dropdown"
                 aria-haspopup="true" aria-expanded="false">
                <img id='img_avatar' :src="avatar" alt="user"
                     class="rounded-circle"
                     width="40">
                <span class="ml-2 d-none d-lg-inline-block"><span>你好鸭！,</span> <span
                  class="text-dark">{{ username }}</span> <i data-feather="chevron-down"
                                                             class="svg-icon"></i></span>
              </a>
              <div class="dropdown-menu dropdown-menu-right user-dd animated flipInY">
                <!--            <a class="dropdown-item" href="javascript:void(0)"><i data-feather="user"-->
                <!--                                                                  class="svg-icon mr-2 ml-1"></i>-->
                <!--                个人中心 开发中....</a>-->
                <!--            <a class="dropdown-item" href="javascript:void(0)"><i data-feather="credit-card"-->
                <!--                                                                  class="svg-icon mr-2 ml-1"></i>-->
                <!--                我的消息 开发中....</a>-->
                <!--            <a class="dropdown-item" href="javascript:void(0)"><i data-feather="mail"-->
                <!--                                                                  class="svg-icon mr-2 ml-1"></i>-->
                <!--                我的邮箱 开发中....</a>-->
                <div class="dropdown-divider"></div>
                <router-link to='userconfig' class="dropdown-item"><i data-feather="settings"
                                                                      class="svg-icon mr-2 ml-1"></i>
                  账户设置
                </router-link>
                <div class="dropdown-divider"></div>
                <a class="dropdown-item" href="#" @click="loginout"><i data-feather="power"
                                                                         class="svg-icon mr-2 ml-1"></i>
                  注销</a>
                <div class="dropdown-divider"></div>
                <!--            <div class="pl-4 p-3"><a href="javascript:void(0)" class="btn btn-sm btn-info">查看资料 开发中....</a>-->
                <!--            </div>-->
              </div>
            </div>
            <div v-show="false">
              <a href="/">
                <img class="faa-shake animated-hover"
                     src="https://cdn.jsdelivr.net/gh/moezx/cdn@3.1.9/img/Sakura/images/none.png"
                     width="30" height="30"> </a>
              <div class="header-user-menu">
                <div class="herder-user-name no-logged">Whether to <a href="https://2heng.xin/login/" target="_blank"
                                                                      style="color:#333;font-weight:bold;text-decoration:none">log
                  in</a> now?
                </div>
              </div>
            </div>

          </div>
        </div>
      </div>
    </nav>


  </div>
</template>


<script>
export default {
  name: 'Header',
  data() {
    return {

      token: null,
      username: '',
      avatar:this.$settings.Host+'/static/avatar/touxiang.png',
            screenHeight: '', // 浏览器窗口高度

      msg: 'Welcome to Your Vue.js App',
      // c_top:"cd-top faa-float animated",
      s_top: 'top: ' + (document.documentElement.clientHeight - 900).toString() + 'px',
      c_top: 'cd-top faa-float animated cd-is-visible',
      scrollTop: '',
      sliderStyle: {

        width: '0%',
        background: "orange",
      },
      class_header: 'navbar navbar-default site-header no-select is-homepage gizle yya', //
    }
  },
  created() {

    this.token = sessionStorage.token || localStorage.token;
    this.username = sessionStorage.username || localStorage.username;
    // this.$settings.avatar = this.$settings.Host+ '/static/' + (sessionStorage.avatar || localStorage.avatar);

          if (sessionStorage.avatar || localStorage.avatar){
            this.avatar = sessionStorage.avatar || localStorage.avatar
          }
    console.log(!this.token)
    if (!this.token){
      this.$router.push('/login');
    }

  },
  mounted() {

    window.addEventListener('scroll', this.event_qwq, true); // 监听滚动条高度
    window.addEventListener('resize', this.event_qwq, true); // 监听滚动条高度


    // 向页面添加股东事件


  },
  methods: {
    // 退出登录
    loginout() {
      localStorage.removeItem('token');//
      localStorage.removeItem('username');//
      localStorage.removeItem('id');//
      sessionStorage.removeItem('token');
      sessionStorage.removeItem('username');
      sessionStorage.removeItem('id');
      this.token = false
      this.$router.push('/login');

    },

    event_qwq() {


      var scrollTop = window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop;
      this.scrollTop = scrollTop


      var offsetTop = document.documentElement.scrollTop // 获取所需元素到文档顶部的距离，然后判断滚动条位置让该元素是否固定定位
      var v = document.body.scrollHeight

      this.sliderStyle.width = (scrollTop / v * 100).toString() + '%'
      let screenHeight = document.documentElement.clientHeight - 950;
      if (scrollTop !== 0) {
        this.s_top = 'top: ' + (screenHeight).toString() + 'px'
        // console.log(screenHeight)

        this.class_header = 'navbar navbar-default site-header no-select is-homepage gizle yya'
      } else {
        this.s_top = 'top: ' + (this.screenHeight - 900).toString() + 'px'

                 // 原隐藏样式
                // this.class_header = 'navbar navbar-default site-header no-select is-homepage gizle sabit'
        this.class_header = 'navbar navbar-default site-header no-select is-homepage gizle yya'
      }


    },
    screen_Height() {


      this.screenWidth = document.body.clientWidth;
      this.screenHeight = document.body.clientHeight;
      window.onresize = () => {
        return (() => {
          this.screenWidth = document.body.clientWidth;
          this.screenHeight = document.documentElement.clientHeight - 900;

          console.log(this.screenHeight)
          if (this.scrollTop !== 0) {


            this.s_top = 'top: ' + (this.screenHeight).toString() + 'px'
          } else {
            this.s_top = 'top: ' + (this.screenHeight - 900).toString() + 'px'
            console.log('top: ' + (this.screenHeight - 900).toString() + 'px')
          }
        })();
      };

    },

    //滚动事件
    handleScroll() {
      window.addEventListener()
      var scrollTop = window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop;
      this.scrollTop = scrollTop


      var offsetTop = document.documentElement.scrollTop // 获取所需元素到文档顶部的距离，然后判断滚动条位置让该元素是否固定定位
      var v = document.body.scrollHeight

      this.sliderStyle.width = (scrollTop / v * 100).toString() + '%'

      if (scrollTop !== 0) {

        this.class_header = 'site-header no-select is-homepage gizle yya'
      } else {

        this.class_header = 'site-header no-select is-homepage gizle sabit'
      }
    },
  },

  destroyed() { //离开这个界面之后，删除滚动事件，不然容易除bug
    window.removeEventListener('scroll', this.handleScroll)
  },


}

function scrollBar() {
  if (document.body.clientWidth > 860) {
    $(window).scroll(function () {
      var s = $(window).scrollTop(),
        a = $(document).height(),
        b = $(window).height(),
        result = parseInt(s / (a - b) * 100),
        cached = $("#bar");
      cached.css("width", result + "%");
      if (false) {
        if (result >= 0 && result <= 19)
          cached.css("background", "#cccccc");
        if (result >= 20 && result <= 39)
          cached.css("background", "#50bcb6");
        if (result >= 40 && result <= 59)
          cached.css("background", "#85c440");
        if (result >= 60 && result <= 79)
          cached.css("background", "#f2b63c");
        if (result >= 80 && result <= 99)
          cached.css("background", "#FF0000");
        if (result == 100)
          cached.css("background", "#5aaadb");
      } else {
        cached.css("background", "orange");
      }
      $(".toc-container").css("height", $(".site-content").outerHeight());
      $(".skin-menu").removeClass('show');
    });
  }
}


</script>


<style scoped>


@import "../../../static/font/fonts.css"; /*下拉小人*/
.navbar-nav > li > a {
  padding-top: 30px;
  padding-bottom: 0;
  height: 75px;
}

.register .signin, .register .signup {
  font-size: 14px;
  border: none;
  background-color: rgba(109, 255, 198, 0);
  color: #5e5e5e;
  white-space: nowrap;
}

.signup :hover {
  color: red;
}

.nav {
  border: 0;
}


.navbar-default .navbar-toggle {

  margin-top: 20px;


}

.navbar-toggle {

}

.navbar {

  min-height: 75px;
  border: 0;

}
/* logo 鼠标悬浮阴影 */
.top > nav:hover {
  position: fixed;
  left: 0;
  background: rgba(255, 255, 255, .95);
  box-shadow: 0 1px 40px -8px rgba(0, 0, 0, .2)
}

.navbar .navbar-default .site-header .no-select .is-homepage .gizle .sabit :hover {
  /*position: fixed;*/
  left: 0;
  background: rgba(255, 255, 255, .95);
  box-shadow: 0 1px 40px -8px rgba(0, 0, 0, .5)
  /*box-shadow: 0 0 40px -8px rgba(0, 0, 0, .5);*/
  /*min-height:75px ;*/
  /*border: 0;*/

}

.cd-top {
  position: fixed;
  right: 30px;
  top: -900px;
  z-index: 99;
  width: 70px;
  height: 900px;
  background: url(/static/img/scroll.png) no-repeat center;
  /*background-size: cover;*/
  /*-webkit-transition: all .5s ease-in-out;*/
  transition: all .5s ease-in-out;
  cursor: url(https://cdn.jsdelivr.net/gh/moezx/cdn@3.1.9/img/Sakura/cursor/No_Disponible.cur), auto;
  opacity: 1
}

.cd-top.cd-is-visible {

  opacity: 1;

  top: -400px;
}

/* 登录头像 */
.searchbox, .site-top .lower, .header-user-avatar {
  animation: searchbox 1s
}

.herder-user-name {
  font-size: 12px;
  background: #fff;
  padding: 10px;
  border-radius: 4px 4px 0 0
}

.header-user-menu .user-menu-option {
  padding: 5px 0;
  background: #fff;
  border-radius: 0 0 4px 4px;
  width: 130px
}

.header-user-menu {
  position: absolute;
  width: 110px;
  right: -11px;
  /*text-align: left;*/
  background: 0 0;
  top: 44px;
  display: none;
  overflow: hidden;
  animation: header-user-menu .4s;
  box-shadow: 0 1px 40px -8px rgba(0, 0, 0, .2);
  border-radius: 5px;
  text-align: center
}

.header-user-menu a {
  display: block;
  padding: 6px 10px;
  margin: 2px 0;
  width: 110px;

  color: #333;
  font-size: 13px;
  text-align: center
}

.header-user-menu:before {
  content: "";
  position: fixed;
  top: 46px;
  right: 25px;
  margin-left: -10px;
  border-width: 10px;
  border-style: solid;
  border-color: transparent transparent #fff
}

@keyframes header-user-menu {
  0% {
    opacity: 0;
    transform: translateY(-20px)
  }
  100% {
    opacity: 1;
    transform: translateY(0)
  }
}

.header-user-avatar {
  position: relative;
  float: right;
  margin-left: 20px;
  margin-top: 22px
}

.header-user-avatar img {
  border-radius: 100%;
  cursor: pointer
}

.header-user-avatar:hover .header-user-menu {
  display: block
}

.no-logged {
  font-size: 13px;
  padding: 15px 10px;
  border-radius: 4px;
  border: 0
}

.no-logged a {
  display: initial;
  color: #69d2e7;
  font-size: 14px;
  padding: 0 5px;
  text-decoration: underline
}

#qq {
  height: 50px;
  font-family: 'Moe-Mashiro' !important;
}

.moe-mashiro {
  font-family: 'Moe-Mashiro', 'Merriweather Sans', Helvetica, Tahoma, Arial, 'PingFang SC', 'Hiragino Sans GB', 'Microsoft Yahei', 'WenQuanYi Micro Hei', sans-serif;
}

.site-header:hover {
  background-color: #fff;
}

.site-header {
  width: 100%;
  height: 75px;
  background: 0 0;
  -webkit-transition: all .4s ease;
  transition: all .4s ease;
  position: fixed;
  z-index: 9999;
  top: 0;
}

.logolink.moe-mashiro a {
  color: #464646;
  float: left;
  font-size: 25px;
  font-weight: 800;
  height: 56px;
  line-height: 56px;
  padding-left: 6px;
  padding-right: 15px;
  padding-top: 11px;
  text-decoration-line: none;
}

.logolink a:hover ruby rt {
  opacity: 1;
}

.logolink a:hover rt {
  color: orange;
}

.logolink ruby rt {
  font-size: 10px;
  transform: translateY(-15px);
  opacity: 0;
  transiton-property: opacity;
  transition-duration: .5s, .5s
}

.logolink ruby {
  ruby-position: under;
}


.shironeko {
  color: #656262;
}

.logolink .sakuraso {
  background-color: rgba(255, 255, 255, .5);
  border-radius: 5px;
  color: #656262;
  height: auto;
  line-height: 25px;
  margin-right: 0;
  padding-bottom: 0;
  padding-top: 1px;
  text-size-adjust: 100%;
  width: auto
}

/* 动态logo悬浮变色 */
/*.logolink a:hover .sakuraso {*/
/*  background-color: orange;*/
/*  color: #fff*/
/*}*/
/*.logolink a:hover .shironeko, .logolink a:hover rt {*/
/*  color: orange*/
/*}*/

.logolink a:hover .no {

  position: relative;
  animation: haha1 2s infinite;
  /*animation-direction:alternate;*/
  animation-timing-function: linear;
  animation-iteration-count: 1000;
  /*animation-name:haha1  ; !*flash为要使用的动画效果名，在这里不需要加animate前缀*!*/
  /*animation-duration: 1s; !*这里设定完成该动画的时间*!*/
  /*animation-direction: alternate;*/
  color: orange;

  /*-webkit-animation: spin 1.5s linear infinite;*/
  /*animation: spin 1.5s linear infinite*/
}

@-webkit-keyframes haha1 {
  from {
    transform: rotate(0)
  }
  to {
    transform: rotate(360deg)
  }
}


.logolink ruby rt {
  font-size: 10px;
  transform: translateY(-15px);
  opacity: 0;
  transiton-property: opacity;
  transition-duration: .5s, .5s;
}

* {
  box-sizing: border-box;
}

::-webkit-scrollbar {
  width: 6px;
  height: 6px;
  background-color: #eee
}

#mo-nav::-webkit-scrollbar {
  width: 0;
  opacity: 0
}

::-webkit-scrollbar-track {
  background-color: #eee
}

::-webkit-scrollbar-thumb {
  background-color: #69d2e7
}

.scrollbar {
  position: fixed;
  top: 0;
  height: 3px;
  background: #bebebe;
  transiton-property: width, background;
  transition-duration: 1s, 1s;
  z-index: 99999
}

.logolink.moe-mashiro a {
  color: #464646;
  float: left;
  font-size: 25px;
  font-weight: 800;
  height: 56px;
  line-height: 56px;
  padding-left: 6px;
  padding-right: 15px;
  padding-top: 11px;
  text-decoration-line: none;
}

.site-branding {

  float: left;
  position: relative;
  height: 75px;
  line-height: 75px;
  /*margin-left: 16px;*/

}

/* logo从左淡出*/
.site-branding {
  animation-name: fadeInLeft; /*flash为要使用的动画效果名，在这里不需要加animate前缀*/
  animation-duration: 3s; /*这里设定完成该动画的时间*/


}

.site-top {
  width: 100%;
  display: block;
  margin: 0 auto;
  padding: 0 20px;
}


.logolink ruby {
  /* ruby-position: under; */
  -webkit-ruby-position: after;
}

.logolink.moe-mashiro .no {
  display: inline-block;
  margin-left: 5px;

}

.logolink.moe-mashiro .sakuraso, .logolink.moe-mashiro .no {

  font-size: 25px;
  border-radius: 9px;
  padding-bottom: 2px;
  padding-top: 1px;
}

.logolink .sakuraso {
  background-color: rgba(255, 255, 255, .5);
}


/* header头阴影 */
.yya {
  position: fixed;
  left: 0;
  background: rgba(255, 255, 255, .95);
  box-shadow: 0 1px 40px -8px rgba(0, 0, 0, .2)
}

.dropdown-item {
  display: block;
  width: 100%;
  padding: 0.65rem 1rem;
  clear: both;
  color: #6c757d;
  text-align: inherit;
  background-color: transparent;
  border: 0;
}

</style>


<!--<style scoped>-->
<!--@import "../../../static/font/fonts.css";-->
<!--#qq {-->
<!--  height: 50px;-->
<!--  font-family: 'Moe-Mashiro'!important;-->
<!--}-->

<!--.moe-mashiro {-->
<!--    font-family: 'Moe-Mashiro', 'Merriweather Sans', Helvetica, Tahoma, Arial, 'PingFang SC', 'Hiragino Sans GB', 'Microsoft Yahei', 'WenQuanYi Micro Hei', sans-serif;-->
<!--}-->

<!--.logolink.moe-mashiro .no {-->
<!--    display: inline-block;-->
<!--    margin-left: 5px;-->
<!--}-->
<!--.no :hover {-->
<!--    color: orange;-->
<!--}-->
<!--.logolink a:hover .no {-->
<!--    -webkit-animation: spin 1.5s linear infinite;-->
<!--    animation: spin 1.5s linear infinite;-->
<!--}-->


<!--/* header 部分的 */-->
<!--.site-header {-->
<!--    width: 100%;-->
<!--    height: 75px;-->
<!--    background: 0 0;-->
<!--    -webkit-transition: all .4s ease;-->
<!--    transition: all .4s ease;-->
<!--    position: fixed;-->
<!--    z-index: 9999;-->
<!--    top: 0-->
<!--}-->

<!--.site-header.is-homepage .lower-cantiner {-->
<!--    display: none-->
<!--}-->

<!--.site-header.is-homepage.yya .lower-cantiner {-->
<!--    display: block-->
<!--}-->

<!--.site-header:hover.is-homepage .lower-cantiner {-->
<!--    display: block-->
<!--}-->

<!--.site-header:hover {-->
<!--    background-color: #fff-->
<!--}-->

<!--.clear:before, .clear:after, .entry-content:before, .entry-content:after, .comment-content:before, .comment-content:after, .site-header:before, .site-header:after, .site-content:before, .site-content:after, .site-footer:before, .site-footer:after {-->
<!--    content: "";-->
<!--    display: table;-->
<!--    table-layout: fixed-->
<!--}-->

<!--.clear:after, .entry-content:after, .comment-content:after, .site-header:after, .site-content:after, .site-footer:after {-->
<!--    clear: both-->
<!--}-->

<!--.site-header.iconsearch {-->
<!--    font-size: 18px;-->
<!--    font-size: 1.125rem;-->
<!--    position: relative;-->
<!--    z-index: 9998-->
<!--}-->

<!--.site-header.iconsearch:hover {-->
<!--    cursor: pointer;-->
<!--    color: #999-->
<!--}-->

<!--@media (max-width: 860px) {-->
<!--    .comments {-->
<!--        max-width: 100% !important-->
<!--    }-->

<!--    .top-feature, .top-feature-row {-->
<!--        display: none-->
<!--    }-->

<!--    .site-content {-->
<!--        padding: 0 4%-->
<!--    }-->

<!--    .feature img {-->
<!--        width: 52px;-->
<!--        height: 52px-->
<!--    }-->

<!--    .post-list h1.entry-title {-->
<!--        margin: 0 0 0 65px;-->
<!--        font-size: 16px;-->
<!--        line-height: 30px-->
<!--    }-->

<!--    .p-time {-->
<!--        position: relative;-->
<!--        margin: -15px 0 0 65px-->
<!--    }-->

<!--    .post-list p {-->
<!--        margin: 20px 0 0 65px;-->
<!--        font-size: 14px;-->
<!--        height: 30px;-->
<!--        overflow: hidden-->
<!--    }-->

<!--    .s-content {-->
<!--        padding: 10px 15px;-->
<!--        margin-right: 65px-->
<!--    }-->

<!--    .s-content p {-->
<!--        margin-left: 0;-->
<!--        margin-top: 0;-->
<!--        height: 30px;-->
<!--        overflow: hidden-->
<!--    }-->

<!--    .postava img {-->
<!--        width: 52px;-->
<!--        height: 52px-->
<!--    }-->

<!--    .overlay {-->
<!--        display: none-->
<!--    }-->

<!--    .info-meta {-->
<!--        display: none-->
<!--    }-->

<!--    .post-more {-->
<!--        display: none-->
<!--    }-->

<!--    h1.entry-title {-->
<!--        font-size: 18px-->
<!--    }-->

<!--    .entry-content p {-->
<!--        font-size: 14px-->
<!--    }-->

<!--    .post-footer, .post-share, .post-like {-->
<!--        display: none-->
<!--    }-->

<!--    .post-tags {-->
<!--        text-align: center;-->
<!--        float: none;-->
<!--        font-size: 12px-->
<!--    }-->

<!--    .author-profile {-->
<!--        display: none-->
<!--    }-->

<!--    .site-footer {-->
<!--        padding: 30px-->
<!--    }-->

<!--    .lower {-->
<!--        display: none !important-->
<!--    }-->

<!--    .m-nav {-->
<!--        display: block-->
<!--    }-->

<!--    .site-header {-->
<!--        display: none-->
<!--    }-->

<!--    .site-branding {-->
<!--        float: right;-->
<!--        height: 50px;-->
<!--        line-height: 43px;-->
<!--        margin-right: -6px-->
<!--    }-->

<!--    .site-title img {-->
<!--        height: 40px;-->
<!--        line-height: 40px;-->
<!--        margin: 0;-->
<!--        vertical-align: middle-->
<!--    }-->

<!--    .site-title {-->
<!--        font-size: 20px;-->
<!--        margin-right: 10px-->
<!--    }-->

<!--    .links ul li {-->
<!--        width: 48.6%-->
<!--    }-->

<!--    .links ul li:before {-->
<!--        display: none-->
<!--    }-->

<!--    .links ul li:hover .sitename {-->
<!--        color: orange-->
<!--    }-->

<!--    .links ul li:hover .linkdes {-->
<!--        color: #949494;-->
<!--        border-top: 1px dashed #ddd-->
<!--    }-->

<!--    .author-box {-->
<!--        display: none-->
<!--    }-->

<!--    #archives-temp {-->
<!--        padding: 0 20px-->
<!--    }-->
<!--}-->

<!--.no-select {-->
<!--    -webkit-touch-callout: none;-->
<!--    -webkit-user-select: none;-->
<!--    -khtml-user-select: none;-->
<!--    -moz-user-select: none;-->
<!--    -ms-user-select: none;-->
<!--    user-select: none-->
<!--}-->

<!--.site-header.is-homepage .lower-cantiner {-->
<!--    display: none-->
<!--}-->

<!--.site-header.is-homepage.yya .lower-cantiner {-->
<!--    display: block-->
<!--}-->

<!--.site-header:hover.is-homepage .lower-cantiner {-->
<!--    display: block-->
<!--}-->

<!--.gizle {-->
<!--    top: -100px;-->
<!--    top: 0;-->
<!--    z-index: 9999-->
<!--}-->
<!--.sabit {-->
<!--    top: 0;-->
<!--    z-index: 9999-->
<!--}-->

<!--.searchbox, .site-top .lower, .header-user-avatar {-->
<!--    animation: searchbox 1s-->
<!--}-->

<!--.site-top {-->
<!--    width: 100%;-->
<!--    display: block;-->
<!--    margin: 0 auto;-->
<!--    padding: 0 20px-->
<!--}-->

<!--.site-top .lower-cantiner {-->
<!--    position: absolute;-->
<!--    left: 50%;-->
<!--    min-width: 758.4px;-->
<!--    pointer-events: none-->
<!--}-->

<!--.site-top .lower {-->
<!--    display: inline-block;-->
<!--    margin: 15px 0 0 10px;-->
<!--    font-size: 16px;-->
<!--    position: relative;-->
<!--    left: -50%;-->
<!--    pointer-events: auto !important-->
<!--}-->

<!--@media (max-width: 1200px) {-->
<!--    .site-top .lower {-->
<!--        left: 15px-->
<!--    }-->

<!--    .site-top .lower-cantiner {-->
<!--        left: 0-->
<!--    }-->

<!--    .site-top .lower nav.hide {-->
<!--        display: none !important-->
<!--    }-->

<!--    #show-nav.mobile-fit {-->
<!--        opacity: 1;-->
<!--        pointer-events: auto-->
<!--    }-->
<!--}-->

<!--@media (max-width: 860px) {-->
<!--    .site-top .lower nav ul li .animated-hover i {-->
<!--        display: inline-->
<!--    }-->
<!--}-->

<!--.site-top .lower nav {-->
<!--    position: relative;-->
<!--    float: right;-->
<!--    display: none;-->
<!--    animation: searchbox .2s-->
<!--}-->

<!--.site-top .lower nav.navbar {-->
<!--    display: block-->
<!--}-->

<!--.site-top ul {-->
<!--    margin: 0;-->
<!--    padding: 0;-->
<!--    list-style: none;-->
<!--    display: inline-block-->
<!--}-->

<!--.site-top ul li {-->
<!--    float: left;-->
<!--    margin: 0 13px;-->
<!--    position: relative;-->
<!--    -webkit-transition: all 1s ease-->
<!--}-->

<!--.site-top ul li a {-->
<!--    padding: 10px 0;-->
<!--    display: inline-block;-->
<!--    color: #666-->
<!--}-->

<!--.site-top ul li a:hover {-->
<!--    color: orange-->
<!--}-->

<!--.site-top ul li a:after {-->
<!--    content: "";-->
<!--    display: block;-->
<!--    position: absolute;-->
<!--    bottom: -16px;-->
<!--    height: 6px;-->
<!--    background-color: #fe9600;-->
<!--    width: 100%;-->
<!--    max-width: 0;-->
<!--    transition: max-width .25s ease-in-out-->
<!--}-->

<!--.site-top ul li ul li a:after {-->
<!--    content: "";-->
<!--    display: none;-->
<!--    position: absolute;-->
<!--    bottom: -21px;-->
<!--    height: 6px;-->
<!--    background-color: #fe9600;-->
<!--    width: 100%;-->
<!--    max-width: 0;-->
<!--    transition: max-width .25s ease-in-out-->
<!--}-->

<!--.site-top ul li a:hover:after {-->
<!--    max-width: 100%-->
<!--}-->

<!--.site-top .menu-item-has-children li a {-->
<!--    font-size: 14px;-->
<!--    padding: 8px 18px;-->
<!--    text-transform: none;-->
<!--    color: #545454-->
<!--}-->

<!--.site-branding {-->
<!--    animation: sitetop 1s-->
<!--}-->

<!--.site-branding {-->
<!--    float: left;-->
<!--    position: relative;-->
<!--    height: 75px;-->
<!--    line-height: 75px;-->
<!--    margin-left: -6px-->
<!--}-->

<!--@media (max-width: 860px) {-->
<!--    .comments {-->
<!--        max-width: 100% !important-->
<!--    }-->

<!--    .top-feature, .top-feature-row {-->
<!--        display: none-->
<!--    }-->

<!--    .site-content {-->
<!--        padding: 0 4%-->
<!--    }-->

<!--    .feature img {-->
<!--        width: 52px;-->
<!--        height: 52px-->
<!--    }-->

<!--    .post-list h1.entry-title {-->
<!--        margin: 0 0 0 65px;-->
<!--        font-size: 16px;-->
<!--        line-height: 30px-->
<!--    }-->

<!--    .p-time {-->
<!--        position: relative;-->
<!--        margin: -15px 0 0 65px-->
<!--    }-->

<!--    .post-list p {-->
<!--        margin: 20px 0 0 65px;-->
<!--        font-size: 14px;-->
<!--        height: 30px;-->
<!--        overflow: hidden-->
<!--    }-->

<!--    .s-content {-->
<!--        padding: 10px 15px;-->
<!--        margin-right: 65px-->
<!--    }-->

<!--    .s-content p {-->
<!--        margin-left: 0;-->
<!--        margin-top: 0;-->
<!--        height: 30px;-->
<!--        overflow: hidden-->
<!--    }-->

<!--    .postava img {-->
<!--        width: 52px;-->
<!--        height: 52px-->
<!--    }-->

<!--    .overlay {-->
<!--        display: none-->
<!--    }-->

<!--    .info-meta {-->
<!--        display: none-->
<!--    }-->

<!--    .post-more {-->
<!--        display: none-->
<!--    }-->

<!--    h1.entry-title {-->
<!--        font-size: 18px-->
<!--    }-->

<!--    .entry-content p {-->
<!--        font-size: 14px-->
<!--    }-->

<!--    .post-footer, .post-share, .post-like {-->
<!--        display: none-->
<!--    }-->

<!--    .post-tags {-->
<!--        text-align: center;-->
<!--        float: none;-->
<!--        font-size: 12px-->
<!--    }-->

<!--    .author-profile {-->
<!--        display: none-->
<!--    }-->

<!--    .site-footer {-->
<!--        padding: 30px-->
<!--    }-->

<!--    .lower {-->
<!--        display: none !important-->
<!--    }-->

<!--    .m-nav {-->
<!--        display: block-->
<!--    }-->

<!--    .site-header {-->
<!--        display: none-->
<!--    }-->

<!--    .site-branding {-->
<!--        float: right;-->
<!--        height: 50px;-->
<!--        line-height: 43px;-->
<!--        margin-right: -6px-->
<!--    }-->

<!--    .site-title img {-->
<!--        height: 40px;-->
<!--        line-height: 40px;-->
<!--        margin: 0;-->
<!--        vertical-align: middle-->
<!--    }-->

<!--    .site-title {-->
<!--        font-size: 20px;-->
<!--        margin-right: 10px-->
<!--    }-->

<!--    .links ul li {-->
<!--        width: 48.6%-->
<!--    }-->

<!--    .links ul li:before {-->
<!--        display: none-->
<!--    }-->

<!--    .links ul li:hover .sitename {-->
<!--        color: orange-->
<!--    }-->

<!--    .links ul li:hover .linkdes {-->
<!--        color: #949494;-->
<!--        border-top: 1px dashed #ddd-->
<!--    }-->

<!--    .author-box {-->
<!--        display: none-->
<!--    }-->

<!--    #archives-temp {-->
<!--        padding: 0 20px-->
<!--    }-->
<!--}-->


<!--.site-title {-->
<!--    margin: 0-->
<!--}-->

<!--.site-title a {-->
<!--    color: #464646;-->
<!--    font-weight: 400-->
<!--}-->

<!--.site-title a:hover {-->
<!--    color: orange-->
<!--}-->

<!--.site-title img {-->
<!--    height: 40px;-->
<!--    margin-top: 17px;-->
<!--    opacity: .75;-->
<!--    -webkit-transition: color .2s ease-out, border .2s ease-out, opacity .2s ease-out;-->
<!--    -moz-transition: color .2s ease-out, border .2s ease-out, opacity .2s ease-out;-->
<!--    transition: color .2s ease-out, border .2s ease-out, opacity .2s ease-out-->
<!--}-->

<!--.site-title img:hover {-->
<!--    opacity: 1-->
<!--}-->

<!--@media (max-width: 630px) {-->
<!--    .links ul li {-->
<!--        width: 100% !important-->
<!--    }-->

<!--    .we-content li {-->
<!--        width: 100%;-->
<!--        margin-top: 0-->
<!--    }-->

<!--    .we-icon {-->
<!--        top: 50px !important-->
<!--    }-->

<!--    .wtitle {-->
<!--        top: 130px !important-->
<!--    }-->

<!--    .sub-text {-->
<!--        top: 160px !important-->
<!--    }-->

<!--    .admin-login, .wesite-des {-->
<!--        display: none-->
<!--    }-->

<!--    .wesite-title {-->
<!--        float: none;-->
<!--        text-align: center;-->
<!--        border-right: none;-->
<!--        padding-right: 0-->
<!--    }-->
<!--}-->

<!--@media (max-width: 860px) {-->
<!--    .comments {-->
<!--        max-width: 100% !important-->
<!--    }-->

<!--    .top-feature, .top-feature-row {-->
<!--        display: none-->
<!--    }-->

<!--    .site-content {-->
<!--        padding: 0 4%-->
<!--    }-->

<!--    .feature img {-->
<!--        width: 52px;-->
<!--        height: 52px-->
<!--    }-->

<!--    .post-list h1.entry-title {-->
<!--        margin: 0 0 0 65px;-->
<!--        font-size: 16px;-->
<!--        line-height: 30px-->
<!--    }-->

<!--    .p-time {-->
<!--        position: relative;-->
<!--        margin: -15px 0 0 65px-->
<!--    }-->

<!--    .post-list p {-->
<!--        margin: 20px 0 0 65px;-->
<!--        font-size: 14px;-->
<!--        height: 30px;-->
<!--        overflow: hidden-->
<!--    }-->

<!--    .s-content {-->
<!--        padding: 10px 15px;-->
<!--        margin-right: 65px-->
<!--    }-->

<!--    .s-content p {-->
<!--        margin-left: 0;-->
<!--        margin-top: 0;-->
<!--        height: 30px;-->
<!--        overflow: hidden-->
<!--    }-->

<!--    .postava img {-->
<!--        width: 52px;-->
<!--        height: 52px-->
<!--    }-->

<!--    .overlay {-->
<!--        display: none-->
<!--    }-->

<!--    .info-meta {-->
<!--        display: none-->
<!--    }-->

<!--    .post-more {-->
<!--        display: none-->
<!--    }-->

<!--    h1.entry-title {-->
<!--        font-size: 18px-->
<!--    }-->

<!--    .entry-content p {-->
<!--        font-size: 14px-->
<!--    }-->

<!--    .post-footer, .post-share, .post-like {-->
<!--        display: none-->
<!--    }-->

<!--    .post-tags {-->
<!--        text-align: center;-->
<!--        float: none;-->
<!--        font-size: 12px-->
<!--    }-->

<!--    .author-profile {-->
<!--        display: none-->
<!--    }-->

<!--    .site-footer {-->
<!--        padding: 30px-->
<!--    }-->

<!--    .lower {-->
<!--        display: none !important-->
<!--    }-->

<!--    .m-nav {-->
<!--        display: block-->
<!--    }-->

<!--    .site-header {-->
<!--        display: none-->
<!--    }-->

<!--    .site-branding {-->
<!--        float: right;-->
<!--        height: 50px;-->
<!--        line-height: 43px;-->
<!--        margin-right: -6px-->
<!--    }-->

<!--    .site-title img {-->
<!--        height: 40px;-->
<!--        line-height: 40px;-->
<!--        margin: 0;-->
<!--        vertical-align: middle-->
<!--    }-->

<!--    .site-title {-->
<!--        font-size: 20px;-->
<!--        margin-right: 10px-->
<!--    }-->

<!--    .links ul li {-->
<!--        width: 48.6%-->
<!--    }-->

<!--    .links ul li:before {-->
<!--        display: none-->
<!--    }-->

<!--    .links ul li:hover .sitename {-->
<!--        color: orange-->
<!--    }-->

<!--    .links ul li:hover .linkdes {-->
<!--        color: #949494;-->
<!--        border-top: 1px dashed #ddd-->
<!--    }-->

<!--    .author-box {-->
<!--        display: none-->
<!--    }-->

<!--    #archives-temp {-->
<!--        padding: 0 20px-->
<!--    }-->
<!--}-->


<!--.logolink a {-->
<!--    color: #464646;-->
<!--    float: left;-->
<!--    font-size: 20px;-->
<!--    font-weight: 800;-->
<!--    height: 56px;-->
<!--    line-height: 56px;-->
<!--    padding-left: 35px;-->
<!--    padding-right: 15px;-->
<!--    padding-top: 11px;-->
<!--    text-decoration-line: none-->
<!--}-->

<!--.logolink .sakuraso {-->
<!--    background-color: rgba(255, 255, 255, .5);-->
<!--    border-radius: 5px;-->
<!--    color: #464646;-->
<!--    height: auto;-->
<!--    line-height: 25px;-->
<!--    margin-right: 0;-->
<!--    padding-bottom: 0;-->
<!--    padding-top: 1px;-->
<!--    text-size-adjust: 100%;-->
<!--    width: auto-->
<!--}-->

<!--.logolink a:hover .sakuraso {-->
<!--    background-color: orange;-->
<!--    color: #fff-->
<!--}-->

<!--.logolink a:hover .shironeko, .logolink a:hover rt {-->
<!--    color: orange-->
<!--}-->

<!--.logolink a:hover .no {-->
<!--    -webkit-animation: spin 1.5s linear infinite;-->
<!--    animation: spin 1.5s linear infinite-->
<!--}-->

<!--.logolink ruby {-->
<!--    ruby-position: under;-->
<!--    -webkit-ruby-position: after-->
<!--}-->

<!--.logolink ruby rt {-->
<!--    font-size: 10px;-->
<!--    transform: translateY(-15px);-->
<!--    opacity: 0;-->
<!--    transiton-property: opacity;-->
<!--    transition-duration: .5s, .5s-->
<!--}-->

<!--.logolink a:hover ruby rt {-->
<!--    opacity: 1-->
<!--}-->

<!--.logolink.moe-mashiro .sakuraso, .logolink.moe-mashiro .no {-->
<!--    font-size: 25px;-->
<!--    border-radius: 9px;-->
<!--    padding-bottom: 2px;-->
<!--    padding-top: 5px-->
<!--}-->

<!--.logolink.moe-mashiro .no {-->
<!--    display: inline-block;-->
<!--    margin-left: 5px-->
<!--}-->

<!--.logolink a:hover .no {-->
<!--    -webkit-animation: spin 1.5s linear infinite;-->
<!--    animation: spin 1.5s linear infinite-->
<!--}-->

<!--.chinese-font {-->
<!--    font-family: 'Merriweather Sans', Helvetica, Tahoma, Arial, 'PingFang SC', 'Hiragino Sans GB', 'Microsoft Yahei', 'WenQuanYi Micro Hei', sans-serif-->
<!--}-->


<!--.lower li ul {-->
<!--    display: none;-->
<!--    opacity: 1;-->
<!--    position: absolute;-->
<!--    background: #fff;-->
<!--    padding: 10px;-->
<!--    top: 46px;-->
<!--    right: -13px;-->
<!--    width: 80px;-->
<!--    text-align: center;-->
<!--    z-index: 9999;-->
<!--    border-radius: 5px;-->
<!--    box-shadow: 0 1px 40px -8px rgba(0, 0, 0, .5);-->
<!--    -webkit-animation: fadeInUp .3s .1s ease both;-->
<!--    -moz-animation: fadeInUp .3s .1s ease both-->
<!--}-->

<!--.lower li ul:before {-->
<!--    content: "";-->
<!--    position: absolute;-->
<!--    top: -20px;-->
<!--    left: 50%;-->
<!--    margin-left: -10px;-->
<!--    border-width: 10px;-->
<!--    border-style: solid;-->
<!--    border-color: transparent transparent #fff-->
<!--}-->

<!--#show-nav.mobile-fit {-->
<!--    position: fixed !important;-->
<!--    right: 120px;-->
<!--    opacity: 0;-->
<!--    pointer-events: none-->
<!--}-->

<!--#show-nav {-->
<!--    position: relative;-->
<!--    float: right;-->
<!--    margin-left: 20px;-->
<!--    display: block;-->
<!--    width: 30px;-->
<!--    height: 33px;-->
<!--    margin-top: 4.5px;-->
<!--    cursor: pointer;-->
<!--    z-index: 999-->
<!--}-->

<!--#show-nav .line {-->
<!--    position: absolute;-->
<!--    top: 7px;-->
<!--    left: 50%;-->
<!--    width: 28px;-->
<!--    margin-left: -15px;-->
<!--    height: 2px;-->
<!--    background: #666;-->
<!--    -webkit-transition: all .2s ease-->
<!--}-->

<!--#show-nav.showNav .line1 {-->
<!--    top: 16px-->
<!--}-->

<!--#show-nav.showNav .line3 {-->
<!--    top: 25px-->
<!--}-->

<!--#show-nav.hideNav .line1 {-->
<!--    top: 16px;-->
<!--    -webkit-transform: rotateZ(45deg)-->
<!--}-->

<!--#show-nav.hideNav .line2 {-->
<!--    opacity: 0-->
<!--}-->

<!--#show-nav.hideNav .line3 {-->
<!--    top: 16px;-->
<!--    -webkit-transform: rotateZ(-45deg)-->
<!--}-->

<!--@media (max-width: 860px) {-->
<!--    .site-top .lower nav ul li .animated-hover i {-->
<!--        display: inline-->
<!--    }-->
<!--}-->
<!--</style>-->

