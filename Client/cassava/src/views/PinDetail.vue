<template>
  <v-main class="pin-detail">
    <v-container>
      <v-row>
        <v-col cols="1"> พื้นที่ {{ areanumber }} </v-col>
      </v-row>
      <v-row class="text-center" justify="center">
        <v-col class="text-center">
          เปอร์เซ็นต์แป้งเฉลี่ย(%): {{ precentstarchavg }}
          <br />
          วันที่เก็บข้อมูล: {{ datekeepdata }}
          <br />
          อายุของมันสำปะหลัง(ณ เวลาที่เก็บข้อมูล): {{ cassavaage }} เดือน
          <br />
          ระยะขอบเขต: {{ widtharea }} เมตร
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
              <td>{{ item.precentstarch }}</td>
              <td>{{ item.temperture }}</td>
              <td>{{ item.humidity }}</td>
            </tr>
          </tbody>
        </template>
      </v-simple-table>
      <v-row>
        <v-col class="text-left">
          <v-btn color="#F2F2F2" rounded @click="moveto('back')">ยกเลิก</v-btn>
        </v-col>
        <v-col class="text-right">
          <v-btn color="#FFB200" rounded @click="editdata()">แก้ไข</v-btn>
        </v-col>
      </v-row>
    </v-container>
  </v-main>
</template>

<script>
export default {
  data: () => ({
    areanumber: 1,
    precentstarchavg: 26.02,
    datekeepdata: "13/11/2563",
    cassavaage: 12,
    widtharea: 5,
    detailpin: [
      {
        precentstarch: 25.5,
        temperture: 28.35,
        humidity: 50,
      },
      {
        precentstarch: 28.09,
        temperture: 28.32,
        humidity: 50,
      },
      {
        precentstarch: 31.07,
        temperture: 28.12,
        humidity: 50,
      },
      {
        precentstarch: 18.03,
        temperture: 28.63,
        humidity: 50,
      },
      {
        precentstarch: 27.03,
        temperture: 28.66,
        humidity: 50,
      },
    ],
  }),
  mounted() {
    this.totalprecent();
    this.calculatormonthstart()
  },
  methods: {
    calculatormonthstart() {
      var currentdate = new Date().toISOString().substr(0, 10);
      console.log(currentdate)
      if (currentdate != null) {
        var totalmonth = 0
        const [year, month, day] = currentdate.split("-");
        const newyear = parseInt(year) + 543;
        var [startday, startmonth, startyear] = this.datekeepdata.split("/");
        console.log(startday,day)
        var currentmonth = parseInt(startmonth)
        var newstartmonth = parseInt(month) 
        var currentyear = parseInt(startyear)
        var newstartyear = parseInt(newyear)
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
    totalprecent() {
      var i = 0;
      var totalstarch = 0;
      while (i < this.detailpin.length) {
        totalstarch += this.detailpin[i].precentstarch;
        i++;
      }
      this.precentstarchavg = (totalstarch / this.detailpin.length).toFixed(2);
    },
    moveto(i) {
      const vm = this;
      if (i == "back") {
        vm.$router.back();
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