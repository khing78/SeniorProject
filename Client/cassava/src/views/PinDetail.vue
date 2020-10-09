<template>
  <div class="pin-detail">
    <v-container>
      <v-row class="text-center" justify="center">
        <v-col cols="1"> พื้นที่ {{ areanumber }} </v-col>
        <v-col cols="10"> เปอร์เซ็นต์แป้ง(%): {{precentstarch}}
          <br>
          วันที่เก็บข้อมูล: {{datekeepdata}}
          <br>
          อายุของมันสำปะหลัง(ณ เวลาที่เก็บข้อมูล): {{cassvanaage}} เดือน
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
export default {
  data: () => ({
    areanumber: 1,
    precentstarch: 35.02,
    datekeepdata: "13/1/2563" ,
    cassvanaage: 12,
  }),
};
</script>
<style scoped>
</style>