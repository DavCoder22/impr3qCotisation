<template>
  <div>
    <h1>Cotizador de Impresión 3D</h1>
    <form @submit.prevent="cotizar">
      <label>Volumen total (cm³):</label>
      <input type="number" v-model.number="form.volumen" required />

      <label>Peso material (g):</label>
      <input type="number" v-model.number="form.peso" required />

      <label>Tiempo de impresión (horas):</label>
      <input type="number" v-model.number="form.tiempo" required />

      <label>Tipo de filamento:</label>
      <select v-model="form.tipo_filamento" required>
        <option value="pla">PLA</option>
        <option value="ptge">PTGE</option>
        <option value="abs">ABS</option>
        <option value="tpu">TPU</option>
      </select>

      <label>¿Requiere acabados?</label>
      <select v-model="form.acabados" required>
        <option value="true">Sí</option>
        <option value="false">No</option>
      </select>

      <label>Costo de envío:</label>
      <input type="number" v-model.number="form.envio" required />

      <button type="submit">Calcular Cotización</button>
    </form>

    <div v-if="cotizacion">
      <h2>Resultado de la Cotización</h2>
      <p>Subtotal: ${{ cotizacion.subtotal.toFixed(2) }}</p>
      <button @click="confirmarPedido">Confirmación de Pedido</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { createClient } from "@supabase/supabase-js";

const supabase = createClient("https://tu-supabase-url.supabase.co", "tu-clave-publica");

export default {
  data() {
    return {
      form: {
        volumen: "",
        peso: "",
        tiempo: "",
        tipo_filamento: "pla",
        acabados: "false",
        envio: "",
      },
      cotizacion: null,
    };
  },
  methods: {
    async cotizar() {
      try {
        const response = await axios.post("http://localhost:5000/cotizar", this.form);
        this.cotizacion = response.data;
      } catch (error) {
        console.error("Error al calcular la cotización:", error);
      }
    },
    async confirmarPedido() {
      if (confirm("¿Deseas confirmar el pedido?")) {
        try {
          const { error } = await supabase.from("pedidos").insert([{ ...this.form, total: this.cotizacion.total }]);
          if (error) throw error;
          alert("Pedido guardado exitosamente.");
        } catch (error) {
          console.error("Error al guardar el pedido:", error);
          alert("No se pudo guardar el pedido.");
        }
      }
    },
  },
};
</script>

<style>
form {
  display: flex;
  flex-direction: column;
  max-width: 400px;
}
label {
  margin-top: 10px;
}
button {
  margin-top: 20px;
}
</style>
