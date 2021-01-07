<template>
  <v-main class="area-detail-chart">
    <v-container>
      <v-row>
        <v-col cols="3"> แปลง {{ areaname }}</v-col>
        <v-col class="text-right"> </v-col>
      </v-row>
      <v-row>
        <v-col cols="12" md="2" sm="3">
          <v-menu
            :close-on-content-click="true"
            :nudge-right="40"
            transition="scale-transition"
            offset-y
            min-width="290px"
          >
            <template v-slot:activator="{ on, attrs }">
              <v-text-field
                v-model="computedDateFromFormatted"
                label="วัน/เดือน/ปี ที่บันทึก"
                prepend-icon="mdi-calendar"
                readonly
                v-bind="attrs"
                v-on="on"
              ></v-text-field>
            </template>
            <v-date-picker
              v-model="datefrom"
              @input="menu2 = false"
            ></v-date-picker>
          </v-menu>
        </v-col>
        <div id="todatelabel">ถึง</div>
        <v-col cols="12" md="2" sm="3">
          <v-menu
            :close-on-content-click="true"
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
              @input="menu2 = false"
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
    datefrom: new Date().toISOString().substr(0, 10),
    dateto: new Date().toISOString().substr(0, 10),
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
      pindtail:[
        {
          id:0,
          daygetdata:"15/6/2563",
          precentstarch: 10.45
        },
        {
          id:1,
          daygetdata:"18/6/2563",
          precentstarch: 13.43
        },
        {
          id:2,
          daygetdata:"15/6/2563",
          precentstarch: 18.85
        },
        {
          id:3,
          daygetdata:"15/6/2563",
          precentstarch: 22.15
        },
        {
          id:4,
          daygetdata:"15/6/2563",
          precentstarch: 25.12
        },
        {
          id:5,
          daygetdata:"15/6/2563",
          precentstarch: 24.53
        },
        {
          id:6,
          daygetdata:"15/6/2563",
          precentstarch: 21.25
        },
      ]
    },
  }),
  computed: {
    computedDateFromFormatted() {
      return this.formatDate(this.datefrom);
    },
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
    afterselectdate() {
      //แสดงข้อมูลตั้งแต่วันที่ถึงวันที่
    },
    formatDate(date) {
      if (!date) return null;

      const [year, month, day] = date.split("-");
      const newyear = parseInt(year) + 543;
      return `${day}/${month}/${newyear}`;
    },
    addDatachart(label, data) {
      var chart = this.$refs.chartee;
      chart.datacollection.labels.push(label);
      chart.datacollection.datasets.forEach((dataset) => {
        dataset.data.push(data);
      });
      chart.update();
    },
    changechart() {
      var chart = this.$refs.chartee;
      //console.log(chart.datacollection.labels.length)
      chart.datacollection.labels = this.datachart.day
      chart.datacollection.datasets[0].data = this.datachart.precentstarch
      console.log(this.datachart.day)
      console.log(chart.datacollection.datasets.data)
      /*chart.datacollection.datasets.forEach((dataset) => {
        dataset.data.push(data);
      });*/
      console.log(chart.datacollection.datasets.length)

      chart.refreashchart();
    },
    updatechart(chart) {
      chart.update();
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