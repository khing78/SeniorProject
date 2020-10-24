<template>
  <div class="area-detail-chart">
    <v-container>
      <v-row>
        <v-col cols="3"> แปลง {{areaname}}</v-col>
        <v-col class="text-right">
        </v-col>
      </v-row>
      <v-row >
          <v-col cols="9">
            <canvas id="myChart" width="400" height="200"></canvas>
              <!-- For Graph -->
          </v-col>
          <v-col cols="3">
              เกรดคุณภาพแป้ง: {{gradecassvana}}
              <br>
              เปอร์เซ็นต์แป้ง(%)เฉลี่ย: {{precentstarch}}
              <br>
              วันที่ทำการวัด(ว/ด/ป): {{dategetdata}}
              <br>
              อุณหภูมิ(เซลเซียส): {{temputure}}
              <br>
              อายุของมันสำปะหลัง(เดือน): {{cassvanaage}}
          </v-col>
      </v-row>
      <v-row>
          <v-btn rounded>
              ย้อนกลับ
          </v-btn>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import Chart from 'chart.js'
window.addEventListener('load', function() {
var ctx = document.getElementById('myChart');
// eslint-disable-next-line no-unused-vars
var myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange','x','x','x','x','x'],
        datasets: [{
            label: '# of Votes',
            data: [12, 19, 3, 5, 2, 3,2,3,6,4,6],
            borderColor: 'rgba(0, 0, 0, 1)',
            fill: false,
        }]
    },
    options: {
        
    }
});
});
export default {
  data: () => ({
      areaname: "สมชาย",
      gradecassvana: "A",
      precentstarch: 5,
      dategetdata: "26/5/2563",
      temputure: 35.25,
      cassvanaage: 12,
  }),
};
</script>
<style scoped>
</style>