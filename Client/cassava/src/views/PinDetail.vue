<template>
  <div class="pin-detail">
    <v-container>
      <v-row>
        <v-col cols="1"> พื้นที่ {{ areanumber }} </v-col>
      </v-row>
      <v-row class="text-center" justify="center">
        <v-col class="text-center"> เปอร์เซ็นต์แป้งเฉลี่ย(%): {{precentstarch}}
          <br>
          วันที่เก็บข้อมูล: {{datekeepdata}}
          <br>
          อายุของมันสำปะหลัง(ณ เวลาที่เก็บข้อมูล): {{cassvanaage}} เดือน
        </v-col>
      </v-row>
  <v-simple-table fixed-header height="400px" style="padding-bottom:20px">
    <template v-slot:default>
      <thead>
        <tr>
          <th class="text-center" style="background-color:#FFA9A9">
            หัวที่
          </th>
          <th class="text-center" style="background-color:#FFA9A9">
            เปอร์เซ็นต์แป้ง(%)
          </th>
          <th class="text-center" style="background-color:#FFA9A9">
            อุณหภูมิ(เซลเซียส)
          </th>
          <th class="text-center" style="background-color:#FFA9A9">
            ความชื้นสัมพัทธ์(%)
          </th>
        </tr>
      </thead>
      <tbody>
        <tr class="text-center"
          v-for="item in desserts"
          :key="item.name"
        >
          <td>{{ item.name }}</td>
          <td>{{ item.calories }}</td>
        </tr>
      </tbody>
    </template>
  </v-simple-table>
  <v-row>
    <v-col class="text-left">
      <v-btn color="#F2F2F2" rounded>ยกเลิก</v-btn>
    </v-col>
    <v-col class="text-right">
      <v-btn color="#FFB200" rounded>แก้ไข</v-btn>
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
    desserts: [
          {
            name: 'Frozen Yogurt',
            calories: 159,
          },
          {
            name: 'Ice cream sandwich',
            calories: 237,
          },
          {
            name: 'Eclair',
            calories: 262,
          },
          {
            name: 'Cupcake',
            calories: 305,
          },
          {
            name: 'Gingerbread',
            calories: 356,
          },
          {
            name: 'Jelly bean',
            calories: 375,
          },
          {
            name: 'Lollipop',
            calories: 392,
          },
          {
            name: 'Honeycomb',
            calories: 408,
          },
          {
            name: 'Donut',
            calories: 452,
          },
          {
            name: 'KitKat',
            calories: 518,
          },
        ],
  }),
};
</script>
<style scoped>
</style>