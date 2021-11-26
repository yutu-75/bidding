<template>
  <div class="home">

    <Header></Header>
    <Bidding></Bidding>



<!--    <div class="WordArt" style="height: 8000px;"></div>-->


  </div>

</template>

<script>
import Header from '@/components/common/Header'
import Bidding from '@/components/Bidding'


export default {
  name: "Home",
  data(){
    return {
      title:'Home组件'
    }

  },
  components:{
    Header,
    Bidding,

  }

}
</script>

<style scoped>
/* scoped  */
/*h1{*/
/*  color:red;*/
/*}*/

</style>
