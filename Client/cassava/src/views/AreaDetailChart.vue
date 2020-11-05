<template>
  <div class="area-detail-chart">
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
      </v-row>
      <v-row>
        <v-col cols="12" md="9">
          <canvas id="myChart"></canvas>
        </v-col>
        <v-col cols="12" md="3">
          เกรดคุณภาพแป้ง: {{ gradecassvana }}
          <br />
          เปอร์เซ็นต์แป้ง(%)เฉลี่ย: {{ precentstarch }}
          <br />
          วันที่ทำการวัด(ว/ด/ป): {{ dategetdata }}
          <br />
          อุณหภูมิ(เซลเซียส): {{ temputure }}
          <br />
          อายุของมันสำปะหลัง(เดือน): {{ cassvanaage }}
        </v-col>
      </v-row>
      <v-row>
        <v-btn rounded @click="moveto('back')"> ย้อนกลับ </v-btn>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import Chart from "chart.js";
window.addEventListener("load", function () {
  var ctx = document.getElementById("myChart");
  // eslint-disable-next-line no-unused-vars
  var myChart = new Chart(ctx, {
    type: "line",
    data: {
      labels: [
        "21/06/2563",
        "22/06/2563",
        "23/06/2563",
        "26/06/2563",
        "29/06/2563",
        "6/07/2563",
        "8/07/2563",
      ],
      datasets: [
        {
          label: "# of Votes",
          data: [2, 9, 15, 25, 26, 27, 26, 25, 25.5, 26.5, 24],
          borderColor: "rgba(0, 0, 0, 1)",
          fill: false,
        },
      ],
    },
    options: {},
  });
});
export default {
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
      computedDateFromFormatted () {
        return this.formatDate(this.datefrom)
      },
      computedDatetoFormatted (){
        return this.formatDate(this.dateto)
      }
    },
  methods:{
    moveto(i){
      const vm = this
      if (i == "back"){
        vm.$router.push("/show-area")
      }
    },
    formatDate (date) {
        if (!date) return null

        const [year, month, day] = date.split('-')
        return `${day}/${month}/${year}`
      },
  },
};
</script>
<style scoped>
</style>