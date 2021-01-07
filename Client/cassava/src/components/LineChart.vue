<script>
import { Line } from "vue-chartjs";

export default {
  extends: Line,
  data() {
    return {
      datacollection: {
        labels: [
          "21/6/2563",
          "22/6/2563",
          "23/6/2563",
          "26/6/2563",
          "29/6/2563",
          "6/7/2563",
          "8/7/2563",
        ],
        datasets: [
          {
            label: "ปริมาณแป้งมันสำปะหลัง(%)",
            data: [22, 19, 15, 25, 26, 27, 26, 25, 25.5, 26.5, 24],
            pointRadius: 5,
            pointHoverRadius: 9,
          },
        ],
      },
      options: {
        scales: {
          yAxes: [
            {
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