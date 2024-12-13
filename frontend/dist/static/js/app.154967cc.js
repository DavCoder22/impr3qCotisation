(function(e){function t(t){for(var o,i,u=t[0],l=t[1],s=t[2],c=0,m=[];c<u.length;c++)i=u[c],Object.prototype.hasOwnProperty.call(n,i)&&n[i]&&m.push(n[i][0]),n[i]=0;for(o in l)Object.prototype.hasOwnProperty.call(l,o)&&(e[o]=l[o]);p&&p(t);while(m.length)m.shift()();return a.push.apply(a,s||[]),r()}function r(){for(var e,t=0;t<a.length;t++){for(var r=a[t],o=!0,i=1;i<r.length;i++){var l=r[i];0!==n[l]&&(o=!1)}o&&(a.splice(t--,1),e=u(u.s=r[0]))}return e}var o={},n={app:0},a=[];function i(e){return u.p+"static/js/"+({}[e]||e)+"."+{"chunk-2d0e2721":"39716f46"}[e]+".js"}function u(t){if(o[t])return o[t].exports;var r=o[t]={i:t,l:!1,exports:{}};return e[t].call(r.exports,r,r.exports,u),r.l=!0,r.exports}u.e=function(e){var t=[],r=n[e];if(0!==r)if(r)t.push(r[2]);else{var o=new Promise((function(t,o){r=n[e]=[t,o]}));t.push(r[2]=o);var a,l=document.createElement("script");l.charset="utf-8",l.timeout=120,u.nc&&l.setAttribute("nonce",u.nc),l.src=i(e);var s=new Error;a=function(t){l.onerror=l.onload=null,clearTimeout(c);var r=n[e];if(0!==r){if(r){var o=t&&("load"===t.type?"missing":t.type),a=t&&t.target&&t.target.src;s.message="Loading chunk "+e+" failed.\n("+o+": "+a+")",s.name="ChunkLoadError",s.type=o,s.request=a,r[1](s)}n[e]=void 0}};var c=setTimeout((function(){a({type:"timeout",target:l})}),12e4);l.onerror=l.onload=a,document.head.appendChild(l)}return Promise.all(t)},u.m=e,u.c=o,u.d=function(e,t,r){u.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:r})},u.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},u.t=function(e,t){if(1&t&&(e=u(e)),8&t)return e;if(4&t&&"object"===typeof e&&e&&e.__esModule)return e;var r=Object.create(null);if(u.r(r),Object.defineProperty(r,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var o in e)u.d(r,o,function(t){return e[t]}.bind(null,o));return r},u.n=function(e){var t=e&&e.__esModule?function(){return e["default"]}:function(){return e};return u.d(t,"a",t),t},u.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},u.p="/",u.oe=function(e){throw console.error(e),e};var l=window["webpackJsonp"]=window["webpackJsonp"]||[],s=l.push.bind(l);l.push=t,l=l.slice();for(var c=0;c<l.length;c++)t(l[c]);var p=s;a.push([0,"chunk-vendors"]),r()})({0:function(e,t,r){e.exports=r("56d7")},"0dd9":function(e,t,r){},"56d7":function(e,t,r){"use strict";r.r(t);var o=r("2b0e"),n=function(){var e=this,t=e._self._c;return t("div",{attrs:{id:"app"}},[t("router-view")],1)},a=[],i={name:"App"},u=i,l=(r("7e91"),r("2877")),s=Object(l["a"])(u,n,a,!1,null,null,null),c=s.exports,p=r("8c4f"),m=function(){var e=this,t=e._self._c;return t("div",[t("h1",[e._v("Cotizador de Impresión 3D")]),t("form",{on:{submit:function(t){return t.preventDefault(),e.cotizar.apply(null,arguments)}}},[t("label",[e._v("Volumen total (cm³):")]),t("input",{directives:[{name:"model",rawName:"v-model.number",value:e.form.volumen,expression:"form.volumen",modifiers:{number:!0}}],attrs:{type:"number",required:""},domProps:{value:e.form.volumen},on:{input:function(t){t.target.composing||e.$set(e.form,"volumen",e._n(t.target.value))},blur:function(t){return e.$forceUpdate()}}}),t("label",[e._v("Peso material (g):")]),t("input",{directives:[{name:"model",rawName:"v-model.number",value:e.form.peso,expression:"form.peso",modifiers:{number:!0}}],attrs:{type:"number",required:""},domProps:{value:e.form.peso},on:{input:function(t){t.target.composing||e.$set(e.form,"peso",e._n(t.target.value))},blur:function(t){return e.$forceUpdate()}}}),t("label",[e._v("Tiempo de impresión (horas):")]),t("input",{directives:[{name:"model",rawName:"v-model.number",value:e.form.tiempo,expression:"form.tiempo",modifiers:{number:!0}}],attrs:{type:"number",required:""},domProps:{value:e.form.tiempo},on:{input:function(t){t.target.composing||e.$set(e.form,"tiempo",e._n(t.target.value))},blur:function(t){return e.$forceUpdate()}}}),t("label",[e._v("Tipo de filamento:")]),t("select",{directives:[{name:"model",rawName:"v-model",value:e.form.tipo_filamento,expression:"form.tipo_filamento"}],attrs:{required:""},on:{change:function(t){var r=Array.prototype.filter.call(t.target.options,(function(e){return e.selected})).map((function(e){var t="_value"in e?e._value:e.value;return t}));e.$set(e.form,"tipo_filamento",t.target.multiple?r:r[0])}}},[t("option",{attrs:{value:"pla"}},[e._v("PLA")]),t("option",{attrs:{value:"ptge"}},[e._v("PTGE")]),t("option",{attrs:{value:"abs"}},[e._v("ABS")]),t("option",{attrs:{value:"tpu"}},[e._v("TPU")])]),t("label",[e._v("¿Requiere acabados?")]),t("select",{directives:[{name:"model",rawName:"v-model",value:e.form.acabados,expression:"form.acabados"}],attrs:{required:""},on:{change:function(t){var r=Array.prototype.filter.call(t.target.options,(function(e){return e.selected})).map((function(e){var t="_value"in e?e._value:e.value;return t}));e.$set(e.form,"acabados",t.target.multiple?r:r[0])}}},[t("option",{attrs:{value:"true"}},[e._v("Sí")]),t("option",{attrs:{value:"false"}},[e._v("No")])]),t("label",[e._v("Costo de envío:")]),t("input",{directives:[{name:"model",rawName:"v-model.number",value:e.form.envio,expression:"form.envio",modifiers:{number:!0}}],attrs:{type:"number",required:""},domProps:{value:e.form.envio},on:{input:function(t){t.target.composing||e.$set(e.form,"envio",e._n(t.target.value))},blur:function(t){return e.$forceUpdate()}}}),t("button",{attrs:{type:"submit"}},[e._v("Calcular Cotización")])]),e.cotizacion?t("div",[t("h2",[e._v("Resultado de la Cotización")]),t("p",[e._v("Subtotal: $"+e._s(e.cotizacion.subtotal.toFixed(2)))]),t("button",{on:{click:e.confirmarPedido}},[e._v("Confirmar Pedido")])]):e._e()])},f=[],d=r("cee4"),v=r("940b");const b=Object(v["a"])("https://tu-supabase-url.supabase.co","tu-clave-publica");var h={data(){return{form:{volumen:"",peso:"",tiempo:"",tipo_filamento:"pla",acabados:"false",envio:""},cotizacion:null}},methods:{async cotizar(){try{const e=await d["a"].post("http://localhost:5000/cotizar",this.form);this.cotizacion=e.data}catch(e){console.error("Error al calcular la cotización:",e)}},async confirmarPedido(){if(confirm("¿Deseas confirmar el pedido?"))try{const{error:e}=await b.from("pedidos").insert([{...this.form,total:this.cotizacion.total}]);if(e)throw e;alert("Pedido guardado exitosamente.")}catch(e){console.error("Error al guardar el pedido:",e),alert("No se pudo guardar el pedido.")}}}},g=h,_=(r("b60c"),Object(l["a"])(g,m,f,!1,null,null,null)),y=_.exports;o["a"].use(p["a"]);var w=new p["a"]({mode:"history",base:"/",routes:[{path:"/",name:"CotizadorPrincipal",component:y}]});o["a"].config.productionTip=!1,new o["a"]({router:w,render:e=>e(c)}).$mount("#app")},"7e91":function(e,t,r){"use strict";r("0dd9")},"8fd2":function(e,t,r){},b60c:function(e,t,r){"use strict";r("8fd2")}});