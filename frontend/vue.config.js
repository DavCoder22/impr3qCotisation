const path = require('path');

module.exports = {
  // Configuración básica
  publicPath: '/',
  outputDir: 'dist',
  assetsDir: 'static',
  lintOnSave: process.env.NODE_ENV !== 'production',
  productionSourceMap: false,
  devServer: {
    port: 8080,
    open: true,
    overlay: {
      warnings: false,
      errors: true
    }
  },
  // Configuración adicional según sea necesario
  pluginOptions: {
    'define-options': {
      VUE_APP_SUPABASE_URL: JSON.stringify(process.env.VUE_APP_SUPABASE_URL),
      VUE_APP_SUPABASE_ANON_KEY: JSON.stringify(process.env.VUE_APP_SUPABASE_ANON_KEY),
    }
  },
  configureWebpack: {
    resolve: {
      alias: {
        '@': path.resolve(__dirname, 'src')
      }
    }
  }
};
