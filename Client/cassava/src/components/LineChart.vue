<script>
import { Line } from "vue-chartjs";

export default {
  extends: Line,
  data() {
    return {
      datacollection: {
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
            label: "ปริมาณแป้งมันสำปะหลัง(%)",
            data: [2, 9, 15, 25, 26, 27, 26, 25, 25.5, 26.5, 24],
            pointRadius: 5,
            pointHoverRadius: 9,
          },
        ],
      },
      options: {
        tooltip: {
          callbacks: {
            title: function (tooltipItem, data) {
              return data["labels"][tooltipItem[0]["index"]];
            },
          },
        },
        scales: {
          yAxes: [
            {
              ticks: {
                beginAtZero: true,
              },
              gridLines: {
                display: true,
              },
            },
          ],
          xAxes: [
            {
              gridLines: {
                display: false,
              },
            },
          ],
        },
        legend: {
          display: true,
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
  methods:{
    refreashchart(){
      this.renderChart(this.datacollection, this.options);
    }
  },
  mounted() {
    this.renderChart(this.datacollection, this.options);
  },
};
</script>