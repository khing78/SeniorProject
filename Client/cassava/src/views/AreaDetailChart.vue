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
          <v-btn id="resetchartbutton"> ยืนยัน </v-btn>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="12" md="9">
          <div id="showchart">
            <line-chart></line-chart>
            <!--<canvas id="myChart"></canvas>-->
          </div>
        </v-col>
        <v-col cols="12" md="3">
          เกรดคุณภาพแป้งเฉลี่ย: {{ gradecassvana }}
          <br />
          เปอร์เซ็นต์แป้งเฉลี่ย(%): {{ precentstarch }}
          <br />
          อุณหภูมิเฉลี่ย(เซลเซียส): {{ temputure }}
          <br />
          อายุของมันสำปะหลัง(เดือน): {{ cassvanaage }}
        </v-col>
      </v-row>
      <v-row>
        <v-btn rounded @click="moveto('back')"> ย้อนกลับ </v-btn>
      </v-row>
    </v-container>
  </v-main>
</template>
<script>
import LineChart from '@/components/LineChart'
export default {
  components:{
    LineChart
  },
  data: () => ({
    datefrom: new Date().toISOString().substr(0, 10),
    dateto: new Date().toISOString().substr(0, 10),
    menu: false,
    modal: false,
    menu2: false,
    areaname: "สมชาย",
    gradecassvana: "B",
    precentstarch: 28.52,
    dategetdata: "26/5/2563",
    temputure: 35.25,
    cassvanaage: 12,
    
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
    afterselectdate(){
      //แสดงข้อมูลตั้งแต่วันที่ถึงวันที่
    },
    formatDate(date) {
      if (!date) return null;

      const [year, month, day] = date.split("-");
      const newyear = parseInt(year)+543
      return `${day}/${month}/${newyear}`;
    },
    addDatachart(chart, label, data) {
      chart.data.labels.push(label);
      chart.data.datasets.forEach((dataset) => {
        dataset.data.push(data);
      });
      chart.update();
    },
    removeDatachart(chart) {
      chart.data.labels.pop();
      chart.data.datasets.forEach((dataset) => {
        dataset.data.pop();
      });
      chart.update();
    },
    updatechart(chart){
      chart.update()
    }
  },
};
</script>
<style scoped>
#todatelabel {
  text-align: center;
  padding: 3vh;
}
</style>