import { createClient } from '@supabase/supabase-js';

// Accede a las variables de entorno definidas en .env
const SUPABASE_URL = import.meta.env.VITE_SUPABASE_URL;
const SUPABASE_ANON_KEY = import.meta.env.VITE_SUPABASE_ANON_KEY;

// Crea el cliente de Supabase
export const supabase = createClient(SUPABASE_URL, SUPABASE_ANON_KEY);
