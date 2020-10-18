<template>
  <div class="data-save">
    <v-container>
      <v-row>
        <v-col cols="3"> ข้อมูลผลตรวจคุณภาพ</v-col>
        <v-col class="text-right">
          <v-btn color="#E21C1C" rounded>ลบข้อมูล</v-btn>
        </v-col>
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
        <v-col cols="2"
          ><v-text-field
            v-model="title"
            :rules="rules"
            hint="กรุณาใส่ละติจูด"
            label="ละติจูด"
          ></v-text-field
        ></v-col>
        <v-col cols="2"
          ><v-text-field
            v-model="title"
            :rules="rules"
            hint="กรุณาใส่ลองจิจูด"
            label="ลองจิจูด"
          ></v-text-field
        ></v-col>
        <v-col cols="2">
          <v-btn>Map</v-btn>
        </v-col>
      </v-row>
      <v-row>
        <v-btn rounded>เพิ่มต้น +</v-btn>
      </v-row>
      <v-simple-table
        fixed-header
        height="350px"
        style="padding-bottom: 20px; padding-top: 20px"
      >
        <template v-slot:default>
          <thead>
            <tr>
              <th class="text-center" style="background-color: #ffa9a9"></th>
            </tr>
          </thead>
          <tbody>
            <tr
              class="text-left"
              v-for="(item, index) in xdata"
              :key="item.name"
            >
              <td>
                หัวที่{{ index + 1 }}<v-btn rounded color="#E21C1C">ลบ</v-btn>
                <br>
                <v-row>
                <v-col cols="2">
                  <v-text-field
                  v-model="item.x1"
                  :rules="rules"
                  hint="X1"
                  label="X1"
                ></v-text-field>
                </v-col>
                <v-col cols="2">
                  <v-text-field
                  v-model="item.x2"
                  :rules="rules"
                  hint="X2"
                  label="X2"
                ></v-text-field>
                </v-col>
                <v-col cols="2">
                  <v-text-field
                  v-model="item.x3"
                  :rules="rules"
                  hint="X3"
                  label="X3"
                ></v-text-field>
                </v-col>
                <v-col cols="2">
                  <v-text-field
                  v-model="item.temputure"
                  :rules="rules"
                  hint="อุณหภูมิ"
                  label="อุณหภูมิ"
                ></v-text-field>
                </v-col>
                </v-row>
                <v-row>
                <v-col cols="2">
                  <v-text-field
                  v-model="item.x4"
                  :rules="rules"
                  hint="X4"
                  label="X4"
                ></v-text-field>
                </v-col>
                <v-col cols="2">
                  <v-text-field
                  v-model="item.x5"
                  :rules="rules"
                  hint="X5"
                  label="X5"
                ></v-text-field>
                </v-col>
                <v-col cols="2">
                  <v-text-field
                  v-model="item.x6"
                  :rules="rules"
                  hint="X6"
                  label="X6"
                ></v-text-field>
                </v-col>
                </v-row>
              </td>
            </tr>
          </tbody>
        </template>
      </v-simple-table>
      <v-row>
        <v-col class="text-left">
          <v-btn color="#F2F2F2" rounded>ยกเลิก</v-btn>
        </v-col>
        <v-col class="text-right">
          <v-btn color="#1CE227" rounded>บันทึก</v-btn>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
export default {
  data: () => ({
    xdata: [
      {
        x1: "Frozen Yogurt",
        x2: "Frozen Yogurt",
        x3: "Frozen Yogurt",
        x4: "Frozen Yogurt",
        x5: "Frozen Yogurt",
        x6: "Frozen Yogurt",
        temputure: 159,
      },
      {
        x1: "Frozen Yogurt",
        x2: "Frozen Yogurt",
        x3: "Frozen Yogurt",
        x4: "Frozen Yogurt",
        x5: "Frozen Yogurt",
        x6: "Frozen Yogurt",
        temputure: 159,
      },
      {
        x1: "Frozen Yogurt",
        x2: "Frozen Yogurt",
        x3: "Frozen Yogurt",
        x4: "Frozen Yogurt",
        x5: "Frozen Yogurt",
        x6: "Frozen Yogurt",
        temputure: 159,
      },
      {
        x1: "Frozen Yogurt",
        x2: "Frozen Yogurt",
        x3: "Frozen Yogurt",
        x4: "Frozen Yogurt",
        x5: "Frozen Yogurt",
        x6: "Frozen Yogurt",
        temputure: 159,
      },
      {
        x1: "Frozen Yogurt",
        x2: "Frozen Yogurt",
        x3: "Frozen Yogurt",
        x4: "Frozen Yogurt",
        x5: "Frozen Yogurt",
        x6: "Frozen Yogurt",
        temputure: 159,
      },
      {
        x1: "Frozen Yogurt",
        x2: "Frozen Yogurt",
        x3: "Frozen Yogurt",
        x4: "Frozen Yogurt",
        x5: "Frozen Yogurt",
        x6: "Frozen Yogurt",
        temputure: 159,
      },
      {
        x1: "Frozen Yogurt",
        x2: "Frozen Yogurt",
        x3: "Frozen Yogurt",
        x4: "Frozen Yogurt",
        x5: "Frozen Yogurt",
        x6: "Frozen Yogurt",
        temputure: 159,
      },
      {
        x1: "Frozen Yogurt",
        x2: "Frozen Yogurt",
        x3: "Frozen Yogurt",
        x4: "Frozen Yogurt",
        x5: "Frozen Yogurt",
        x6: "Frozen Yogurt",
        temputure: 159,
      },
      {
        x1: "Frozen Yogurt",
        x2: "Frozen Yogurt",
        x3: "Frozen Yogurt",
        x4: "Frozen Yogurt",
        x5: "Frozen Yogurt",
        x6: "Frozen Yogurt",
        temputure: 159,
      },
      {
        x1: "Frozen Yogurt",
        x2: "Frozen Yogurt",
        x3: "Frozen Yogurt",
        x4: "Frozen Yogurt",
        x5: "Frozen Yogurt",
        x6: "Frozen Yogurt",
        temputure: 159,
      },
    ],
  }),
};
</script>
<style scoped>
</style>