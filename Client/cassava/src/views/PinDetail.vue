<template>
  <v-main class="pin-detail">
    <v-container>
      <v-row>
        <v-col cols="12" class="text-right">
          <v-btn rounded @click="moveto('chart')">กราฟ</v-btn>
        </v-col>
      </v-row>
      <v-row class="text-center" justify="center">
        <v-col class="text-center">
          เปอร์เซ็นต์แป้งเฉลี่ย(%): {{ precentstarchavg }}
          <br />
          วันที่เก็บข้อมูล: {{ showdate }}
          <br />
          อายุของมันสำปะหลัง(ณ เวลาที่เก็บข้อมูล): {{ cassavaage }} เดือน
          <br />
        </v-col>
      </v-row>
      <v-simple-table fixed-header height="400px" style="padding-bottom: 20px">
        <template v-slot:default>
          <thead>
            <tr>
              <th class="text-center" style="background-color: #ffa9a9">
                เปอร์เซ็นต์แป้ง(%)
              </th>
              <th class="text-center" style="background-color: #ffa9a9">
                อุณหภูมิ(เซลเซียส)
              </th>
              <th class="text-center" style="background-color: #ffa9a9">
                ความชื้นสัมพัทธ์(%)
              </th>
            </tr>
          </thead>
          <tbody>
            <tr class="text-center" v-for="item in detailpin" :key="item.name">
              <td>{{ item.starchPercentage }}</td>
              <td>{{ item.temperature }}</td>
              <td>{{ item.humidity }}</td>
            </tr>
          </tbody>
        </template>
      </v-simple-table>
      <v-row>
        <v-col class="text-left">
          <v-btn color="#F2F2F2" rounded @click="moveto('back')">ย้อนกลับ</v-btn>
        </v-col>
        <v-col class="text-right">
          <v-btn color="#FFB200" rounded @click="editdata()">แก้ไข</v-btn>
        </v-col>
      </v-row>
    </v-container>
  </v-main>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  data: () => ({
    areanumber: 1,
    precentstarchavg: 26.02,
    cassavaage: 12,
    showdate: "",
    detailpin: [
      {
        starchPercentage: 25.5,
        temperature: 28.35,
        humidity: 50,
      },
      {
        starchPercentage: 28.09,
        temperature: 28.32,
        humidity: 50,
      },
      {
        starchPercentage: 31.07,
        temperature: 28.12,
        humidity: 50,
      },
      {
        starchPercentage: 18.03,
        temperature: 28.63,
        humidity: 50,
      },
      {
        starchPercentage: 27.03,
        temperature: 28.66,
        humidity: 50,
      },
    ],
  }),
  mounted() {
    this.totalprecent();
    this.calculatormonthstart()
  },
  computed:{
      ...mapGetters({
      areadetail: "getDetailArea",
      selecteddate : "getSelectedDate",
      selectedarea : "getSelectedArea",
      dateplant: "getDatePlant",
    }),
    
  },
  async created(){
    this.startshow()
    this.formatDate(this.selecteddate)
  },
  methods: {
    formatDate(date) {
      const [year, month, day] = date.split("-");
      const newyear = parseInt(year) + 543;
      this.showdate = `${day}/${month}/${newyear}`;
    },
    calculatormonthstart() {
      var currentdate = this.selecteddate
      console.log(currentdate)
      if (currentdate != null) {
        var totalmonth = 0
        const [year, month, day] = currentdate.split("-");
        var [startyear, startmonth, startday] = this.dateplant.split("-");
        console.log(startday,day)
        var currentmonth = parseInt(startmonth)
        var newstartmonth = parseInt(month) 
        var currentyear = parseInt(startyear)
        var newstartyear = parseInt(year)
        if (newstartmonth >= currentmonth){
          totalmonth = newstartmonth - currentmonth
        }
        else{
          totalmonth = newstartmonth - currentmonth
        }
        if (currentyear >= newstartyear){
            totalmonth += (currentyear - newstartyear)*12
          }
          else{
            totalmonth += (newstartyear - currentyear )*12
          }
        this.cassavaage = totalmonth
      }
    },
    startshow(){
      var i = 0
      var m = 0
      this.detailpin = []
      var detailsaver = []
      while(i < this.areadetail.length){
        if (this.areadetail[i].cassavaareaid == this.selectedarea){
          detailsaver.push(this.areadetail[i])
          break
        }
        i++
      }
      while(m < detailsaver[0].datadetail.length){
        if(detailsaver[0].datadetail[m].dategetdata == this.selecteddate){
          console.log(detailsaver[0].datadetail[m])
          this.detailpin.push(detailsaver[0].datadetail[m])
        }
        m++
      }
    },
    totalprecent() {
      var i = 0;
      var totalstarch = 0;
      while (i < this.detailpin.length) {
        totalstarch += this.detailpin[i].starchPercentage;
        i++;
      }
      this.precentstarchavg = (totalstarch / this.detailpin.length).toFixed(2);
      if(isNaN(this.precentstarchavg)){
        this.precentstarchavg = 0
      }
    },
    moveto(i) {
      const vm = this;
      if (i == "back") {
        vm.$router.back();
      }
      if (i == "chart"){
        vm.$router.push("/area-detail-chart");
      }
    },
    editdata() {
      //ไปดึงที่หน้าเพิ่มข้อมูลมันสำปะหลัง พร้อมดึง ID จากฐานข้อมูล
      const vm = this;
      vm.$router.push("/data-save");
    },
  },
};
</script>
<style scoped>
</style>