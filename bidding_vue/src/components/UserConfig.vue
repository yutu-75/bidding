<template>

  <div style="height: 300px;background-color: #f9fbfd">
    <Header></Header>
    <div style="height: 80px;"></div>

    <div class="card_c" style="width:800px; margin-left: 20%;margin-top: 20px;">
      <el-card class="box-card">

        <el-row :gutter="20"   style="height: 90px;">
          <el-col :span="2">
            <div class="" style="width:200px;line-height: 50px;margin-left: 40px;font-weight: 600">头像</div>
          </el-col>

          <el-col :span="5" :offset="2">

            <div class="grid-content bg-purple" style="float: top">


              <el-avatar :size="80" :src="avatar" style="background-color:rgba(190, 190, 190,0.2);margin-left: 60px" ></el-avatar>
            </div>
          </el-col>
          <el-col :span="1">
            <el-upload
              class="upload-demo"
              accept="image/jpeg,image/gif,image/png,image/jpg"
              :action="this.$settings.Host+'/users/avatar/'"
              :on-success="response_avatar"
              :headers="myHeaders"
              :show-file-list="false"
              multiple

            >
              <button class="el-button" style="width: 150px;margin-top: 20px;margin-left: 85px">更换头像</button>

              <!--  <el-button size="small" type="primary">点击上传</el-button>-->

            </el-upload>


          </el-col>
        </el-row>


        <div style="width: 500px;margin: 30px;">

          <el-form :model="ruleForm" :rules="ruleForm" ref="ruleForm" label-position="left" label-width="150px"
                   class="demo-ruleForm">
            <el-form-item label="用户名" prop="username">
              <el-input v-model="ruleForm.username" @input="change_u"></el-input>
            </el-form-item>
            <el-form-item label="密码" prop="password">
              <el-input placeholder="请输入密码" v-model="ruleForm.password" show-password @input="change_u"></el-input>

            </el-form-item>

            <el-form-item
              prop="email"
              label="邮箱"
              :rules="[
      { required: true, message: '请输入邮箱地址', trigger: 'blur' },
      { type: 'email', message: '请输入正确的邮箱地址', trigger: ['blur', 'change'] }
    ]"
            >
              <el-input v-model="ruleForm.email" @input="change_u(rules)"></el-input>
            </el-form-item>

            <el-form-item
              label="获取几天内数据"
              prop="time_day"
              :rules="[
      { required: true, message: '获取几天内数据不能为空'},
      { type: 'number', message: '获取几天内数据必须为数字值'}
    ]"
            >
              <el-input type="age" v-model.number="ruleForm.time_day" autocomplete="off" @input="change_u"></el-input>
            </el-form-item>

            <el-form-item label="选择获取数据的网站" style="" >

              <el-select
                v-model="ruleForm.url_id"
                multiple
                filterable
                collapse-tags
                style="width: 100%;"
                @change="change_u"

                placeholder="请选择">
                <el-option

                  v-for="item in ruleForm.options_u"
                  @click.native="all_get(item.value)"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value">
                </el-option>
              </el-select>
            </el-form-item>

            <el-form-item label="是否开启邮件发送" prop="delivery">
              <el-switch v-model="ruleForm.state" @change="change_s"></el-switch>
            </el-form-item>


            <el-form-item label="关键字" prop="key_word">
              <el-input v-model="ruleForm.key_word" :disabled="true"></el-input>
            </el-form-item>


            <el-form-item>
              <el-button type="primary" :disabled="disabled" style="width: 200px;" @click="update_data('ruleForm')">
                立即创建
              </el-button>
              <!--              <el-button @click="resetForm('ruleForm')">重置</el-button>-->
            </el-form-item>
          </el-form>
        </div>

      </el-card>
    </div>
  </div>
</template>

<script>
import Header from '@/components/common/Header'
import {GetUser, UpdateUser} from "../api";



