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

    <div v-if="error">
      <p>Error: {{ error }}</p>
    </div>

    <!-- Modal para confirmar pedido -->
    <div v-if="showModal" class="modal">
      <div class="modal-content">
        <h2>Confirmar Pedido</h2>
        <form @submit.prevent="enviarPedido">
          <label>Correo:</label>
          <input type="email" v-model="cliente.email" required @input="autocompletarCliente" />

          <label>Teléfono:</label>
          <input type="text" v-model="cliente.telefono" required @input="autocompletarCliente" />

          <p>Total a pagar: ${{ totalConIVA.toFixed(2) }}</p>

          <button type="submit">Enviar Pedido</button>
          <button type="button" @click="showModal = false">Cancelar</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { supabase } from '@/supabase'; // Importa Supabase desde el archivo supabase.js usando una ruta relativa

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
      showModal: false,
      cliente: {
        email: "",
        telefono: "",
        nombre: "",
        whatsapp: "",
        correo: ""
      },
      error: null
    };
  },
  methods: {
    async cotizar() {
      try {
        const response = await axios.post("http://localhost:5000/cotizar", this.form);
        this.cotizacion = response.data;
        this.error = null;
      } catch (error) {
        console.error("Error al calcular la cotización:", error);
        this.error = (error.response && error.response.data && error.response.data.error) ? error.response.data.error : "Error al calcular la cotización";
      }
    },
    confirmarPedido() {
      this.showModal = true;
    },
    autocompletarCliente() {
      this.cliente.nombre = this.cliente.email;
      this.cliente.whatsapp = this.cliente.telefono;
      this.cliente.correo = this.cliente.email;
    },
    async enviarPedido() {
      if (!this.cotizacion) {
        console.error("No hay cotización disponible.");
        alert("No hay cotización disponible.");
        return;
      }

      if (!supabase) {
        console.error("Supabase no está inicializado.");
        alert("Supabase no está inicializado.");
        return;
      }

      const totalConIVA = this.cotizacion.subtotal * 1.16; // Asumiendo un IVA del 16%

      // Verificar y crear el estado del pedido si no existe
      let estadoId;
      const { data: estados, error: errorEstados } = await supabase
        .from('estados_pedido')
        .select('id')
        .eq('nombre', 'pendiente');

      if (errorEstados) {
        console.error("Error al obtener estados del pedido:", errorEstados);
        alert("No se pudo obtener los estados del pedido.");
        return;
      }

      if (estados && estados.length > 0) {
        estadoId = estados[0].id;
      } else {
        const { data: nuevoEstado, error: errorNuevoEstado } = await supabase
          .from('estados_pedido')
          .insert([{ nombre: 'pendiente' }]);

        if (errorNuevoEstado) {
          console.error("Error al crear nuevo estado del pedido:", errorNuevoEstado);
          alert("No se pudo crear el estado del pedido.");
          return;
        }

        estadoId = nuevoEstado[0].id;
      }

      // Verificar y crear el cliente si no existe
      let clienteId;
      const { data: clientes, error: errorClientes } = await supabase
        .from('clientes')
        .select('id')
        .eq('email', this.cliente.email);

      if (errorClientes) {
        console.error("Error al obtener clientes:", errorClientes);
        alert("No se pudo obtener los clientes.");
        return;
      }

      if (clientes && clientes.length > 0) {
        clienteId = clientes[0].id;
      } else {
        const { data: nuevoCliente, error: errorNuevoCliente } = await supabase
          .from('clientes')
          .insert([{
            nombre: this.cliente.nombre,
            email: this.cliente.email,
            telefono: this.cliente.telefono,
            whatsapp: this.cliente.whatsapp,
            correo: this.cliente.correo
          }]);

        if (errorNuevoCliente) {
          console.error("Error al crear nuevo cliente:", errorNuevoCliente);
          alert("No se pudo crear el cliente.");
          return;
        }

        clienteId = nuevoCliente[0].id;
      }

      // Crear el pedido
      const pedido = {
        volumen: this.form.volumen,
        peso: this.form.peso,
        tiempo: this.form.tiempo,
        tipo_filamento: this.form.tipo_filamento,
        acabados: this.form.acabados === "true",
        envio: this.form.envio,
        total: totalConIVA,
        estado_id: estadoId,
        cliente_id: clienteId,
        precio_filamento_gramo: this.cotizacion.precio_filamento_gramo,
        fecha_pedido: new Date().toISOString(),
        precio_venta: this.cotizacion.total_final
      };

      try {
        const { error } = await supabase.from("pedidos").insert([pedido]);
        if (error) throw error;
        alert("Pedido guardado exitosamente.");
        this.showModal = false;
      } catch (error) {
        console.error("Error al guardar el pedido:", error);
        alert("No se pudo guardar el pedido.");
      }
    }
  },
  computed: {
    totalConIVA() {
      return this.cotizacion ? this.cotizacion.subtotal * 1.16 : 0;
    }
  }
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
.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}
.modal-content {
  background: white;
  padding: 20px;
  border-radius: 5px;
}
</style>
