<template>
  <div class="show-all-area">
    <v-container>
      <v-row>
        <v-btn color="#1CE227" rounded>+ เพิ่มแปลงใหม่</v-btn>
        <v-col cols="2">
          <v-combobox
            v-model="selectstate"
            :items="itemsstate"
            label="จังหวัด"
            outlined
            dense
          ></v-combobox>
        </v-col>
        <v-col cols="2">
          <v-combobox
            v-model="selectdistrict"
            :items="itemsdistrict"
            label="อำเภอ"
            outlined
            dense
          ></v-combobox>
        </v-col>
        <v-col cols="2">
          <v-combobox
            v-model="selectgrade"
            :items="itemsgrade"
            label="สถานะ"
            outlined
            dense
          ></v-combobox>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="8">
          <GmapMap
            :center="{ lat: latitude, lng: longitude }"
            :zoom="7"
            map-type-id="terrain"
            style="width: 100%; height: 100%"
          >
            <GmapMarker
              :key="index"
              v-for="(m, index) in markers"
              :position="m.position"
              :clickable="true"
              :draggable="true"
              @click="center = m.position"
            />
          </GmapMap>
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
    latitude:30,
    longitude:30,
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