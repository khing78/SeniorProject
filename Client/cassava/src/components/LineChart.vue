<script>
import { Line } from "vue-chartjs";

export default {
  extends: Line,
  data() {
    return {
      datacollection: {
        labels: [],
        datasets: [
          {
            label: "ปริมาณแป้งมันสำปะหลัง(%)",
            data: [],
            pointRadius: 5,
            pointHoverRadius: 9,
          },
        ],
      },
      options: {
        /*onClick: function (e) {
          var activePoints = this.getElementsAtEvent(e);
          var selectedIndex = activePoints[0]._index;
          alert(this.data.datasets[0].data[selectedIndex]);
        },*/
        tooltips: {
          enabled: true,
          callbacks: {
            label: function (tooltipItem, data) {
              let dataset = data.datasets[tooltipItem.datasetIndex];
              let currentValue = dataset.data[tooltipItem.index];
              var allword = "เปอร์เซ็นต์แป้ง = " + currentValue + "%";
              return allword;
            },
          },
        },
        scales: {
          yAxes: [
            {
              gridLines: {
                display: true,
              },
              scaleLabel: {
                display: true,
                labelString: "เปอร์เซ็นต์แป้งมันสำปะหลัง(%)",
              },
            },
          ],
          xAxes: [
            {
              gridLines: {
                display: false,
              },
              scaleLabel: {
                display: true,
                labelString: "วัน/เดือน/ปี ที่บันทึก",
              },
            },
          ],
        },
        elements: {
          line: {
            fill: false,
            tension: 0,
            borderColor: "rgba(76, 156, 0, 1)",
          },
        },
        responsive: true,
        maintainAspectRatio: false,
      },
    };
  },
  methods: {
    refreashchart() {
      this.renderChart(this.datacollection, this.options);
    },
  },
  mounted() {
    this.renderChart(this.datacollection, this.options);
  },
};
</script>