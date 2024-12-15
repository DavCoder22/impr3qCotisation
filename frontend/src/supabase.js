import { createClient } from '@supabase/supabase-js';

// Define tus credenciales directamente aquí
const supabaseUrl = 'https://helaklijjobvxzgysrmn.supabase.co';
const supabaseKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImhlbGFrbGlqam9idnh6Z3lzcm1uIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzM3MjY1MjYsImV4cCI6MjA0OTMwMjUyNn0.CUotpjQMW2FbI1aWvzqjFNVMA21f6sLhcSD_5e3PWyM';

export const supabase = createClient(supabaseUrl, supabaseKey);
