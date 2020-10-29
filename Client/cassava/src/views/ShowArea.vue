<template>
  <div class="show-area">
    <v-container>
      <v-row>
        <v-btn color="#1CE227" rounded>+ เพิ่มข้อมูลมันสำปะหลัง</v-btn>
      </v-row>
      <v-row>
        <v-col cols="8">
          <!-- For Map -->
        </v-col>
        <v-col cols="4">
          <v-simple-table
            fixed-header
            height="400px"
            style="padding-bottom: 20px"
          >
            <template v-slot:default>
              <thead>
                <tr>
                  <th class="text-center" style="background-color: #ffa9a9">
                    ชื่อแปลง
                  </th>
                  <th class="text-center" style="background-color: #ffa9a9">
                    รายละเอียด
                  </th>
                </tr>
              </thead>
              <tbody>
                <tr
                  class="elevation-1"
                  v-for="item in desserts"
                  :key="item.name"
                  style="text:center"
                >
                  <td>{{ item.name }}</td>
                  <td>{{ item.calories }}</td>
                </tr>
              </tbody>
            </template>
          </v-simple-table>
        </v-col>
      </v-row>
      <v-row>
        <v-col class="text-right">
          <v-btn rounded style="margin-end: 10px">ย้อนกลับ</v-btn>
          <v-btn color="#1CE227" rounded>บันทึก</v-btn>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
export default {
  data: () => ({
    selectstate: "",
    itemsstate: ["ขอนแก่น", "เลย", "เชียงใหม่", "อุบลราชธานี"],
    selectdistrict: "",
    itemsdistrict: ["เมือง", "เลย", "เชียงใหม่", "อุบลราชธานี"],
    selectgrade:"",
    itemsgrade: ["A","B","C"],
    desserts: [
      {
        name: "Frozen Yogurt",
        calories: 159,
      },
      {
        name: "Ice cream sandwich",
        calories: 237,
      },
      {
        name: "Eclair",
        calories: 262,
      },
      {
        name: "Cupcake",
        calories: 305,
      },
      {
        name: "Gingerbread",
        calories: 356,
      },
      {
        name: "Jelly bean",
        calories: 375,
      },
      {
        name: "Lollipop",
        calories: 392,
      },
      {
        name: "Honeycomb",
        calories: 408,
      },
      {
        name: "Donut",
        calories: 452,
      },
      {
        name: "KitKat",
        calories: 518,
      },
    ],
  }),
};
</script>
<style scoped>
</style>