export default {
  name: "UserConfig",
  data() {
    return {

      avatar: this.$settings.Host+'/static/avatar/touxiang.png',
      myHeaders: {Authorization: 'jwt ' + (sessionStorage.token || localStorage.token)},

      disabled: true,    // 判断表单数据是否变动


      ruleForm1: {
        username: 'qwq',
        password: '123456',
        time_day: '1',
        email: 'xiao3952@foxmail.com',
        state: false,
        url_id: ['1', '2'],
        key_word: '第三方、满意度、调查、统计、调研、检查、研究、咨询、巡查、普查、考核、测评、评估、绩效、创建、摸底、核查、入户、监测、社会救助、城市管理',
        // 网站选择
        options_u: [
          {
            value: '0',
            label: '全部'
          }, {
            value: '1',
            label: '中国政府采购公告'
          }, {
            value: '2',
            label: '湖北省公共资源交易中心'
          }, {
            value: '3',
            label: '宜昌市公共资源交易中心'
          }, {
            value: '4',
            label: '武汉市政府采购信息发布系统'
          }, {
            value: '5',
            label: '孝感政务服务和大数据管理局'
          }, {
            value: '6',
            label: '黄冈市公共资源交易中心'
          }, {
            value: '7',
            label: '随州政府采购'
          }, {
            value: '8',
            label: '黄石市公共资源交易中心'
          }, {
            value: '9',
            label: '十堰市公共资源交易中心'
          }, {
            value: '10',
            label: '鄂州政府采购'
          }, {
            value: '11',
            label: '荆门市公共资源交易中心'
          }, {
            value: '12',
            label: '荆州市公共资源交易中心'
          }, {
            value: '13',
            label: '咸宁市公共资源交易中心'
          }, {
            value: '14',
            label: '恩施政府采购'
          }, {
            value: '15',
            label: '神农架林区政府采购'
          }],

      },
      ruleForm: {
        username: '',
        password: '',
        time_day: '',
        email: '',
        state: false,
        url_id: [],
        key_word: '第三方、满意度、调查、统计、调研、检查、研究、咨询、巡查、普查、考核、测评、评估、绩效、创建、摸底、核查、入户、监测、社会救助、城市管理',
        // 网站选择
        options_u: [
          {
            value: '0',
            label: '全部'
          }, {
            value: '1',
            label: '中国政府采购公告'
          }, {
            value: '2',
            label: '湖北省公共资源交易中心'
          }, {
            value: '3',
            label: '宜昌市公共资源交易中心'
          }, {
            value: '4',
            label: '武汉市政府采购信息发布系统'
          }, {
            value: '5',
            label: '孝感政务服务和大数据管理局'
          }, {
            value: '6',
            label: '黄冈市公共资源交易中心'
          }, {
            value: '7',
            label: '随州政府采购'
          }, {
            value: '8',
            label: '黄石市公共资源交易中心'
          }, {
            value: '9',
            label: '十堰市公共资源交易中心'
          }, {
            value: '10',
            label: '鄂州政府采购'
          }, {
            value: '11',
            label: '荆门市公共资源交易中心'
          }, {
            value: '12',
            label: '荆州市公共资源交易中心'
          }, {
            value: '13',
            label: '咸宁市公共资源交易中心'
          }, {
            value: '14',
            label: '恩施政府采购'
          }, {
            value: '15',
            label: '神农架林区政府采购'
          }],

      },
      rules: {
        username: [
          {required: true, message: '请输入需要更改的用户名', trigger: 'blur'},
          {min: 1, max: 10, message: '长度在 1 到 10 个字符', trigger: 'blur'}
        ],
        password: [
          {required: true, message: '请输入需要更改的密码', trigger: 'blur'},
          {min: 3, max: 16, message: '长度在 3 到 16 个字符', trigger: 'blur'}
        ],
        // url_id: [
        //   {required: true, message: '选择获取数据的网站', trigger: 'change'}
        // ],

      },


      size: '',
      uname: 'sss',
      password: 'qwer',
      email: 'xiao3952@foxmail.com',
      time_day: '1',
      url_id: ['1', '4', '3'],
      send_time: '2014',
      key_word: '第三方、满意度、调查、统计、调研、检查、研究、咨询、巡查、普查、考核、测评、评估、绩效、创建、摸底、核查、入户、监测、社会救助、城市管理',
      value2: '',
      state: 'true',

      currentPage4: 1,        // 页数
      p_number: 10,
      count_t: 0,             // 数据总数

      value_u: '0',
      show_s: false,
      // 日期选择
      pickerOptions: {
        shortcuts: [{
          text: '最近一天',
          onClick(picker) {
            const end = new Date();
            const start = new Date();
            start.setTime(start.getTime() - 3600 * 1000 * 24);
            picker.$emit('pick', [start, end]);
          }
        }, {
          text: '最近一个月',
          onClick(picker) {
            const end = new Date();
            const start = new Date();
            start.setTime(start.getTime() - 3600 * 1000 * 24 * 30);
            picker.$emit('pick', [start, end]);
          }
        }, {
          text: '最近三个月',
          onClick(picker) {
            const end = new Date();
            const start = new Date();
            start.setTime(start.getTime() - 3600 * 1000 * 24 * 90);
            picker.$emit('pick', [start, end]);
          }
        }, {
          text: '最近一年',
          onClick(picker) {
            const end = new Date();
            const start = new Date();
            start.setTime(start.getTime() - 3600 * 1000 * 24 * 365);
            picker.$emit('pick', [start, end]);
          }
        }]
      },
      value1: [new Date(2000, 10, 10, 10, 10), new Date(2000, 10, 11, 10, 10)],
      value_time: '',
      value_t: '',
      id_max: 0,       // 每个文件的id 最大值
      search: '',  // 表格搜素
      textarea2: '', // 添加的关键字符串
      word_v: '',      // 词汇库的选择
      word_options: '', //    词汇库名称
      all_state: false,

    }
  },
  created() {

        this.token = sessionStorage.token || localStorage.token;

    console.log(!this.token)
    if (!this.token){
      // this.$router.push('/login');
    }else {
      this.get_user()
    }


  },
  watch: {
    ruleForm(val) {//普通的watch监听
      console.log("a: ");
    },


  },
  methods: {
    // 头像上传成功钩子
    response_avatar(res, file) {
      this.avatar = this.$settings.Host + '/static/' + res.img_name
      localStorage.avatar = this.$settings.Host + '/static/' + res.img_name

      console.log(this.avatar)
                this.$message({
            message: '恭喜你，成功更换头像！ 如果没出现头像就刷新一下',
            type: 'success',
              offset: 100
          });
      console.log(this.avatar)

    },
    // 更换头像


    get_user() {
      let token_s1 = sessionStorage.token || localStorage.token
      GetUser({
        headers:{'Authorization':'jwt ' + token_s1
        }})
        .then((data) => {

          this.ruleForm.username = data.data.data.username;
          this.ruleForm.password = data.data.data.password;
          localStorage.avatar = this.$settings.Host + '/static' + data.data.data.avatar;
          if (data.data.data.avatar){
            this.avatar = this.$settings.Host + '/static' + data.data.data.avatar
          }

          this.ruleForm.email = data.data.data.email;
          this.ruleForm.state = data.data.data.state;
          this.ruleForm.url_id = eval(data.data.data.url_id);
          this.ruleForm.time_day = data.data.data.time_day;

          // 深拷贝数组
          this.ruleForm1 = JSON.parse(JSON.stringify(this.ruleForm));


        })
        .catch((err) => {
        this.$message({
          message: err.data,
          type: 'error',
          offset: 100
        });
        })
    },
    change_u(a) {
      console.log(a)

    this.disabled = !this.disabled;


      // this.disabled = Object.values(this.ruleForm).toString() === Object.values(this.ruleForm1).toString();

    },
    change_s() {

      this.disabled = !this.disabled;

      if (this.ruleForm.email.length < 2) {
        this.$message({
          message: '亲~ 要先填邮箱哟！',
          type: 'error',
          offset: 100
        });
        this.ruleForm.state = false;
      } else {
        // this.change_u()
      }


    },
    all_get(val) {

      // 数组删除指定元素的构造函数
      Array.prototype.remove = function (val) {
        var index = this.indexOf(val);
        if (index > -1) {
          this.splice(index, 1);
        }
      };
      if (val === '0') {
        if (this.all_state) {
          this.all_state = false;
          this.ruleForm.url_id = []
        } else {
          this.all_state = true;
          this.ruleForm.url_id = ['2', '4', '11', '9', '12', '15', '14', '13', '8', '6', '7', '5', '3', '1', '10', '0']
        }
      } else {
        if ('0' in this.ruleForm.url_id) {
          this.ruleForm.url_id.remove('0');
        }
      }

    },
    func_setting() {

      this.show_s = this.show_s === false;

    },


    update_data(formName) {
      this.$refs[formName].validate((valid) => {
          if (valid) {

                  let data_send = {
        username: this.ruleForm.username,
        password: this.ruleForm.password,
        state:this.ruleForm.state,
        url_id:this.ruleForm.url_id,
        time_day:this.ruleForm.time_day,
        email:this.ruleForm.email,
      }
      // axios请求在这里
let token_s1 = sessionStorage.token || localStorage.token
      UpdateUser(
          {data: data_send,headers:{'Authorization':'jwt ' + token_s1}}
      )
        .then((res) => {


          this.$message({
            message: '恭喜你，成功修改数据！',
            type: 'success',
              offset: 100
          });
          this.show_s = false;
          this.disabled = true;

        })
        .catch((err) => {
          console.log()
                  this.$message({
          message: err.data,
          type: 'error',
          offset: 100
        });
        })


          } else {
          this.$message({
          message: '请正确填写内容呢！',
          type: 'error',
          offset: 100
        });
            console.log('error submit!!');
            return false;
          }
        });





    },
    handleCurrentChange1(val) {
      alert(this.p_number)


      console.log(`当前页: ${val}`);
    },

    handleSizeChange1(val) {
      console.log(`每页 ${val} 条`);
      this.p_number = val;


    },
    // 时间转行
    dateFormat_m(row, column, cellValue) {

      let date = new Date(cellValue)
      let y = date.getFullYear()
      let m = date.getMonth() + 1
      m = m < 10 ? ('0' + m) : m
      let d = date.getDate()
      d = d < 10 ? ('0' + d) : d
      let h = date.getHours()
      h = h < 10 ? ('0' + h) : h
      let M = date.getMinutes()
      M = M < 10 ? ('0' + M) : M
      let s = date.getSeconds()
      s = s < 10 ? ('0' + s) : s
      // let dateTime = y + '-' + m + '-' + d + ' ' + h + ':' + M + ':' + s;
      let dateTime = y + '-' + m + '-' + d + ' ';

      return dateTime

    },


    // 字段显示过多 省略号
    stateFormat(row, column, cellValue) {
      if (!cellValue) return ''
      if (cellValue.length > 10) {       //最长固定显示10个字符
        return cellValue.slice(0, 10) + '...'
      }
      return cellValue
    },


    // 查询数据
    get_data() {

      axios.defaults.headers.post['X-CSRFToken'] = '{{ csrf_token }}'
      axios.post(BASE_URL + '/bidding/', {
        value_u: this.value_u,
        value_time: this.value_time,
        f_number: 1,
        p_number: this.p_number,
      })
        .then((res) => {
          this.tableData = res.data.data_list
          this.count_t = res.data.count_t
          console.log(res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },








    handleEdit(index, row) {
      console.log(index, row);
    },
    handleDelete(index, row) {
      console.log(index, row);
    },
    // 表格方法操作
    // 选中第几行的方法
    toggleSelection(rows) {
      if (rows) {
        rows.forEach(row => {
          this.$refs.multipleTable.toggleRowSelection(row);
        });
      } else {
        this.$refs.multipleTable.clearSelection();
      }
    },
    // 删除选中的方法
    toggleremove() {

      console.log(this.multipleSelection)
      this.table1Data.splice(1, 1);
      this.multipleSelection.sort().reverse();


      console.log(this.multipleSelection)
      let table_data = []
      console.log(this.multipleSelection)
      alert(this.multipleSelection)
      for (i in this.table1Data) {
        console.log(this.table1Data[i].id)


        console.log(this.table1Data.id + this.multipleSelection)
        if (this.multipleSelection.includes(this.table1Data[i].id)) {
          console.log(this.table1Data[i].id)

        } else {
          console.log(this.table1Data[i].id)
          table_data.push(this.table1Data[i])
        }

        console.log(this.multipleSelection, 1)
      }
      console.log(table_data)
      this.table1Data = table_data
      let word_str = []
      for (let i = 0; i < this.table1Data.length; i++) {

        word_str.push(this.table1Data[i]['name'])
      }
      this.data_word = {'word_str': JSON.stringify(word_str), 'word_v': this.word_v};

    },

    handleSelectionChange(val, index) {

      let val1 = []
      val.forEach((alert) => {
        console.log(alert)
        console.log(alert.id)
        val1.push(alert.id);

      })


      this.multipleSelection = val1;

      console.log(this.multipleSelection)
    },

    tableRowClassName(row) {
      //设置row对象的index
      row.row.index = row.rowIndex;
    },

    // 拆分字符串，添加到词汇列表里
    data_word_change() {
      console.log(this.word_v)
      alert(this.textarea2)
      let a = this.textarea2
      let v = a.split('、')
      let id_list = []
      let name_list = []
      for (let i = 0; i < this.table1Data.length; i++) {
        id_list.push(this.table1Data[i]['id'])
      }
      for (let i = 0; i < this.table1Data.length; i++) {
        name_list.push(this.table1Data[i]['name'])
      }
      max_id_list = id_list.sort().reverse()[0]


      for (let i = 0; i < v.length; i++) {

        if (name_list.includes(v[i]) || !(Boolean(v[i]))) {

        } else {
          name_list.push(v[i])
          this.table1Data.push({id: max_id_list + i + 1, name: v[i]})
        }

      }
      let word_str = []
      for (let i = 0; i < this.table1Data.length; i++) {

        word_str.push(this.table1Data[i]['name'])
      }
      this.data_word = {'word_str': JSON.stringify(word_str), 'word_v': this.word_v};


      alert(this.data_word['word_str'])
    },
    // 清空上传文件列表
    clearFiles() {
      this.$refs['my-upload'].clearFiles();
      this.tableData = [];
      this.id_max = 0
    },

    // 文件上传之前的钩子
    beforeAvatarUpload(file) {
      this.$refs['my-upload'].clearFiles();
      console.log(this.table1Data.length)
      let word_str = []
      for (let i = 0; i < this.table1Data.length; i++) {

        word_str.push(this.table1Data[i]['name'])
      }
      console.log(word_str)


      this.data_word = {'word_str': JSON.stringify(word_str), 'word_v': this.word_v}
      console.log(this.data_word)
      return true

    },

    // 上传完文件，反回的数据
    handleAvatarSuccess(res, file) {
      console.log(res)

      // 解决id重名问题
      for (let r = 0; r < res.length; r++) {
        this.id_max += 1
        res[r]['id'] = this.id_max
        for (let c = 0; c < res[r]['children'].length; c++) {
          this.id_max += 1
          res[r]['children'][c]['id'] = this.id_max
          console.log(res[r]['children'][c]['id'])
        }


      }
      let c = this.tableData.concat(res);  // 连接两个或多个数组。
      this.tableData = c
      console.log(this.tableData)

    },
    handleAvatarError(res, file) {
      this.$message.error(res);
    },


    handleCurrentChange(val) {
      alert(this.p_number)

      console.log(`当前页: ${val}`);
    }


  },
  components: {
    Header,


  }
}
</script>

<style scoped>
>>> .el-upload__input {
  display: none;
}



@media screen and (max-width: 800px) {
  .card_c{
  width:800px; margin-left: 0px;margin-top: 20px;
  }
}


.card {
  position: relative;
  display: flex;
  flex-direction: column;
  min-width: 0;
  word-wrap: break-word;
  background-color: #fff;
  background-clip: border-box;
  border: 0 solid #e9ecef;
  border-radius: 0.25rem;
}

#bar {
  margin: 30px;
}
</style>
