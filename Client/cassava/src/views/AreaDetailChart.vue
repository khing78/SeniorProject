<template>
  <v-main class="area-detail-chart">
    <v-container>
      <v-row>
        <v-col cols="3"> แปลง {{ areaname }}</v-col>
        <v-col class="text-right"> </v-col>
      </v-row>
      <v-row>
        <v-col cols="12" md="4" sm="5">
          <v-menu
            :close-on-content-click="false"
            :nudge-right="40"
            transition="scale-transition"
            offset-y
            min-width="290px"
          >
            <template v-slot:activator="{ on, attrs }">
              <v-text-field
                v-model="computedDatetoFormatted"
                label="วัน/เดือน/ปี ที่บันทึก"
                prepend-icon="mdi-calendar"
                readonly
                v-bind="attrs"
                v-on="on"
              ></v-text-field>
            </template>
            <v-date-picker
              v-model="dateto"
              range
            ></v-date-picker>
          </v-menu>
        </v-col>
        <v-col cols="12" md="2" sm="3" class="text-center">
          <v-btn id="resetchartbutton" @click="changechart()">
            ยืนยัน
          </v-btn>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="12" md="9">
          <div id="showchart">
            <line-chart id="chartee" ref="chartee" style="height:400px"></line-chart>
            <!--<canvas id="myChart"></canvas>-->
          </div>
        </v-col>
        <v-col cols="12" md="3">
          เกรดคุณภาพแป้งเฉลี่ย: {{ gradecassava }}
          <br />
          เปอร์เซ็นต์แป้งเฉลี่ย(%): {{ precentstarchaverage }}
          <br />
          อุณหภูมิเฉลี่ย(เซลเซียส): {{ temputure }}
          <br />
          อายุของมันสำปะหลัง(เดือน): {{ cassavaage }}
        </v-col>
      </v-row>
      <v-row>
        <v-btn rounded @click="moveto('back')"> ย้อนกลับ </v-btn>
      </v-row>
    </v-container>
  </v-main>
</template>
<script>
import LineChart from "@/components/LineChart";
export default {
  components: {
    LineChart,
  },
  data: () => ({
    dateto: [new Date().toISOString().substr(0, 10), new Date().toISOString().substr(0, 10)],
    fromdate:"",
    todate:"",
    menu: false,
    modal: false,
    menu2: false,
    areaname: "สมชาย",
    gradecassava: "B",
    precentstarchaverage: 28.52,
    dategetdata: "26/5/2563",
    temputure: 35.25,
    cassavaage: 12,
    addDatachartw: [0, 1, 2, 3],
    datachart:{
      day:["15/6/2563",
          "11/7/2563",
          "12/7/2563",
          "18/8/2563",
          "11/8/2563",
          "6/9/2563",
          "8/9/2563",],
      precentstarch:[22, 19, 22, 25, 26, 27, 26],
    },
    pindetail:[
        {
          id:0,
          daygetdata:"15/11/2563",
          precentstarch: 10.45,
          temputure: 25.05
        },
        {
          id:1,
          daygetdata:"18/11/2563",
          precentstarch: 13.43,
          temputure: 32.02
        },
        {
          id:2,
          daygetdata:"27/11/2563",
          precentstarch: 18.85,
          temputure: 31.12
        },
        {
          id:3,
          daygetdata:"5/12/2563",
          precentstarch: 22.15,
          temputure: 28.04
        },
        {
          id:4,
          daygetdata:"8/12/2563",
          precentstarch: 25.12,
          temputure: 27.03
        },
        {
          id:5,
          daygetdata:"19/12/2563",
          precentstarch: 24.53,
          temputure: 26.15
        },
        {
          id:6,
          daygetdata:"20/12/2563",
          precentstarch: 21.25,
          temputure: 24.05
        },
      ],
  }),
  computed: {
    computedDatetoFormatted() {
      return this.formatDate(this.dateto);
    },
  },
  methods: {
    moveto(i) {
      const vm = this;
      if (i == "back") {
        vm.$router.push("/show-area");
      }
    },
    formatDate(date) {
      var fromday = date[0]
      var today = date[1]
      if(date[0]>date[1]){
        this.dateto[0] = today
        this.dateto[1] = fromday
      }
      var i = 0
      var finsheddate = ""
      if (!date) return null;
      while(i < date.length){
        const [year, month, day] = date[i].split("-");
        const newyear = parseInt(year) + 543;
        finsheddate += `${day}/${month}/${newyear}`
        if(i+1 != date.length){
          finsheddate += " - "
          this.fromdate = `${day}/${month}/${newyear}`
          console.log(this.fromdate)
        }
        else{
          this.todate = `${day}/${month}/${newyear}`
          console.log(this.todate)
        }
        i++
      }
      
      return finsheddate;
    },
    checkday(){
      var [fromday,frommonth,fromyear] = this.fromdate.split("/")
      fromday = parseInt(fromday)
      frommonth = parseInt(frommonth)
      fromyear = parseInt(fromyear)
      var [today,tomonth,toyear] = this.todate.split("/")
      today = parseInt(today)
      tomonth = parseInt(tomonth)
      toyear = parseInt(toyear)
      var i = 0
      var dayforchart = []
      var precentforchart = []
      var tempforcal = []
      console.log(tomonth)
      console.log(frommonth)
      while(i < this.pindetail.length){
        var [selecteday,selectmonth,selectyear] = this.pindetail[i].daygetdata.split("/")
        selecteday = parseInt(selecteday)
        selectmonth = parseInt(selectmonth)
        selectyear = parseInt(selectyear)
        if (fromday <= selecteday && selecteday <= today){
          if(frommonth <= selectmonth && selectmonth <= tomonth){
            if(fromyear <= selectyear && selectyear <= toyear){
              dayforchart.push(this.pindetail[i].daygetdata)
              precentforchart.push(this.pindetail[i].precentstarch)
              tempforcal.push(this.pindetail[i].temputure)
            }
          }
        }
        i++
      }
      return [dayforchart,precentforchart,tempforcal]
    },
    changedetailside(precentforchart,tempforcal){
      var i = 0
      var totalprecent = 0
      var avgprecent = 0
      var tempall = 0
      while(i < precentforchart.length){
        totalprecent += precentforchart[i]
        tempall += tempforcal[i]
        i++
      }
      avgprecent = totalprecent/precentforchart.length
      this.precentstarchaverage = avgprecent.toFixed(2)
      this.temputure = (tempall/tempforcal.length).toFixed(2)
      if(avgprecent < 25){
        this.gradecassava = "C"
      }
      else if(avgprecent < 30){
        this.gradecassava = "B"
      }
      else if(avgprecent >= 30){
        this.gradecassava = "A"
      }
    },
    changechart() {
      var [dayforchart,precentforchart,tempforcal] = this.checkday()
      this.changedetailside(precentforchart,tempforcal)
      console.log(dayforchart)
      console.log(precentforchart)
      var chart = this.$refs.chartee;
      //console.log(chart.datacollection.labels.length)
      chart.datacollection.labels = dayforchart
      chart.datacollection.datasets[0].data = precentforchart
      /*chart.datacollection.datasets.forEach((dataset) => {
        dataset.data.push(data);
      });*/

      chart.refreashchart();
    },
  },
};
</script>
<style scoped>
#todatelabel {
  text-align: center;
  padding: 3vh;
}
</style>