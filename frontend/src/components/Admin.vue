<template>
  <div class="container">
    <h1 class="title is-1 has-text-centered">Administración de Pedidos</h1>
    <div v-if="!authenticated">
      <div class="field">
        <label class="label">Contraseña:</label>
        <div class="control">
          <input type="password" v-model="password" @keyup.enter="authenticate" class="input">
        </div>
      </div>
      <div class="field is-grouped is-grouped-centered">
        <div class="control">
          <button type="button" @click="authenticate" class="button is-primary">Ingresar</button>
        </div>
      </div>
    </div>
    <div v-if="authenticated">
      <div class="buttons">
        <button @click="loadPedidos" class="button is-info">Actualizar Pedidos</button>
        <button @click="logout" class="button is-danger">Cerrar Sesión</button>
      </div>
      <table class="table is-fullwidth">
        <thead>
          <tr>
            <th>ID</th>
            <th>Volumen</th>
            <th>Peso</th>
            <th>Tiempo</th>
            <th>Tipo de Filamento</th>
            <th>Acabados</th>
            <th>Envío</th>
            <th>Estado</th>
            <th>Precio de Venta</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="pedido in pedidos" :key="pedido.id">
            <td>{{ pedido.id }}</td>
            <td>
              <input type="number" v-model="pedido.volumen" class="input">
            </td>
            <td>
              <input type="number" v-model="pedido.peso" class="input">
            </td>
            <td>
              <input type="number" v-model="pedido.tiempo" class="input">
            </td>
            <td>
              <select v-model="pedido.tipo_filamento" class="input">
                <option value="pla">PLA</option>
                <option value="ptge">PTGE</option>
                <option value="abs">ABS</option>
                <option value="tpu">TPU</option>
              </select>
            </td>
            <td>
              <select v-model="pedido.acabados" class="input">
                <option value="true">Sí</option>
                <option value="false">No</option>
              </select>
            </td>
            <td>
              <input type="number" v-model="pedido.envio" class="input">
            </td>
            <td>
              <select v-model="pedido.estado_id" class="input">
                <option v-for="estado in estados" :value="estado.id" :key="estado.id">{{ estado.nombre }}</option>
              </select>
            </td>
            <td>{{ pedido.precio_venta.toFixed(2) }}</td>
            <td>
              <button @click="savePedido(pedido)" class="button is-success">Guardar</button>
              <button @click="confirmDelete(pedido.id)" class="button is-danger">Eliminar</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import { supabase } from '@/supabase'; // Importa Supabase desde el archivo supabase.js usando una ruta relativa
import axios from 'axios';

export default {
  data() {
    return {
      password: '',
      authenticated: false,
      pedidos: [],
      estados: [],
      pedidoToDelete: null,
      sessionTimeout: null,
      keepAliveInterval: null
    };
  },
  methods: {
    authenticate() {
      if (this.password === 'Sebasalejandro22IMPR3Q') {
        this.authenticated = true;
        this.loadPedidos();
        this.loadEstados();
        this.startSessionTimeout();
        this.startKeepAlive();
      } else {
        alert('Contraseña incorrecta');
      }
    },
    async loadPedidos() {
      const { data, error } = await supabase
        .from('pedidos')
        .select('*');
      if (error) {
        console.error('Error al cargar los pedidos:', error);
      } else {
        this.pedidos = data;
      }
    },
    async loadEstados() {
      const { data, error } = await supabase
        .from('estados_pedido')
        .select('*');
      if (error) {
        console.error('Error al cargar los estados:', error);
      } else {
        this.estados = data;
      }
    },
    async savePedido(pedido) {
      // Recalcular el precio antes de guardar
      await this.recalcularPrecio(pedido);

      const { data, error } = await supabase
        .from('pedidos')
        .update([pedido])
        .eq('id', pedido.id);
      if (error) {
        console.error('Error al guardar el pedido:', error);
      } else {
        alert('Pedido guardado exitosamente.');
      }
    },
    async recalcularPrecio(pedido) {
      try {
        const response = await axios.post("http://localhost:5000/cotizar", {
          ...pedido,
          precio_filamento_gramo: pedido.precio_filamento_gramo
        });
        pedido.precio_venta = response.data.total_final;
      } catch (error) {
        console.error("Error al recalcular la cotización:", error);
      }
    },
    confirmDelete(id) {
      this.pedidoToDelete = id;
      if (confirm('¿Estás seguro de que deseas eliminar este pedido?')) {
        this.deletePedido(id);
      }
    },
    async deletePedido(id) {
      const { error } = await supabase
        .from('pedidos')
        .delete()
        .eq('id', id);
      if (error) {
        console.error('Error al eliminar el pedido:', error);
      } else {
        this.pedidos = this.pedidos.filter(pedido => pedido.id !== id);
      }
    },
    logout() {
      this.authenticated = false;
      clearInterval(this.sessionTimeout);
      clearInterval(this.keepAliveInterval);
      this.password = '';
    },
    startSessionTimeout() {
      this.sessionTimeout = setInterval(() => {
        if (confirm('¿Sigues atendiendo?')) {
          this.startSessionTimeout();
        } else {
          this.logout();
        }
      }, 1200000); // 20 minutos
    },
    startKeepAlive() {
      this.keepAliveInterval = setInterval(() => {
        if (confirm('¿Sigues atendiendo?')) {
          this.startKeepAlive();
        } else {
          this.logout();
        }
      }, 15000); // 15 segundos
    }
  }
};
</script>

<style>
@import "https://cdn.jsdelivr.net/npm/bulma@0.9.3/css/bulma.min.css";

.container {
  padding: 2rem;
}

.table {
  margin-top: 2rem;
}

.buttons {
  margin-bottom: 2rem;
  display: flex;
  justify-content: space-between;
}
</style>
