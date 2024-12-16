<template>
  <div class="container">
    <h1 class="title is-1 has-text-centered">Cotizador de Impresión 3D</h1>
    <form @submit.prevent="cotizar" class="form">
      <div class="field">
        <label class="label">Ancho (cm):</label>
        <div class="control">
          <input type="number" v-model.number="form.ancho" required @input="calcularVolumen" class="input">
        </div>
      </div>

      <div class="field">
        <label class="label">Alto (cm):</label>
        <div class="control">
          <input type="number" v-model.number="form.alto" required @input="calcularVolumen" class="input">
        </div>
      </div>

      <div class="field">
        <label class="label">Profundidad (cm):</label>
        <div class="control">
          <input type="number" v-model.number="form.profundidad" required @input="calcularVolumen" class="input">
        </div>
      </div>

      <div class="field">
        <label class="label">Volumen total (cm³):</label>
        <div class="control">
          <input type="number" v-model.number="form.volumen" required readonly class="input">
        </div>
      </div>

      <div class="field">
        <label class="label">Peso material (g):</label>
        <div class="control">
          <input type="number" v-model.number="form.peso" required class="input">
        </div>
      </div>

      <div class="field">
        <label class="label">Tiempo de impresión (horas):</label>
        <div class="control">
          <input type="number" v-model.number="form.tiempo" required class="input">
        </div>
      </div>

      <div class="field">
        <label class="label">Tipo de filamento:</label>
        <div class="control">
          <div class="select">
            <select v-model="form.tipo_filamento" required class="input">
              <option value="pla">PLA</option>
              <option value="ptge">PTGE</option>
              <option value="abs">ABS</option>
              <option value="tpu">TPU</option>
            </select>
          </div>
        </div>
      </div>

      <div class="field">
        <label class="label">¿Requiere acabados?</label>
        <div class="control">
          <div class="select">
            <select v-model="form.acabados" required @change="toggleAcabados" class="input">
              <option value="true">Sí</option>
              <option value="false">No</option>
            </select>
          </div>
        </div>
      </div>

      <div class="field">
        <label class="label">Costo de envío:</label>
        <div class="control">
          <input type="number" v-model.number="form.envio" required class="input">
        </div>
      </div>

      <div v-if="form.acabados === 'true'" class="acabados-fields">
        <div class="field">
          <label class="label">Duración de pintado (horas):</label>
          <div class="control">
            <input type="number" v-model.number="form.duracion_pintado" required class="input">
          </div>
        </div>

        <div class="field">
          <label class="label">Tipo de acabado:</label>
          <div class="control">
            <div class="select">
              <select v-model="form.tipo_acabado" required class="input">
                <option value="mate">Mate</option>
                <option value="brillante">Brillante</option>
                <option value="texturizado">Texturizado</option>
              </select>
            </div>
          </div>
        </div>

        <div class="field">
          <label class="label">Número de colores:</label>
          <div class="control">
            <input type="number" v-model.number="form.numero_colores" required class="input">
          </div>
        </div>

        <div class="field">
          <label class="label">Dificultad de acceso:</label>
          <div class="control">
            <div class="select">
              <select v-model="form.dificultad_acceso" required class="input">
                <option value="bajo">Bajo</option>
                <option value="medio">Medio</option>
                <option value="alto">Alto</option>
              </select>
            </div>
          </div>
        </div>
      </div>

      <div class="field is-grouped is-grouped-centered">
        <div class="control">
          <button type="submit" class="button is-primary">Calcular Cotización</button>
        </div>
        <div class="control">
          <button type="button" @click="resetForm" class="button is-link">Cancelar</button>
        </div>
      </div>
    </form>

    <div v-if="cotizacion" class="box">
      <h2 class="subtitle">Resultado de la Cotización</h2>
      <p>Subtotal: ${{ cotizacion.subtotal.toFixed(2) }}</p>
      <p>Costo de envío: ${{ cotizacion.costo_envio.toFixed(2) }}</p>
      <p>Total: ${{ cotizacion.total_final.toFixed(2) }}</p>
      <button @click="confirmarPedido" class="button is-success">Confirmación de Pedido</button>
    </div>

    <div v-if="error" class="notification is-danger">
      <p>Error: {{ error }}</p>
    </div>

    <!-- Modal para confirmar pedido -->
    <div v-if="showModal" class="modal is-active">
      <div class="modal-background"></div>
      <div class="modal-content">
        <div class="box">
          <h2 class="subtitle">Confirmar Pedido</h2>
          <form @submit.prevent="enviarPedido">
            <div class="field">
              <label class="label">Correo:</label>
              <div class="control">
                <input type="email" v-model="cliente.email" required @input="autocompletarCliente" class="input">
              </div>
            </div>

            <div class="field">
              <label class="label">Teléfono:</label>
              <div class="control">
                <input type="text" v-model="cliente.telefono" required @input="autocompletarCliente" class="input">
              </div>
            </div>

            <p>Subtotal: ${{ cotizacion ? cotizacion.subtotal.toFixed(2) : '0.00' }}</p>
            <p>Costo de envío: ${{ cotizacion ? cotizacion.costo_envio.toFixed(2) : '0.00' }}</p>
            <p>Total a pagar: ${{ cotizacion ? cotizacion.total_final.toFixed(2) : '0.00' }}</p>

            <div class="field is-grouped">
              <div class="control">
                <button type="submit" class="button is-link">Enviar Pedido</button>
              </div>
              <div class="control">
                <button type="button" @click="showModal = false" class="button is-link is-light">Cancelar</button>
              </div>
            </div>
          </form>
        </div>
      </div>
      <button class="modal-close is-large" @click="showModal = false" aria-label="close"></button>
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
        ancho: "",
        alto: "",
        profundidad: "",
        volumen: 0,
        peso: "",
        tiempo: "",
        tipo_filamento: "pla",
        acabados: "false",
        envio: 0,
        duracion_pintado: 0,
        tipo_acabado: "mate",
        numero_colores: 0,
        dificultad_acceso: "bajo"
      },
      cotizacion: null,
      showModal: false,
      cliente: {
        email: "",
        telefono: "",
        nombre: "",
        whatsapp: "",
      },
      error: null
    };
  },
  methods: {
    calcularVolumen() {
      this.form.volumen = this.form.ancho * this.form.alto * this.form.profundidad;
    },
    toggleAcabados() {
      if (this.form.acabados === "false") {
        this.form.duracion_pintado = 0;
        this.form.tipo_acabado = "mate";
        this.form.numero_colores = 0;
        this.form.dificultad_acceso = "bajo";
      }
    },
    resetForm() {
      this.form = {
        ancho: "",
        alto: "",
        profundidad: "",
        volumen: 0,
        peso: "",
        tiempo: "",
        tipo_filamento: "pla",
        acabados: "false",
        envio: 0,
        duracion_pintado: 0,
        tipo_acabado: "mate",
        numero_colores: 0,
        dificultad_acceso: "bajo"
      };
    },
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
      this.cliente.nombre = this.extractNameFromEmail(this.cliente.email);
      this.cliente.whatsapp = this.cliente.telefono;
    },
    extractNameFromEmail(email) {
      return email.split('@')[0];
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

      const totalConIVA = this.cotizacion.total_final; // Usamos el total final de la cotización

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
      return this.cotizacion ? this.cotizacion.total_final : 0;
    }
  }
};
</script>

<style>
@import "https://cdn.jsdelivr.net/npm/bulma@0.9.3/css/bulma.min.css";

.form {
  max-width: 600px;
  margin: 0 auto;
  padding: 2rem;
  background: #f5f5f5;
  border-radius: 8px;
  box-shadow: 0 2px 3px rgba(10, 10, 10, 0.1), 0 0 0 1px rgba(10, 10, 10, 0.1);
}

.modal-content .box {
  padding: 2rem;
}

.acabados-fields {
  margin-top: 1rem;
}
</style>
