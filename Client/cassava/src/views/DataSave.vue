<template>
  <div class="data-save">
    <v-container>
      <v-row>
        <v-col cols="2"> ข้อมูลผลตรวจคุณภาพ</v-col>
      </v-row>
      <v-row class="text-center" justify="left">
        <v-col cols="2"
          ><v-menu
            v-model="menu2"
            :close-on-content-click="true"
            :nudge-right="40"
            transition="scale-transition"
            offset-y
            min-width="290px"
          >
            <template v-slot:activator="{ on, attrs }">
              <v-text-field
                v-model="date"
                label="วัน/เดือน/ปี ที่บันทึก"
                prepend-icon="mdi-calendar"
                readonly
                v-bind="attrs"
                v-on="on"
              ></v-text-field>
            </template>
            <v-date-picker
              v-model="date"
              @input="menu2 = false"
            ></v-date-picker> </v-menu
        ></v-col>
        <v-col cols="2"><v-text-field
            v-model="title"
            :rules="rules"
            hint="กรุณาใส่ละติจูด"
            label="ละติจูด"
          ></v-text-field></v-col>
      </v-row>
      <v-simple-table fixed-header height="450px" style="padding-bottom: 20px">
        <template v-slot:default>
          <thead>
            <tr>
              <th class="text-center" style="background-color: #ffa9a9">
                หัวที่
              </th>
              <th class="text-center" style="background-color: #ffa9a9">
                เปอร์เซ็นต์แป้ง(%)
              </th>
              <th class="text-center" style="background-color: #ffa9a9">
                อุณหภูมิ(เซลเซียส)
              </th>
              <th class="text-center" style="background-color: #ffa9a9">
                ความชื้นสัมพัทธ์(%)
              </th>
            </tr>
          </thead>
          <tbody>
            <tr class="text-center" v-for="item in desserts" :key="item.name">
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
    datekeepdata: "13/1/2563",
    cassvanaage: 12,
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