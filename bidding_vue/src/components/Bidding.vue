<template>
  <div style="height: 300px;background-color: #f9fbfd; ">

    <div style="height: 80px;"></div>

    <!--
        <div class="row" style="margin: 30px;">
          <div class="col-xs-6 col-sm-3">
            <div class="grid-content bg-purple">
              <div class="grid-content bg-purple-dark">
                <h3 class="page-title text-truncate text-dark font-weight-medium mb-1" style="margin-left: 15px;"> 招标信息</h3>
                <div class="d-flex align-items-center">
                  <nav aria-label="breadcrumb" style="width: 150px;">
                    <ol class="breadcrumb m-0 p-0">
                      <li class="breadcrumb-item"><a href="/" class="text-muted">首页</a></li>

                      <li class="breadcrumb-item text-muted active"
                          aria-current="page">招标信息
                      </li>

                    </ol>
                  </nav>
                </div>
              </div>
            </div>
          </div>
        </div>

    -->
    <div class="row" style="margin: 30px;">

      <div class="">
        <el-card class="box-card">


          <el-row :gutter="10">
            <el-col :xs="24" :sm="12" :md="9" :lg="7" :xl="6">
              <div class="box-content">
                <span> 网站选择: </span>
                <el-select
                  v-model="value_u"
                  multiple
                  filterable
                  collapse-tags
                  style=" width: 300px;"
                  placeholder="请选择">
                  <el-option
                    v-for="item in options_u"
                    @click.native="all_get(item.value)"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value">
                  </el-option>
                </el-select>

              </div>
            </el-col>
            <el-col :xs="24" :sm="12" :md="9" :lg="7" :xl="6">
              <div class="box-content">
                <span> 时间选择:  </span>


                <el-date-picker
                  v-model="value_time"
                  type="datetimerange"
                  value-format="yyyy-MM-dd HH:mm:ss"
                  :picker-options="pickerOptions"
                  range-separator="至"
                  start-placeholder="开始日期"
                  style="width:300px"
                  end-placeholder="结束日期"
                  align="right">
                </el-date-picker>

              </div>
            </el-col>
            <el-col :xs="24" :sm="12" :md="9" :lg="7" :xl="6">
              <div class="box-content">
                <span> 关&nbsp 键 &nbsp字: </span>
                <el-input

                  :rows="2"
                  placeholder="请输入关键字以 ,，、 (英文逗号 中文逗号 中文顿号)符号隔开"
                  style=" width: 300px;"
                  v-model="key_word">
                </el-input>
              </div>
            </el-col>
            <el-col :xs="24" :sm="12" :md="9" :lg="7" :xl="6">
              <div class="box-content">
                <span> 客户名称:  </span>
                <el-input

                  :rows="2"
                  placeholder="请输入关键字客服名称,本查询采用模糊匹配！"
                  style=" width: 300px;"
                  v-model="customer_name">
                </el-input>
              </div>
            </el-col>
            <el-col :xs="24" :sm="12" :md="9" :lg="7" :xl="6">
              <div class="box-content">
                <span> 招标金额:</span>
                <div style="display:inline-table;">
                  <el-input-number v-model="min" style="width: 144px;" :controls=false
                                   controls-position="top"></el-input-number>
                  ~
                  <el-input-number v-model="max" style="width: 144px;" :controls=false
                                   controls-position="top"></el-input-number>
                </div>


              </div>

            </el-col>

            <el-col :xs="3" :sm="3" :md="3" :lg="3" :xl="3">

              <div class="box-content">
                <el-button @click="get_data">查询</el-button>
              </div>

            </el-col>

          </el-row>
          <p style="margin-top: 10px;color: #bebebe"> 由于招标信息内容里金额单位不统一,金额信息可能为中文数字等问题 <code>招标金额</code> 暂处于开发中...</p>

        </el-card>

        <hr>

        <div class="row">
          <div class="col-lg-12">

            <el-card class="box-card">

              <div class="card-body">


                <div id="bar" style="width: calc(100% - 55px); height:730px;">


                  <h4 class="card-title">招标信息表格
                    <div class="float-right" style="float:right;">
                      <el-button @click="exportExcel">导出</el-button>


                      <!--                      <a style="text-decoration:none;" class="el-button el-button&#45;&#45;default"-->
                      <!--                         :href="this.$settings.Host +'?value_u='+value_u+'&value_time='+value_time">-->
                      <!--                        导出</a>-->


                    </div>
                  </h4>
                  <h6 class="card-subtitle">要先选择条件才能显示呢！
                  </h6>


                  <template>
                    <el-table
                      id="aa"
                      :data="tableData"
                      height="650"
                      border
                      stripe
                      row-key='id'
                      default-expand-all:false
                      :tree-props="{children: 'children', hasChildren: 'hasChildren'}">
                      <el-table-column
                        type="index"
                        label="序号"
                        width="50">
                      </el-table-column>
                      <el-table-column

                        prop="collect_time"
                        :formatter="dateFormat_m"
                        label="采集日期"
                        width="100">
                      </el-table-column>
                      <el-table-column
                        sortable
                        prop="b_title"
                        label="招标标题"
                        width="300">
                      </el-table-column>
                      <el-table-column
                        prop="b_url"
                        label="网页链接地址"
                        :formatter="stateFormat"
                      >

                        <template slot-scope="scope">
                          <a :href="scope.row.b_url" target="_blank">
                            点击跳转....
                          </a>
                        </template>


                      </el-table-column>
                      <el-table-column
                        sortable
                        :formatter="dateFormat_m"
                        prop="b_release"
                        label="发标日期"
                        width="120"
                      >
                      </el-table-column>
                      <el-table-column
                        sortable
                        prop="b_money"
                        width="110"
                        label="招标金额">
                      </el-table-column>
                      <el-table-column
                        prop="customer_name"
                        width="100"
                        label="客户名称">
                      </el-table-column>
                      <el-table-column
                        prop="customer_phone"
                        width="160"
                        label="客户联系方式">
                      </el-table-column>
                      <el-table-column
                        prop="b_time"
                        width="100"
                        :formatter="dateFormat_m"
                        label="获取招标文件时间">
                      </el-table-column>

                      <el-table-column
                        prop="collect__web_name"
                        width="200"
                        label="来源网站名">
                      </el-table-column>
                    </el-table>
                  </template>


                  <div style="margin: 20px">

                    <el-pagination
                      background
                      @size-change="handleSizeChange1"
                      @current-change="handleCurrentChange1"
                      :current-page="currentPage4"
                      :page-sizes="[10, 100, 200, 300, 400]"
                      :page-size="10"
                      layout="total, sizes, prev, pager, next, jumper"
                      :total='count_t'>
                    </el-pagination>
                  </div>
                </div>


              </div>
            </el-card>
          </div>

          <div class="col-lg-4">
            <!--
                                    <div class="card">
                                        <div class="card-body">


                                            <h4 class="card-title">关键字配置项</h4>
                                            <h6 class="card-subtitle">可以自定义关键词汇!输入后点击其他位置即可显示.</h6>
                                            <el-input
                                                    type="textarea"
                                                    @blur="data_word_change"
                                                    :autosize="{ minRows: 2, maxRows: 4}"
                                                    placeholder="请输入内容,格式为:  奖励、补贴、补助、资助、税费、税收"
                                                    v-model="textarea2">
                                            </el-input>

                                            <div style="margin: 20px 0;"></div>
                                            <template>
                                                <el-table
                                                        max-height="250"
                                                        ref="multipleTable"

                                                        :data="table1Data.filter(data => !search || data.name.toLowerCase().includes(search.toLowerCase()))"
                                                        tooltip-effect="dark"
                                                        style="width: 100%"
                                                        @selection-change="handleSelectionChange"
                                                        {#                                            :row-class-name="tableRowClassName"#}


                                                >


                                                    <el-table-column
                                                            type="selection"
                                                            width="55">

                                                    </el-table-column>
                                                    <el-table-column
                                                            prop="name"
                                                            label="关键字"
                                                            width="120"

                                                    >

                                                    </el-table-column>
                                                    <el-table-column
                                                            fixed="right"
                                                            label="操作"

                                                            width="120">
                                                        <template slot="header" slot-scope="scope">
                                                            <el-input
                                                                    v-model="search"
                                                                    size="mini"
                                                                    placeholder="输入关键字搜索"/>
                                                        </template>
                                                        <template slot-scope="scope">
                                                            <el-button
                                                                    @click.native.prevent="deleteRow(scope.$index, table1Data)"
                                                                    type="text"
                                                                    size="small"

                                                            >
                                                                移除
                                                            </el-button>
                                                        </template>
                                                    </el-table-column>
                                                </el-table>
                                                <div style="margin-top: 20px">
                                                    <el-button @click="toggleremove()">
                                                        删除选中
                                                    </el-button>
                                                    <el-button @click="toggleSelection()">取消选择</el-button>
                                                </div>
                                            </template>


                                        </div>
                                    </div>
            -->
          </div>
        </div>
      </div>

    </div>


    <div class="page-wrapper">


    </div>


  </div>

</template>

<script>
// import {SelectData} from "../api";
import {SelectData} from '@/api/index';

export default {
  name: "Bidding",
  data() {
    return {
      min: '',
      max: '',
      customer_name: '',


      value_u: [],
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
        }
      ],
      value_time: '',
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
        },{
          text: '最近三天',
          onClick(picker) {
            const end = new Date();
            const start = new Date();
            start.setTime(start.getTime() - 3600 * 1000 * 24 *3);
            picker.$emit('pick', [start, end]);
          }
        },
          {
          text: '最近十天',
          onClick(picker) {
            const end = new Date();
            const start = new Date();
            start.setTime(start.getTime() - 3600 * 1000 * 24 *10);
            picker.$emit('pick', [start, end]);
          }
        },
          {
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
      key_word: '',
      a_url: '/bidding/download/',
      tableData: [],
      currentPage4: 1,        // 页数
      count_t: 0,             // 数据总数

      p_number: 10,

    }
  },
  methods: {
    // 时间转行
    dateFormat_m(row, column, cellValue) {

      let date = new Date(cellValue)
      let y = date.getFullYear()
      let m = date.getMonth() + 1
      m = m < 10 ? ('0' + m) : m
      let d = date.getDate()
      d = d < 10 ? ('0' + d) : d

      // let h = date.getHours()
      // h = h < 10 ? ('0' + h) : h
      // let M = date.getMinutes()
      // M = M < 10 ? ('0' + M) : M
      // let s = date.getSeconds()
      // s = s < 10 ? ('0' + s) : s
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
          this.value_u = []
        } else {
          this.all_state = true;
          this.value_u = ['2', '4', '11', '9', '12', '15', '14', '13', '8', '6', '7', '5', '3', '1', '10', '0']
        }
      } else {
        if ('0' in this.value_u) {
          this.value_u.remove('0');
        }
      }

    },
    // 查询数据
    get_data() {
      let data_send = {
        value_u: this.value_u,
        value_time: this.value_time,
        f_number: 1,
        p_number: this.p_number,
        key_word: this.key_word,
        customer_name: this.customer_name,
      }
      let token_s1 = sessionStorage.token || localStorage.token
      SelectData({data: data_send,headers:{'Authorization':'jwt ' + token_s1}})
        .then((data) => {
          // console.log(data)
          // console.log(data.data.token)
          // console.log(data.data.username);
          this.tableData = data.data.data_list;

          this.count_t = data.data.count_t;
          // console.log(data.data);
          if (data.data.data_list.length < 1) {
            this.$message({
              message: '亲~  没有查询到数据呢！',
              type: 'error',
              offset: 100
            });

          }
        })
        .catch((err) => {
          this.$message({
            message: err.data,
            type: 'error',
            offset: 100
          });
        });
    },
    // excel 表下载
    exportExcel() {
      if (this.d_status === 0) {
        this.$message({
          message: '亲~ 在下载中不要重复点击呢！',
          type: 'error',
          offset: 100
        });


      } else {
        this.d_status = 0

        this.value_time_str = []
        for (let i in this.value_time) {

          let date = new Date(this.value_time[i])
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
          let dateTime = y + '-' + m + '-' + d + ' ' + h + ':' + M + ':' + s;
          this.value_time_str.push(dateTime)
        }

        let data_send = {
          value_u: this.value_u,
          value_time: this.value_time,
          f_number: 1,
          p_number: this.p_number,
          key_word: this.key_word,
          customer_name: this.customer_name,
          download: 'ture',

        }
let token_s1 = sessionStorage.token || localStorage.token
        SelectData(
          {data: data_send, responseType: 'blob'},
        )
          .then((data) => {


            this.d_status = 1
            const filename = data.headers["content-disposition"];
            const blob = new Blob([data.data]);
            var downloadElement = document.createElement("a");
            var href = window.URL.createObjectURL(blob);
            downloadElement.href = href;
            // alert('5')

            downloadElement.download = decodeURIComponent(filename.split("filename=")[1]);
            document.body.appendChild(downloadElement);
            downloadElement.click();
            document.body.removeChild(downloadElement);
            window.URL.revokeObjectURL(href);

          })
          .catch((err) => {
            this.$message({
              message: '亲~ 没有数据呢！看看能不能查询到数据，查到数据无法导出请联系管理员！',
              type: 'error',
              offset: 100
            });

            this.d_status = 1

          })
      }
    },

    handleCurrentChange1(val) {
      // alert(this.p_number)


      let data_send = {
        value_u: this.value_u,
        value_time: this.value_time,
        f_number: val,
        p_number: this.p_number,
        key_word: this.key_word,
        customer_name: this.customer_name,
      }
let token_s1 = sessionStorage.token || localStorage.token
      SelectData(
        {data: data_send,headers:{'Authorization':'jwt ' + token_s1}}
      )
        .then((data) => {
          console.log(data)
          // console.log(data.data.token)
          // console.log(data.data.username);
          this.tableData = data.data.data_list
          this.count_t = data.data.count_t
          console.log(data.data)
        })
        .catch((err) => {
          console.log(err.data);
        });

      console.log(`当前页: ${val}`);
    },

    handleSizeChange1(val) {
      console.log(`每页 ${val} 条`);
      this.p_number = val;


    },
  }
}
</script>

<style scoped>


>>> .el-range-separator {
  width: 20px;
}

>>> .el-input__inner {
  /*border-radius: 60px;*/
}

a {
  text-decoration: none;
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

.box-content {
  padding: 4px 0;
}
</style>
