<template>
  <div class="area-detail-chart">
    <v-container>
      <v-row>
        <v-col cols="3"> แปลง {{areaname}}</v-col>
        <v-col class="text-right">
        </v-col>
      </v-row>
      <v-row>
          <v-col cols="9">
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