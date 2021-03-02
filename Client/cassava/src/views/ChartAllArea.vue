<template>
  <v-main class="chart-all-area">
    <v-container fluid>
      <v-row>
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
            <v-date-picker v-model="dateto" range></v-date-picker>
          </v-menu>
        </v-col>
        <v-col cols="12" md="2" sm="3" class="text-center">
          <v-btn id="resetchartbutton" @click="changechart()"> ยืนยัน </v-btn>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="12" md="8">
          <div id="showchart">
            <line-chart
              id="chartee"
              ref="chartee"
              style="height: 500px;"
              class="ma-0"
            ></line-chart>
          </div>
        </v-col>
        <v-col cols="12" md="4" style="font-size: 20px" class="ma-0">
         <v-col cols="4" class="ma-0">
            แปลงที่ 1
            เกรดคุณภาพแป้งเฉลี่ย: {{ gradecassava }}
            <br />
            เปอร์เซ็นต์แป้งเฉลี่ย(%): {{ precentstarchaverage }}
            <br />
            อุณหภูมิโดยเฉลี่ย(เซลเซียส): {{ temputure }}
            <br />
            ความชื้นสัมพันธ์โดยเฉลี่ย(%) : {{ humnaity }}
          </v-col>
          <v-col cols="4" class="ma-0">
            แปลงที่ 2
            เกรดคุณภาพแป้งเฉลี่ย: {{ gradecassava }}
            <br />
            เปอร์เซ็นต์แป้งเฉลี่ย(%): {{ precentstarchaverage }}
            <br />
            อุณหภูมิโดยเฉลี่ย(เซลเซียส): {{ temputure }}
            <br />
            ความชื้นสัมพันธ์โดยเฉลี่ย(%) : {{ humnaity }}
          </v-col>
          <v-col cols="4" class="ma-0">
            แปลงที่ 3
            เกรดคุณภาพแป้งเฉลี่ย: {{ gradecassava }}
            <br />
            เปอร์เซ็นต์แป้งเฉลี่ย(%): {{ precentstarchaverage }}
            <br />
            อุณหภูมิโดยเฉลี่ย(เซลเซียส): {{ temputure }}
            <br />
            ความชื้นสัมพันธ์โดยเฉลี่ย(%) : {{ humnaity }}
          </v-col>
          <v-col cols="4" class="ma-0">
            แปลงที่ 4
            เกรดคุณภาพแป้งเฉลี่ย: {{ gradecassava }}
            <br />
            เปอร์เซ็นต์แป้งเฉลี่ย(%): {{ precentstarchaverage }}
            <br />
            อุณหภูมิโดยเฉลี่ย(เซลเซียส): {{ temputure }}
            <br />
            ความชื้นสัมพันธ์โดยเฉลี่ย(%) : {{ humnaity }}
          </v-col>
        </v-col>
      </v-row>
      <v-row>
        <v-btn rounded @click="moveto('back')" style="font-size: 18px">
          ย้อนกลับ
        </v-btn>
      </v-row>
    </v-container>
  </v-main>
</template>
<script>
import LineChart from "@/components/LineChart";
import { mapGetters } from "vuex";
export default {
  components: {
    LineChart,
  },
  data: () => ({
    dateto: [
      new Date().toISOString().substr(0, 10),
      new Date().toISOString().substr(0, 10),
    ],
    fromdate: "",
    todate: "",
    menu: false,
    modal: false,
    menu2: false,
    areaname: "",
    humnaity: 0,
    gradecassava: "-",
    precentstarchaverage: 0,
    temputure: 0,
    addDatachartw: [0, 1, 2, 3],
    datachart: {
      day: [
        "15/06/2563",
        "11/07/2563",
        "12/07/2563",
        "18/08/2563",
        "11/08/2563",
        "06/09/2563",
        "08/09/2563",
      ],
      precentstarch: [22, 19, 22, 25, 26, 27, 26],
    },
    pindetail: [
      {
        daygetdata: "15/11/2563",
        precentstarch: 10.45,
        temputure: 25.05,
        humidity: 40,
      },
      {
        daygetdata: "18/11/2563",
        precentstarch: 13.43,
        temputure: 32.02,
        humidity: 30,
      },
      {
        daygetdata: "27/11/2563",
        precentstarch: 18.85,
        temputure: 31.12,
        humidity: 50,
      },
      {
        daygetdata: "05/12/2563",
        precentstarch: 22.15,
        temputure: 28.04,
        humidity: 40,
      },
      {
        daygetdata: "08/12/2563",
        precentstarch: 25.12,
        temputure: 27.03,
        humidity: 30,
      },
      {
        daygetdata: "19/12/2563",
        precentstarch: 24.53,
        temputure: 26.15,
        humidity: 60,
      },
      {
        daygetdata: "20/12/2563",
        precentstarch: 21.25,
        temputure: 24.05,
        humidity: 60,
      },
    ],
  }),
  computed: {
    ...mapGetters({
      detailarea: "getDetailArea",
      selectedarea: "getSelectedArea",
    }),
    computedDatetoFormatted() {
      return this.formatDate(this.dateto);
    },
  },
  created() {
    this.startshow();
  },
  methods: {
    startshow() {
      this.pindetail = [];
      var i = 0;
      var dataforchart = [];
      while (i < this.detailarea.length) {
        if (this.detailarea[i].cassavaareaid == this.selectedarea) {
          dataforchart.push(this.detailarea[i]);
          break;
        }
        i++;
      }
      i = 0;
      while (i < dataforchart[0].datadetail.length) {
        var daygetdata = this.changeformatforshow(
          dataforchart[0].datadetail[i].dategetdata
        );
        var precentstarch = dataforchart[0].datadetail[i].starchPercentage;
        var temputure = dataforchart[0].datadetail[i].temperature;
        var humidity = dataforchart[0].datadetail[i].humidity;
        this.pindetail.push({ daygetdata, precentstarch, temputure, humidity });
        i++;
      }
    },
    moveto(i) {
      const vm = this;
      if (i == "back") {
        vm.$router.back();
      }
    },
    formatDate(date) {
      var fromday = date[0];
      var today = date[1];
      if (date[0] > date[1]) {
        this.dateto[0] = today;
        this.dateto[1] = fromday;
      }
      var i = 0;
      var finsheddate = "";
      if (!date) return null;
      while (i < date.length) {
        const [year, month, day] = date[i].split("-");
        const newyear = parseInt(year) + 543;
        finsheddate += `${day}/${month}/${newyear}`;
        if (i + 1 != date.length) {
          finsheddate += " - ";
          this.fromdate = `${day}/${month}/${newyear}`;
        } else {
          this.todate = `${day}/${month}/${newyear}`;
        }
        i++;
      }

      return finsheddate;
    },
    changeformatforshow(date) {
      if (!date) return null;
      const [year, month, day] = date.split("-");
      const newyear = parseInt(year) + 543;
      return `${day}/${month}/${newyear}`;
    },

    checkday() {
      var newfromdate;
      var newtodate;
      var newselectdate;
      var [fromday, frommonth, fromyear] = this.fromdate.split("/");
      newfromdate = fromyear + frommonth + fromday;
      newfromdate = parseInt(newfromdate);
      var [today, tomonth, toyear] = this.todate.split("/");
      newtodate = toyear + tomonth + today;
      newtodate = parseInt(newtodate);
      var i = 0;
      var dayforchart = [];
      var precentforchart = [];
      var tempforcal = [];
      var huma = [];
      while (i < this.pindetail.length) {
        var [selectday, selectmonth, selectyear] = this.pindetail[
          i
        ].daygetdata.split("/");
        newselectdate = selectyear + selectmonth + selectday;
        newselectdate = parseInt(newselectdate);
        if (newfromdate <= newselectdate && newselectdate <= newtodate) {
          dayforchart.push(this.pindetail[i].daygetdata);
          precentforchart.push(this.pindetail[i].precentstarch);
          tempforcal.push(this.pindetail[i].temputure);
          huma.push(this.pindetail[i].humidity);
        }
        i++;
      }
      return [dayforchart, precentforchart, tempforcal, huma];
    },
    changedetailside(precentforchart, tempforcal, humidity) {
      var i = 0;
      var totalprecent = 0;
      var avgprecent = 0;
      var tempall = 0;
      var humna = 0;
      while (i < precentforchart.length) {
        totalprecent += precentforchart[i];
        tempall += parseFloat(tempforcal[i]);
        humna += parseFloat(humidity[i]);
        i++;
      }
      avgprecent = totalprecent / precentforchart.length;
      this.precentstarchaverage = avgprecent.toFixed(2);
      this.temputure = (tempall / tempforcal.length).toFixed(2);
      this.humnaity = (humna / humidity.length).toFixed(2);
      if (avgprecent < 25) {
        this.gradecassava = "C";
      } else if (avgprecent < 30) {
        this.gradecassava = "B";
      } else if (avgprecent >= 30) {
        this.gradecassava = "A";
      }
    },
    changechart() {
      var [
        dayforchart,
        precentforchart,
        tempforcal,
        humnidity,
      ] = this.checkday();
      this.changedetailside(precentforchart, tempforcal, humnidity);
      var chart = this.$refs.chartee;
      chart.datacollection.labels = dayforchart;
      chart.datacollection.datasets[0].data = precentforchart;

      chart.refreashchart();
    },
  /*changearea(numberarea,clickarea){
    axios
        .get("http://188.166.246.244:6969/farms/")
        .then((response) => {
          var i = 0;
          while (i < response.data.length) {

            i++;
          }
          
        })
        .catch((err) => {
          console.error(err);
        });
  },*/
  },
};
</script>
<style scoped>
#todatelabel {
  text-align: center;
  padding: 3vh;
}
</style>